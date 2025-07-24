def process_file(input_filename, output_filename):
    """
    Process the input file according to the specified pattern:
    When there's a blank line (excluding the very first blank line), copy the 5th column element
    from 2 lines above the blank line to the 2nd column of the first two lines after the blank line.
    """
    try:
        # Read the input file
        with open(input_filename, 'r') as f:
            lines = f.readlines()
        
        # Strip whitespace and process lines
        processed_lines = [line.rstrip('\n') for line in lines]
        result_lines = []
        seen_first_blank = False
        
        i = 0
        while i < len(processed_lines):
            line = processed_lines[i]
            
            # If it's a blank line
            if line == '':
                # Always append the blank line
                result_lines.append('')
                # Skip processing for the first blank
                if not seen_first_blank:
                    seen_first_blank = True
                    i += 1
                    continue
                
                # For subsequent blanks, perform the copy logic
                source_line_index = i - 2
                element_to_copy = ''
                if source_line_index >= 0:
                    source_elements = processed_lines[source_line_index].split()
                    if len(source_elements) >= 5:
                        element_to_copy = source_elements[4]
                
                # Modify the next two non-blank lines
                j = i + 1
                lines_modified = 0
                while j < len(processed_lines) and lines_modified < 2:
                    next_line = processed_lines[j]
                    if next_line != '':
                        elems = next_line.split()
                        # Replace or append the 2nd element
                        if len(elems) >= 2:
                            elems[1] = element_to_copy
                        elif len(elems) == 1:
                            elems.append(element_to_copy)
                        result_lines.append(' '.join(elems))
                        lines_modified += 1
                    else:
                        result_lines.append('')
                    j += 1
                
                # Advance i past the processed lines
                i = j
            else:
                # Regular line, just add it
                result_lines.append(line)
                i += 1
        
        # Write the output file
        with open(output_filename, 'w') as f:
            for ln in result_lines:
                f.write(ln + '\n')
        
        print(f"Processing complete. Output written to {output_filename}")
    except FileNotFoundError:
        print(f"Error: Could not find input file '{input_filename}'")
    except Exception as e:
        print(f"Error processing file: {e}")

def create_sample_input():
    """Create a sample input file for testing"""
    sample_content = """0 0 0 0 0 0 0
0 0 0 0 0 ac 0
0 0 0 0 0 0 0

0 0 0 0 0 0 0
0 0 0 0 0 0 0"""
    
    with open('input.txt', 'w') as f:
        f.write(sample_content)
    print("Sample input file 'input.txt' created")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        print("Or run without arguments to create a sample input file and process it")
        create_sample_input()
        process_file('input.txt', 'output.txt')
    else:
        process_file(sys.argv[1], sys.argv[2])
