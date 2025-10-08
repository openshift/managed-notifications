#!/bin/bash

# Run this script to validate all managed-notifications are configured with a severity
while IFS= read -r -d '' file
do
  if ! jq .severity -e < "$file" > /dev/null 2>&1; then
    echo "file $file is missing a 'severity' value!"
    exit 1
  fi

  # This is a pretty rough check, ideally we move this repo to a json schema validation in the future
  if ! jq -e '.severity == "Debug" or .severity == "Info" or .severity == "Warning" or .severity == "Major" or .severity == "Critical"'  < "$file" > /dev/null 2>&1; then
    echo "file $file has invalid 'severity' value! must be one of 'Debug', 'Info', 'Warning', 'Major', 'Critical'"
    exit 1
  fi
done < <(find . -type f -name "*.json" -not -path "./mcp/*" -print0)

echo "pass!"
