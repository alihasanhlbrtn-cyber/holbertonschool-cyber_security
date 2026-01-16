#!/bin/bash
curl -s -X POST -H "Host: $NEW_HOST" -d "$FORM_DATA" "$TARGET_URL"
