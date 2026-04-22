#!/bin/bash
nmap --script http-vuln-cve2017-5638,ssl-enum-ciphers,ftp-anon -p 21,22,80,443 $1 -oN comprehensive_scan_results.txt
