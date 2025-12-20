#!/bin/bash
head -c 500 /dev/urandom | tr -dc '[:alnum:]' | head -c "$1"; echo ""
