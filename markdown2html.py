#!/usr/bin/python3
"""
convert markdown to html
"""

import sys
import os

def main():
    """
    Main function to handle the conversion of a
    Markdown file to HTML.

    This function checks if the correct number
    of arguments are provided, 
    verifies the existence of the Markdown file, and
    handles errors appropriately.
    
    Arguments:
    - None: Arguments are read from sys.argv.
    
    Exits with:
    - Code 1 if the number of arguments is incorrect
    or the file does not exist.
    - Code 0 if everything is correct.
    """
    
    # Check if exactly 2 arguments are provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

# Extract arguments
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Check if the Markdown file exists
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)
    
    # If everything is correct, exit with code 0
    sys.exit(0)

if __name__ == "__main__":
    main()
