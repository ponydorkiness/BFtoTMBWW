#!/usr/bin/env python3
import sys

def remap_fields(in_path, out_path):
    mapping = {}
    next_id = 0

    with open(in_path, 'r') as infile, open(out_path, 'w') as outfile:
        for line in infile:
            parts = line.rstrip('\n').split()
            # ensure there are at least 5 fields
            if len(parts) < 5:
                outfile.write(line)
                continue

            for idx in (1, 4):  # 2nd and 5th fields
                key = parts[idx]
                if key not in mapping:
                    mapping[key] = str(next_id)
                    next_id += 1
                parts[idx] = mapping[key]

            outfile.write(' '.join(parts) + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} INPUT_FILE OUTPUT_FILE")
        sys.exit(1)

    in_file, out_file = sys.argv[1], sys.argv[2]
    remap_fields(in_file, out_file)
