#!/data/data/com.termux/files/usr/bin/bash

BASE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$BASE/linux-root"

unset LD_PRELOAD
unset LD_LIBRARY_PATH

export TMPDIR=/tmp
export TMPDIR=/chrome-tmp

proot \
  -S "$ROOT" \
  /headless-shell/headless-shell \
  --headless \
  --no-sandbox \
  --disable-dev-shm-usage \
  --disable-gpu \
  --disable-features=UseDBus \
  --remote-debugging-address=127.0.0.1 \
  --remote-debugging-port=9222 \
  --remote-allow-origins=* \
  --user-data-dir=/chrome-tmp/profile
  --disk-cache-dir=/chrome-tmp/cache
  --disable-dev-shm-usage
  about:blank
  "$@"
