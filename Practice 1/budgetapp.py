
print("Input total budget")
total_budget = input()
base_budget = total_budget
print("Your Total Budget is " + str(int(total_budget)))
while True:    
    print("What to do")
    print("1. Expenses")
    print("2. Add Savings")
    print("3. Check Balance")

    operation = int(input("What to do: "))

    if operation == 1:
        print("Select Category")
        print("1. Food")
        print("2. Clothing")
        print("3. Entertainment")
        print("4. Additional Expenses")

        category = int(input("Select a category: "))

        if category == 1:
            print("Enter Food expense")
            food_expense = int(input())
            new_budget = (int(str(total_budget)) - food_expense)
            print("New budget " + str(int(new_budget)))
            total_budget = new_budget 
            print(total_budget)
            check = input("Do you want to update again? enter Y to start again or N to end: ")
            if check.upper() == "Y":
                continue
            elif check.upper() == "N":
                print("Bye...")
                break

        if category == 2:
            print("Enter Clothing expense")
            clothing_expense = int(input())
            new_budget = (int(str(total_budget)) - clothing_expense)
            print("New budget " + str(int(new_budget)))
            total_budget = new_budget 
            print(total_budget)
            check = input("Do you want to update again? enter Y to start again or N to end: ")
            if check.upper() == "Y":
                continue
            elif check.upper() == "N":
                print("Bye...")
                break
        if category == 3:
            print("Enter Entertainment expense")
            entertainment_expense = int(input())
            new_budget = (int(str(total_budget)) - entertainment_expense)
            print("New budget " + str(int(new_budget)))
            total_budget = new_budget 
            print(total_budget)
            check = input("Do you want to update again? enter Y to start again or N to end: ")
            if check.upper() == "Y":
                continue
            elif check.upper() == "N":
                print("Bye...")
                break
        if category == 4:  
            print("Enter Additional expense")
            addtl_expense = int(input())
            new_budget = (int(str(total_budget)) - addtl_expense)
            print("New budget " + str(int(new_budget)))
            total_budget = new_budget 
            print(total_budget)
            check = input("Do you want to update again? enter Y to start again or N to end: ")
            if check.upper() == "Y":
                continue
            elif check.upper() == "N":
                print("Bye...")
                break

    if operation == 2:
        print("How much will be deposited")
        deposit = int(input())
        new_budget = (int(str(total_budget)) + deposit)
        print("New budget " + str(int(new_budget)))
        total_budget = new_budget 
        print(total_budget)
    if operation == 3:
        print("Your old budget is " + str(base_budget))
        print("Your new budget is " + str(int(total_budget)))
    