awk -F'\t' '{print $2}' "$input_file" | sort -u > "$output_file"
