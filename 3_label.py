import sys

def excel_col_to_num(col):
    num = 0
    for ch in col:
        if 'a' <= ch <= 'z':
            num = num * 26 + (ord(ch) - ord('a') + 1)
        else:
            raise ValueError(f"Invalid column character: {ch}")
    return num

def num_to_excel_col(num):
    col = ''
    while num > 0:
        num -= 1
        num, rem = divmod(num, 26)
        col = chr(rem + ord('a')) + col
    return col

def label_generator(start_label):
    current = excel_col_to_num(start_label)
    while True:
        yield num_to_excel_col(current)
        current += 1

def append_labels_to_line(line, generator, seen):
    parts = line.rstrip('\n').split()
    for idx in (1, 4):
        if idx >= len(parts):
            continue  # skip if not enough fields
        original = parts[idx]
        if original not in seen:
            seen[original] = next(generator)
        parts[idx] = original + seen[original]
    return ' '.join(parts)

def main():
    if len(sys.argv) != 3:
        print("Usage: python append_labels.py input.txt output.txt")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    start_label = 'a'

    gen = label_generator(start_label)
    seen = {}

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if not line.strip():
                seen.clear()
                outfile.write('\n')
                continue
            outfile.write(append_labels_to_line(line, gen, seen) + '\n')

if __name__ == "__main__":
    main()
