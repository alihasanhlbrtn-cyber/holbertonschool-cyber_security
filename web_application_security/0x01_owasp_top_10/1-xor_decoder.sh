#!/bin/bash
# WebSphere XOR decoder

hash="$1"
clean="${hash#\{xor\}}"

python3 - <<EOF
import base64, sys

data = base64.b64decode("$clean")
out = bytes([b ^ 0x5F for b in data])
sys.stdout.write(out.decode())
EOF
