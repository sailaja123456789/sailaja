add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b if b != 0 else "Error: Div by 0 is not allowed"

result = 0
print('Simple calculator')

while True:
    if result == 0:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    else:
        num1 = result

    print("Select an operation:")
    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    print("5. Use the current result for further calculations")
    print("6. Quit")

    choice = input("Enter your choice (1-6): ")

    if choice != '5':
      result = 0

    if choice == '6':
        break

    if choice not in ('1', '2', '3', '4', '5', '6'):
        print("Invalid choice. Please select a valid operation.")
        continue

    if choice == '5':
      num2 = float(input("Enter the next number: "))
      continue

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = sub(num1, num2)
    elif choice == '3':
        result = mul(num1, num2)
    elif choice == '4':
        result = div(num1, num2)

    print("Result:", result)
