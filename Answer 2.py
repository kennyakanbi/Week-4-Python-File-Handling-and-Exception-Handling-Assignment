def read_file():
    # Ask the user for the filename
    filename = input("Enter the filename to read: ")
    
    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile Content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    
    except IOError:
        print(f"Error: The file '{filename}' cannot be read.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_file()