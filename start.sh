#!/usr/bin/env bash
set -euo pipefail

# The system Ruby (2.6) is too old for this site's gems; use the Homebrew one.
RUBY_BIN="/opt/homebrew/opt/ruby/bin"
if [ -d "$RUBY_BIN" ]; then
  export PATH="$RUBY_BIN:$PATH"
else
  echo "Homebrew Ruby not found at $RUBY_BIN — run: brew install ruby" >&2
  exit 1
fi

cd "$(dirname "$0")"
bundle check >/dev/null 2>&1 || bundle install
exec bundle exec jekyll serve --trace --open-url --livereload
