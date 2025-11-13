# calculator.py
# Created by: Shah-zaib Aly

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = num1 + num2
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == '4':
                if num2 != 0:
                    result = num1 / num2
                    print(f"Result: {num1} / {num2} = {result}")
                else:
                    print("Error: Cannot divide by zero.")
            break
        else:
            print("Invalid input, please choose 1, 2, 3, or 4.")

calculator()