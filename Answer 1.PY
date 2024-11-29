# Examole of program that file, modifies its content, and writes 
def read_and_modify_file(input_file_path, output_file_path):
    try:
        # Read the content of the input file
        with open(input_file_path, 'r') as input_file:
            content = input_file.read()
             # Modify the content (for example, convert all text to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        with open(output_file_path, 'w') as output_file:
            output_file.write(modified_content)

        print(f"Modified content has been written to: {output_file_path}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
        # Example usage:
input_file_path = 'input.txt'  # Replace with your input file path
output_file_path = 'output.txt'  # Replace with your desired output file path
read_and_modify_file(input_file_path, output_file_path)