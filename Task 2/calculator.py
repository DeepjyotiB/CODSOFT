# task 2
print("Simple Calculator")
print("Operations: +, -, *, /")


first = float(input("First number: "))
operator = input("Operation (+, -, *, /): ")
second = float(input("Second number: "))

# Perform calculation
if operator == '+':
    print("Result:", first + second)
elif operator == '-':
    print("Result:", first - second)
elif operator == '*':
    print("Result:", first * second)
elif operator == '/':
    if second != 0:
        print("Result:", first / second)
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operation. Please use +, -, *, or /.")
