#!/bin/bash
cat /var/log/auth.log | cut -d' ' -f6- | sort | uniq -c | sort -nr
