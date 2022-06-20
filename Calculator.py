import math
while True:
    print("Select an operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Sq. Root")
    print("6. Power")

    operation = int(input("Operation to be used: "))

    if operation == 1:
        num1 = input("Input a number: ")
        num2 = input("Input a second number: ")
        print(int(num1) + int(num2))

    elif operation == 2:
        num1 = input("Input a number: ")
        num2 = input("Input a second number: ")
        print(int(num1) - int(num2))

    elif operation == 3:
        num1 = input("Input a number: ")
        num2 = input("Input a second number: ")
        print(int(num1) * int(num2))
 
    elif operation == 4:
        num1 = input("Input a number: ")
        num2 = input("Input a second number: ")
        print(int(num1) / int(num2))

    elif operation == 5:
        num1 = int(input("Input a number: "))
        print(math.sqrt(num1)) 
 
    elif operation == 6:
        num1 = int(input("Input a base number: "))
        num2 = int(input("Input a exponent number: "))
        print(pow(num1, num2))

    elif operation >= 7:
        print("Operation does not exist") 


    check = input("Do you want to quit or start again? enter Y to restart or N to end: ")
    if check.upper() == "Y":
        continue
    elif check.upper() == "N":
        print("Bye...")
        break
   



