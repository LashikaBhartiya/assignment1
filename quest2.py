# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is an even number."
    else:
        return f"{number} is an odd number."

# Main function
if __name__ == "__main__":
    try:
        # Input from user
        num = int(input("Enter a number: "))
        
        # Check if the number is even or odd
        result = check_even_odd(num)
        
        # Print the result
        print(result)
        
    except ValueError:
        print("Please enter a valid integer.")
