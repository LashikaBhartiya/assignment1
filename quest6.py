# Program to read and print the content of a text file

# Specify the path to the text file
file_path = 'example.txt'

# Open the file in read mode and print its content
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file at path '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
