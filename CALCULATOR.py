def simple_calculator():
    print("\nWelcome to calculator!\n")
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
  
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    choice = int(input("\nEnter the number corresponding to the operation (1/2/3/4/5): "))
    
    if choice == 1 :
        result = number1 + number2
        print(f"The result of {number1} + {number2} = {result}")
    elif choice == 2 :
        result = number1 - number2
        print(f"The result of {number1} - {number2} = {result}")
    elif choice == 3 :
        result = number1 * number2
        print(f"The result of {number1} * {number2} = {result}")
    elif choice ==  4 :
        if number2 != 0:
            result = number1 / number2
            print(f"The result of {number1} / {number2} = {format(result,".2f")}")
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == 5:
        result = number1 % number2
        print(f"The result of {number1} % {number2} is {result}")
    else:
        print("Invalid operation choice. Please choose a valid operation.")


simple_calculator()
print("\nThank You For Using Calculator!\n")