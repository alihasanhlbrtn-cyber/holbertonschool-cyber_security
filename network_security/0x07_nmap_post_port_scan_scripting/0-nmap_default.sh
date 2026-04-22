#!/bin/bash


if [ -z "$1" ]; then
    echo "Usage: $0 <target_host>"
    exit 1
fi



sudo nmap -sC "$1"
