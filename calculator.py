import pyjokes

off = "O"
print("Hello! Please, choose an option: ")
func = input(
    'type "J" to hear a joke, "C" to use the calculator or "O" to switch it Off: '
).upper()
if func in off:
    exit()
elif func in ["J", "C", "O"]:
    while True:
        while func == "J":
            print(pyjokes.get_joke("en"))
            print()

            func = input(
                '2) type "J" to hear a joke, "C" to use the calculator or "O" to switch it Off: '
            ).upper()
            if func == "C":
                continue
            elif func in off:
                print("Goodbye!")
                exit()

        while func == "C":
            x, operation, y = input(
                'type a first number, an operator ( +  -  *  / ), a second number and finally press "Enter": '
            )
            if operation == "+":
                print(float(x) + float(y))
            elif operation == "-":
                print(float(x) - float(y))
            elif operation == "*":
                print(float(x) * float(y))
            elif operation == "/":
                try:
                    print(float(x) / float(y))
                except ZeroDivisionError:
                    print("It is not possible dividing a number for zero.")
            else:
                print("Please, type only numbers and an operation without any space:")
            print()

            func = input(
                '3) type "J" to hear a joke, "C" to use the calculator or "O" to switch it Off: '
            ).upper()
            if func == "J":
                continue
            elif func in off:
                print("Goodbye!")
                exit()
else:
    print(
        'Your option is not valid: please, next time choose only among "J" "C" or "O".'
    )
