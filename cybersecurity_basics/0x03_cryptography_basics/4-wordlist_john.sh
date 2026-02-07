#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: ./4-wordlist_john.sh <hash_file>"
    exit 1
fi


john --wordlist=/usr/share/wordlists/rockyou.txt --format=Raw-MD5 "$1"
