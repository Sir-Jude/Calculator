# Import "sys" for being able to use "argv" and "exit"
import sys
# Import pyjoke for providing the random joke
import pyjokes

# Exit if user provides a python file and the right number of arguments 
if sys.argv[0][-3:] != ".py":
    sys.exit("Not a Python file")
elif len(sys.argv) > 4: # Too many
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 4: # Too few
    sys.exit("Too few command-line arguments")
else:
    # Otherwise try to perform the operation
    try:
        if sys.argv[2] == "+":
            print(int(sys.argv[1]) + int(sys.argv[3]))
        elif sys.argv[2] == "-":
            print(int(sys.argv[1]) - int(sys.argv[3]))
        elif sys.argv[2] == "*":
            print(int(sys.argv[1]) * int(sys.argv[3]))
        elif sys.argv[2] == "/":
            try:
                print(int(sys.argv[1]) / int(sys.argv[3]))
            # Except the error and exit if User try to perform a zero division
            except ZeroDivisionError:
                sys.exit("It is not possible dividing a number for zero.")
    # Except and exit if User do not use numbers and and a mathematical operator
    except ValueError:
        sys.exit("Only numbers and one of the 4 basic mathematical operators (+ - * /) are allowed.")

# Print a random joke
print()
print(pyjokes.get_joke("en"))