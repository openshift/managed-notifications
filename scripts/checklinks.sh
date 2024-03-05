ARTIFACT_DIR="${ARTIFACT_DIR:-/tmp/artifacts}"
[ ! -d "$ARTIFACT_DIR" ] && mkdir -p "$ARTIFACT_DIR"
TEMP_FILE=$(mktemp -p "$ARTIFACT_DIR" broken_links_XXXXXX)

for file in $(find . -type f -print); do
    grep -shEo "(http|https)://[a-zA-Z0-9./?=_-]*" $file | sort -u | while IFS= read -r URL; do
    cleanurl=${URL%.}
    s=$(curl "$cleanurl" --head --silent --write-out '%{response_code}' -o /dev/null)
    if [[ "$s" == "404" ]]; then
        echo "Path: $file" >> "$TEMP_FILE"
        echo "URL: $URL" >> "$TEMP_FILE"
    fi
    done
done
if [ -s "$TEMP_FILE" ]; then
    echo "Broken links detected:"
    cat "$TEMP_FILE"
    exit 1
else
    echo "No broken links detected."
    exit 0
fi
