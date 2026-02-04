#!/bin/bash
salt=$(openssl rand -base64 12)
echo -n "$salt$1" | openssl dgst -sha512 > 3_hash.txt
