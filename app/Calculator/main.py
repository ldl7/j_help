"""

import sys
import os

# Add the parent directory of the 'Calculator' folder to the Python path.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.Operations import addition, subtraction, multiplication, division

from History import add_calculation, clear_history, get_history,undo_last

while True:
        # Prompt the user for input.
        user_input = input("Enter an operation (add, subtract, multiply, divide) and two numbers, or a command: ")

        # Handle the 'exit' command.
        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break

        # Handle the 'History' command.
        elif user_input.lower() == "history":
            print("Calculation History:")
            for calc in get_history():
                print(calc)
            continue

        # Handle the 'clear' command.
        elif user_input.lower() == "clear":
            clear_history()
            print("History cleared.")
            continue

        # Handle the 'undo' command.
        elif user_input.lower() == "undo":
            undo_last()
            print("Last calculation undone.")
            continue

        # Process the input as a calculation.
        else:
            try:
                # Try to split the input into operation and numbers.
                operation, num1, num2 = user_input.split()
                num1, num2 = float(num1), float(num2)
            except ValueError:
                # If the input is not in the correct format, show an error message.
                print("Invalid input. Please follow the format: <operation> <num1> <num2>")
                continue
        
            # Perform the requested operation.
            if operation == "add":
                result = addition(num1, num2)
                print(f"Result: {result}")
            elif operation == "subtract":
                result = subtraction(num1, num2)
                print(result)
            elif operation == "multiply":
                result = multiplication(num1, num2)
                print(result)
            elif operation == "divide":
                try:
                    result = division(num1, num2)
                    print(result)
                except ValueError as e:
                    print(e)
                    continue
            else:
                print(f"Unknown operation '{operation}'. Supported operations: add, subtract, multiply, divide.")
                continue


        result_add = addition(5.0, 3.0)
        result_sub = subtraction(10.0, 4.0)
        result_mul = multiplication(2.0, 3.0)
        result_div = division(10.0, 2.0)

        print(result_add, result_sub, result_mul, result_div)


                

"""