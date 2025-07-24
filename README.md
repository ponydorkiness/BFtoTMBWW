# Brainfuck to Turing Machine But Way Worse compiler 

This program converts Brainfuck code into the esoteric programming language "Turing Machine But Way Worse".  

## How to Use

1. Run `auto.bat`.
2. Paste your Brainfuck program when prompted.

**Important:**  
Before using this tool, make sure to minify your Brainfuck code using:  
https://mothereff.in/brainfuck-minifier  
This removes any newlines or invalid characters.

## Notes

This interpreter runs on a slightly modified version of Brainfuck:
- The only allowed input is a single digit `0-9`.
- That digit will be stored directly into **cell 0** of memory.

Example: If you input `5`, it will store the value `5` in the 0th cell.
