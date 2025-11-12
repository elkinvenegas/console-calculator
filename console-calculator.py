

print("🧮 Your Console Calculator")

while True:
    try:
        number_1 = float(input("Enter the first number:  "))
        number_2 = float(input("Enter the second number: "))
        
    except ValueError:
        print("Please enter valid numbers")
        continue

    print("Available operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    option = input("Now, choose an option from 1 to 4: ")

    if option == "1":
        result = number_1 + number_2
        print(f"The result of the addition is: {result:.2f}")
    elif option == "2":
        result = number_1 - number_2
        print(f"The result of the substraction is: {result:.2f}")
    elif option == "3":
        result = number_1 * number_2
        print(f"The result of the multiplication is: {result:.2f}")
    elif option == "4":
        if number_2 !=0:
            result = number_1 / number_2
            print(f"The result of the division is: {result:.2f}")
        else:
            print("You cannot divide by zero")
    else:
        print("Invalid option")

    again = input("Do you want to do another calculation? (y/n): " ).lower()
    if again != "y":
        print("Ok. Good bye!")
        break
