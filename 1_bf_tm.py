def main():
    # Multiline blocks
    right_block = """right
0 0 0 1 a2 0 0
1 0 1 1 a2 0 0
0 a2 0 1 a3 0 0
1 a2 1 1 a3 0 0
0 a3 0 1 a4 0 0
1 a3 1 1 a4 0 0
0 a4 0 1 a5 0 0
1 a4 1 1 a5 0 0
0 a5 0 1 a6 0 0
1 a5 1 1 a6 0 0
0 a6 0 1 a7 0 0
1 a6 1 1 a7 0 0
0 a7 0 1 a8 0 0
1 a7 1 1 a8 0 0
0 a8 0 1 b9 0 0
1 a8 1 1 b9 0 0
0 b9 0 1 b2 0 0
1 b9 1 1 b2 0 0
0 b2 0 1 b3 0 0
1 b2 1 1 b3 0 0
0 b3 0 1 b4 0 0
1 b3 1 1 b4 0 0
0 b4 0 1 b5 0 0
1 b4 1 1 b5 0 0
0 b5 0 1 b6 0 0
1 b5 1 1 b6 0 0
0 b6 0 1 b7 0 0
1 b6 1 1 b7 0 0
0 b7 0 1 b8 0 0
1 b7 1 1 b8 0 0
0 b8 0 1 c9 0 0
1 b8 1 1 c9 0 0"""

    left_block = """left
0 0 0 0 aa2 0 0
1 0 1 0 aa2 0 0
0 aa2 0 0 aa3 0 0
1 aa2 1 0 aa3 0 0
0 aa3 0 0 aa4 0 0
1 aa3 1 0 aa4 0 0
0 aa4 0 0 aa5 0 0
1 aa4 1 0 aa5 0 0
0 aa5 0 0 aa6 0 0
1 aa5 1 0 aa6 0 0
0 aa6 0 0 aa7 0 0
1 aa6 1 0 aa7 0 0
0 aa7 0 0 aa8 0 0
1 aa7 1 0 aa8 0 0
0 aa8 0 0 ba9 0 0
1 aa8 1 0 ba9 0 0
0 ba9 0 0 ba2 0 0
1 ba9 1 0 ba2 0 0
0 ba2 0 0 ba3 0 0
1 ba2 1 0 ba3 0 0
0 ba3 0 0 ba4 0 0
1 ba3 1 0 ba4 0 0
0 ba4 0 0 ba5 0 0
1 ba4 1 0 ba5 0 0
0 ba5 0 0 ba6 0 0
1 ba5 1 0 ba6 0 0
0 ba6 0 0 ba7 0 0
1 ba6 1 0 ba7 0 0
0 ba7 0 0 ba8 0 0
1 ba7 1 0 ba8 0 0
0 ba8 0 0 ca9 0 0
1 ba8 1 0 ca9 0 0"""

    plus_block = """plus
1 0 0 0 9 0 0
0 0 1 0 a 0 0
1 9 0 0 10 0 0
0 9 1 0 b 0 0
1 10 0 0 11 0 0
0 10 1 0 c 0 0
1 11 0 0 12 0 0
0 11 1 0 d 0 0
1 12 0 0 13 0 0
0 12 1 0 e 0 0
1 13 0 0 14 0 0
0 13 1 0 f 0 0
1 14 0 0 15 0 0
0 14 1 0 g 0 0
0 15 1 1 f 0 0
1 15 0 1 f 0 0
0 g 0 1 f 0 0
1 g 1 1 f 0 0
0 f 0 1 e 0 0
1 f 1 1 e 0 0
0 e 0 1 d 0 0
1 e 1 1 d 0 0
0 d 0 1 c 0 0
1 d 1 1 c 0 0
0 c 0 1 b 0 0
1 c 1 1 b 0 0
0 b 0 1 a 0 0
1 b 1 1 a 0 0
0 a 0 1 z 0 0
1 a 1 1 z 0 0"""

    minus_block = """minus
1 0 0 0 a 0 0
0 0 1 0 9 0 0
1 9 0 0 b 0 0
0 9 1 0 10 0 0
1 10 0 0 c 0 0
0 10 1 0 11 0 0
1 11 0 0 d 0 0
0 11 1 0 12 0 0
1 12 0 0 e 0 0
0 12 1 0 13 0 0
1 13 0 0 f 0 0
0 13 1 0 14 0 0
1 14 0 0 g 0 0
0 14 1 0 15 0 0
0 15 1 1 f 0 0
1 15 0 1 f 0 0
0 g 0 1 f 0 0
1 g 1 1 f 0 0
0 f 0 1 e 0 0
1 f 1 1 e 0 0
0 e 0 1 d 0 0
1 e 1 1 d 0 0
0 d 0 1 c 0 0
1 d 1 1 c 0 0
0 c 0 1 b 0 0
1 c 1 1 b 0 0
0 b 0 1 a 0 0
1 b 1 1 a 0 0
0 a 0 1 z 0 0
1 a 1 1 z 0 0"""

    cond_leftjump = """cond left
0 0 0 1 k2 0 0
1 0 1 1 k2 0 0
0 k2 0 0 k3 0 0
1 k2 0 0 k3 0 0
1 k3 1 0 a 0 0
0 k3 0 0 9 0 0
1 9 1 0 b 0 0
0 9 0 0 10 0 0
1 10 1 0 c 0 0
0 10 0 0 11 0 0
1 11 1 0 d 0 0
0 11 0 0 12 0 0
1 12 1 0 e 0 0
0 12 0 0 13 0 0
1 13 1 0 f 0 0
0 13 0 0 14 0 0
1 14 1 0 g 0 0
0 14 0 0 15a 0 0
1 15a 1 0 h 0 0
0 15a 0 0 15z 0 0
0 h 0 1 g 0 0
1 h 1 1 g 0 0
0 g 0 1 f 0 0
1 g 1 1 f 0 0
0 f 0 1 e 0 0
1 f 1 1 e 0 0
0 e 0 1 d 0 0
1 e 1 1 d 0 0
0 d 0 1 c 0 0
1 d 1 1 c 0 0
0 c 0 1 b 0 0
1 c 1 1 b 0 0
0 b 0 1 a 0 0
1 b 1 1 a 0 0
0 a 0 1 z 0 0
1 a 1 1 z 0 0
0 15z 0 1 15 0 0
1 15z 1 1 15 0 0
0 15 0 1 2a 0 0
1 15 1 1 2a 0 0
0 2a 0 1 3a 0 0
1 2a 1 1 3a 0 0
0 3a 0 1 4a 0 0
1 3a 1 1 4a 0 0
0 4a 0 1 5a 0 0
1 4a 1 1 5a 0 0
0 5a 0 1 6a 0 0
1 5a 1 1 6a 0 0
0 6a 0 1 7a 0 0
1 6a 1 1 7a 0 0
0 7a 0 1 8a 0 0
1 7a 1 1 8a 0 0
0 8a 0 1 9a 0 0
1 8a 1 1 9a 0 0
0 9a 1 0 z 0 0
1 9a 1 0 z 0 0
0 z 0 1 10a 0 0
1 z 1 1 10a 0 0
0 10a 0 0 countine 0 0
1 10a 1 0 jump 0 0"""
    cond_rightjump = """cond right
0 0 0 1 k2 0 0
1 0 1 1 k2 0 0
0 k2 0 0 k3 0 0
1 k2 0 0 k3 0 0
1 k3 1 0 a 0 0
0 k3 0 0 9 0 0
1 9 1 0 b 0 0
0 9 0 0 10 0 0
1 10 1 0 c 0 0
0 10 0 0 11 0 0
1 11 1 0 d 0 0
0 11 0 0 12 0 0
1 12 1 0 e 0 0
0 12 0 0 13 0 0
1 13 1 0 f 0 0
0 13 0 0 14 0 0
1 14 1 0 g 0 0
0 14 0 0 15a 0 0
1 15a 1 0 h 0 0
0 15a 0 0 15z 0 0
0 h 0 1 g 0 0
1 h 1 1 g 0 0
0 g 0 1 f 0 0
1 g 1 1 f 0 0
0 f 0 1 e 0 0
1 f 1 1 e 0 0
0 e 0 1 d 0 0
1 e 1 1 d 0 0
0 d 0 1 c 0 0
1 d 1 1 c 0 0
0 c 0 1 b 0 0
1 c 1 1 b 0 0
0 b 0 1 a 0 0
1 b 1 1 a 0 0
0 a 0 1 z 0 0
1 a 1 1 z 0 0
0 15z 0 1 15 0 0
1 15z 1 1 15 0 0
0 15 0 1 2a 0 0
1 15 1 1 2a 0 0
0 2a 0 1 3a 0 0
1 2a 1 1 3a 0 0
0 3a 0 1 4a 0 0
1 3a 1 1 4a 0 0
0 4a 0 1 5a 0 0
1 4a 1 1 5a 0 0
0 5a 0 1 6a 0 0
1 5a 1 1 6a 0 0
0 6a 0 1 7a 0 0
1 6a 1 1 7a 0 0
0 7a 0 1 8a 0 0
1 7a 1 1 8a 0 0
0 8a 0 1 9a 0 0
1 8a 1 1 9a 0 0
0 9a 1 0 z 0 0
1 9a 1 0 z 0 0
0 z 0 1 10a 0 0
1 z 1 1 10a 0 0
0 10a 0 0 countine 0 0
1 10a 1 0 jump 0 0
"""

    start_block = """start
0 0 0 1 2 0 0
1 0 0 1 2 0 0
0 2 0 1 3 0 0
1 2 0 1 3 0 0
0 3 0 1 4 0 0
1 3 0 1 4 0 0
0 4 0 1 5 0 0
1 4 0 1 5 0 0
0 5 0 1 6 0 0
1 5 1 1 6 0 0
0 6 0 1 7 0 0
1 6 1 1 7 0 0
0 7 0 1 8 0 0
1 7 1 1 8 0 0
"""

    print_block = """print
0 0 0 0 B 1 0
1 0 1 0 B 1 0
0 B 0 1 C 0 0
1 B 1 1 C 0 0
"""

    terminate_block = """terminate
0 0 0 0 B 0 1
1 0 1 0 B 0 1
"""
    # Map characters to blocks
    mapping = {
        '>': right_block,
        '<': left_block,
        '+': plus_block,
        '-': minus_block,
        '[': cond_leftjump,
        ']': cond_rightjump,
        '.': print_block
    }

    # Read user input string
    input_string = input("Enter characters (like ++--[]): ").strip()
    valid_chars = set('[]+-<>.')
    input_string = ''.join(c for c in input_string if c in valid_chars)

    # First pass: find matching bracket pairs and assign each pair an index
    stack = []
    bracket_indices = {}  # position -> bracket pair index
    pair_counter = 0

    for pos, ch in enumerate(input_string):
        if ch == '[':
            pair_counter += 1
            stack.append(pair_counter)
            bracket_indices[pos] = pair_counter
        elif ch == ']':
            if not stack:
                raise ValueError(f"Unmatched ']' at position {pos}")
            idx = stack.pop()
            bracket_indices[pos] = idx

    if stack:
        raise ValueError("Unmatched '[' in input")

    # Write corresponding blocks to the file, prefixing cond blocks with their pair index
    with open("output.txt", "w") as f:
        f.write(start_block + "\n\n")
        for pos, char in enumerate(input_string):
            block = mapping.get(char)
            if block is None:
                f.write(f"# Unknown character: {char}\n")
                continue

            if char in '[]':
                idx = bracket_indices[pos]
                lines = block.splitlines()
                # Prepend the index to the first line (e.g. "cond left" -> "1 cond left")
                lines[0] = f"{idx} {lines[0]}"
                f.write("\n".join(lines) + "\n\n")
            else:
                f.write(block + "\n\n")
        f.write(terminate_block + "\n\n")

if __name__ == "__main__":
    main()
