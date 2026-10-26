#!/usr/bin/env bash
# Download one Piper voice (model + config) into $PIPER_DIR (default ./piper).
#   tools/get_piper_voice.sh pl_PL-gosia-medium
set -euo pipefail
V="$1"; D="${PIPER_DIR:-piper}"; mkdir -p "$D"
LOC="${V%%-*}"; LANG="${LOC%%_*}"; REST="${V#*-}"; NAME="${REST%-*}"; Q="${REST##*-}"
BASE="https://huggingface.co/rhasspy/piper-voices/resolve/main/$LANG/$LOC/$NAME/$Q/$V"
for ext in onnx onnx.json; do [ -s "$D/$V.$ext" ] || curl -sSfL -o "$D/$V.$ext" "$BASE.$ext"; done
ls -la "$D/$V".onnx*
