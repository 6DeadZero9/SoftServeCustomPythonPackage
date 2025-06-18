#!/bin/bash
set -euo pipefail

cd "$SRC_DIR"

conan profile detect --force || echo "Skipping profile detection (non-zero exit code)"
conan install . --build=missing
conan build .

PACKAGE_DIR="$SRC_DIR/src/soft_serve_custom_python_package"

find . \( -name "*.so" -o -name "*.dll" \) -print0 | xargs -0 cp -n -t "$PACKAGE_DIR" 

$PYTHON -m pip install "$SRC_DIR" --no-deps --ignore-installed --prefix="$PREFIX"
