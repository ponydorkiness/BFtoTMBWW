import sys

def main(a_path, b_path, c_path):
    with open(a_path) as fa, open(b_path) as fb, open(c_path, 'w') as fc:
        for a_line, b_line in zip(fa, fb):
            fc.write(a_line if not b_line.strip() else b_line)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <file_A> <file_B> <file_C>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
