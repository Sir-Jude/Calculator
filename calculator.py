# Import "sys" for being able to use "argv" and "exit"
import sys

# Import pyjoke for providing the random joke
import pyjokes

# Prompt the User for the available options and assign the answer to "func"
func = input(
    'Please, type "J" to hear a joke, "C" to use the calculator or "O" to switch the device off: '
).upper()
print()
# Terminate the programme if User type "O"
if func == "O":
    sys.exit("Goodbye!")
    
# Start a while loop for either of the two other options 
elif func in ["J", "C"]:
    
    # Joke mod
    while func == "J":
        # Print a joke in English
        print(pyjokes.get_joke("en"))
        print()
        # Prompt the User for the available options and assign the answer to "func"
        func = input(
            'Please, type "J" to hear another joke, "C" to use the calculator or "O" to switch the device off: '
        ).upper()
        print()
        # Switch to the calculator mod if User type "C"
        if func == "C":
            continue
        # Terminate the programme if User type "O"
        elif func == "O":
            sys.exit("Goodbye!")

    # Calc mod
    while func == "C":
        # Try to prompt the user for a number
        try:
            x = int(input("Please, type a first number: "))
        # Terminate the programme if Use does not type a number
        except TypeError:
            sys.exit("Only numbers are allowed")
        operator = input("Please, type a kind of operation ( +  -  *  / ): ")
        # Try to prompt the user for a number
        try:
            y = int(input("Please, type a second number: "))
        # Terminate the programme if Use does not type a number
        except TypeError:
            sys.exit("Only numbers are allowed")
        # Perform the desired operation
        if operator == "+":
            print(int(x) + int(y))
        elif operator == "-":
            print(int(x) - int(y))
        elif operator == "*":
            print(int(x) * int(y))
        elif operator == "/":
            # Try to perform the division
            try:
                print(int(x) / int(y))
            # Terminate the programme if the user try to perform a zero division
            except ZeroDivisionError:
                sys.exit("It is not possible dividing a number for zero.")
        else:
            # Terminate the programme if User do not use one of the 4 basic mathematical operators
            sys.exit(
                "Only basic mathematical operators ( +  -  *  / ) are allowed"
            )
        print()
        # Prompt the User for the available options and assign the answer to "func"
        func = input(
            'Please, type "C" to use again the calculator, "J" to hear a joke  or "O" to switch the device Off: '
        ).upper()
        print()
        # Switch to the random joke mod if User type "C"
        if func == "J":
            continue
        # Terminate the programme if User type "O"
        elif func == "O":
            sys.exit("Goodbye!")
# Terminate the programme if User type do not type neither "J" "C" nor "O"
else:
    sys.exit('Your option is not valid: please, next time type only "J" "C" or "O".')
