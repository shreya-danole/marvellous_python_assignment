def remove_blank_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.strip():  # Skip blank lines
                outfile.write(line)

def main():
    input_file = "input.txt"
    output_file = "cleaned_output.txt"
    
    remove_blank_lines(input_file, output_file)
    print(f"Blank lines removed. Cleaned content saved in '{output_file}'.")

if __name__ == "__main__":
    main()
