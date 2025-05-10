#!/bin/bash
URL="https://www.amfiindia.com/spages/NAVAll.txt"
TEMP_FILE="NAVAll.txt"
OUTPUT_TSV_FILE="scheme_nav_data.tsv"

echo "Downloading NAV data from $URL..."
wget -q -O "$TEMP_FILE" "$URL"

if [ ! -s "$TEMP_FILE" ]; then
    echo "Error: Failed to download or file is empty."
    exit 1
fi

echo -e "Scheme Name\tNet Asset Value" > "$OUTPUT_TSV_FILE"

awk -F';' '
BEGIN { OFS="\t" }
NR > 1 && NF == 6 {
    scheme_name = $4;
    nav = $5;
    gsub(/^[ \t]+|[ \t]+$/, "", scheme_name);
    gsub(/^[ \t]+|[ \t]+$/, "", nav);
    if (length(scheme_name) > 0 || length(nav) > 0) {
        print scheme_name, nav;
    }
}
' "$TEMP_FILE" >> "$OUTPUT_TSV_FILE"

echo "TSV data extracted to $OUTPUT_TSV_FILE"
