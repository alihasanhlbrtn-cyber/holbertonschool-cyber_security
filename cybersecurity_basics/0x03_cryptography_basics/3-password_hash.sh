#!/bin/bash
echo -n "$(openssl rand -base64 12)$1" | openssl dgst -sha512 > 3_hash.txt
