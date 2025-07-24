import sys
import re

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_file> <output_file>")
        return

    infile, outfile = sys.argv[1], sys.argv[2]

    cond_pattern = re.compile(r'^\s*\d+\s+cond\s+(?:right|left)\b', re.IGNORECASE)
    word_pattern = re.compile(r'\b(?:plus|minus|left|right|print|start|terminate)\b', re.IGNORECASE)

    with open(infile, 'r') as fin, open(outfile, 'w') as fout:
        for line in fin:
            if not line.strip():
                continue  # Remove real blank lines entirely

            if cond_pattern.search(line) or word_pattern.search(line):
                fout.write('\n')  # Replace matching lines with a blank line
            else:
                fout.write(line)  # Keep the line as-is

if __name__ == '__main__':
    main()
