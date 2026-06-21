# Environment And Outputs

## Required Environment Variables

- `IMAGE_BASE_URL`: custom OpenAI-compatible API root, usually ending with `/v1`
- `IMAGE_API_KEY`: API key used for the request

The bundled script reads both values from the environment at runtime. It does not accept them as CLI flags.

## Endpoint Handling

- If `IMAGE_BASE_URL` ends with `/images/generations`, the script uses it directly.
- Otherwise the script appends `/images/generations`.
- Keep the base URL stable across runs so dry-run output and live output target the same endpoint.
- If a run includes `--image-file`, the helper encodes each local file into a base64 data URI and sends the array through `image_urls`.
- In image-to-image mode, if `size` is left at the default `auto`, the helper omits the `size` field so the upstream endpoint may keep the input-image resolution contract.
- For workflow background-removal retries, use prompt text exactly `移除背景` together with `image_urls`; do not switch to `/images/edits`.

## Output Strategy

- Use `--out` for one image.
- Use `--out-dir` for multiple images.
- The script creates parent directories automatically.
- Use `--force` only when overwriting an existing file is intentional.

## Response Expectations

The script expects a JSON payload compatible with the OpenAI Images API and writes `b64_json` results to local files. If the endpoint returns a non-compatible structure, surface the response body and stop instead of guessing how to decode it.
