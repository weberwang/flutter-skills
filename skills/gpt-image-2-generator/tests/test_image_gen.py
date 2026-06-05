"""gpt-image-2 生成脚本的异步任务兼容测试。"""

from __future__ import annotations

import base64
import importlib.util
from pathlib import Path


def _load_module():
    """加载待测试的脚本模块。"""
    script_path = (
        Path(__file__).resolve().parent.parent / "scripts" / "image_gen.py"
    )
    spec = importlib.util.spec_from_file_location(
        "gpt_image_2_generator_image_gen",
        script_path,
    )
    assert spec is not None
    loader = spec.loader
    assert loader is not None
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


def test_resolve_image_bytes_supports_sync_b64_response() -> None:
    """同步接口仍应继续支持 b64_json 返回。"""
    module = _load_module()
    expected = b"fox"
    response = {
        "data": [
            {
                "b64_json": base64.b64encode(expected).decode("utf-8"),
            },
        ],
    }

    image_bytes = module._resolve_image_bytes(  # noqa: SLF001
        base_url="https://api.example.com/v1",
        api_key="test-key",
        response=response,
        timeout_seconds=5,
    )

    assert image_bytes == [expected]


def test_resolve_image_bytes_polls_async_task_until_completed() -> None:
    """异步任务返回 task_id 时应轮询并下载最终图片。"""
    module = _load_module()
    calls: list[str] = []

    def fake_request_json(
        url: str,
        api_key: str,
        timeout_seconds: int,
        *,
        method: str = "GET",
        payload: dict[str, object] | None = None,
    ) -> dict[str, object]:
        del api_key, timeout_seconds, method, payload
        calls.append(url)
        if len(calls) == 1:
            return {
                "code": 200,
                "data": {
                    "status": "processing",
                },
            }
        return {
            "code": 200,
            "data": {
                "status": "completed",
                "result": {
                    "images": [
                        {
                            "url": [
                                "https://cdn.example.com/luoluofox.png",
                            ],
                        },
                    ],
                },
            },
        }

    def fake_download_bytes(
        url: str,
        timeout_seconds: int,
    ) -> bytes:
        del timeout_seconds
        assert url == "https://cdn.example.com/luoluofox.png"
        return b"png-bytes"

    module._request_json = fake_request_json  # type: ignore[attr-defined]
    module._download_bytes = fake_download_bytes  # type: ignore[attr-defined]
    module.time.sleep = lambda _: None

    image_bytes = module._resolve_image_bytes(  # noqa: SLF001
        base_url="https://api.example.com/v1",
        api_key="test-key",
        response={
            "data": [
                {
                    "status": "submitted",
                    "task_id": "task_123",
                },
            ],
        },
        timeout_seconds=5,
    )

    assert image_bytes == [b"png-bytes"]
    assert calls == [
        "https://api.example.com/v1/tasks/task_123",
        "https://api.example.com/v1/tasks/task_123",
    ]
