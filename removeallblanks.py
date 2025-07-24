def remove_blank_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    non_blank_lines = [line for line in lines if line.strip() != '']

    with open(filename, 'w') as f:
        f.writelines(non_blank_lines)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        remove_blank_lines(sys.argv[1])
