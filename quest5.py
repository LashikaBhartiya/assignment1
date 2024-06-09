# Program to take a string input from the user and write it to a text file

# Prompt the user for input
user_input = input("Please enter the text you want to write to the file: ")

# Specify the file name
file_name = "output.txt"

# Open the file in write mode
with open(file_name, "w") as file:
    # Write the user input to the file
    file.write(user_input)

# Notify the user that the text has been written to the file
print(f"The text has been written to {file_name}")
