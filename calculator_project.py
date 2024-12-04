############## (PROJECT 1) SIMPLE CALCULATOR #################

# Function to perform addition
def addition(a, b):
    return a + b

# Function to perform subtraction
def substraction(a, b):
    return a - b

# Function to perform multiplication
def multiplication(a, b):
    return a * b

# Function to perform division, includes error handling for division by zero
def division(a, b):
    if b == 0:
        raise ZeroDivisionError  # Raise error if second number is zero
    return a / b

# Function to perform modulus operation
def modulus(a, b):
    return a % b

# Main function to run the calculator
def main():
    while True:  # Infinite loop to keep calculator running until valid input
        try:
            # Displaying a menu for calculation options
            print("Select operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus")

            # Get the user input for operation choice
            switch = int(input("Enter choice (1/2/3/4/5): "))

            # Check if the input is within the valid range of operations
            if switch < 0 or switch > 5:
                print("Please enter a choice between (1/2/3/4/5)\n")
                continue  # If not, prompt user to re-enter

            else:
                # Prompting user to input the two numbers for the operation
                first_number = float(input("Enter first number: "))
                second_number = float(input("Enter second number: "))

                # Perform the appropriate operation based on the user's choice
                if switch == 1:
                    sum = addition(first_number, second_number)
                    print(f"{first_number} + {second_number} = {sum}")
                    break  # Exit the loop after successful calculation

                elif switch == 2:
                    sub = substraction(first_number, second_number)
                    print(f"{first_number} - {second_number} = {sub}")
                    break

                elif switch == 3:
                    mul = multiplication(first_number, second_number)
                    print(f"{first_number} X {second_number} = {mul}")
                    break

                elif switch == 4:
                    div = division(first_number, second_number)
                    print(f"{first_number} / {second_number} = {div}")
                    break

                elif switch == 5:
                    mod = modulus(first_number, second_number)
                    print(f"\n{first_number} % {second_number} = {mod}\n")
                    break

            break  # End the loop if a valid calculation is performed

        # Handling error in case of division by zero
        except ZeroDivisionError:
            print("Division by zero is impossible!\n")

        # Handling error if the user enters invalid input (non-numeric)
        except ValueError:
            print("Please enter only numbers!\n")

        # Final block that always runs regardless of errors
        finally:
            print("Calculation was successful!\n")

# Running the main function
if __name__ == "__main__":
    main()
