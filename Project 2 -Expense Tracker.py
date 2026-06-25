expenses = []
total_spent = 0

while True:
    print("\n========= Expense Tracker =========")
    print("1. Add expense")
    print("2. View total spent")
    print("3. View all expenses")
    print("4. Exit")
    user_choice = input("Enter your choice: ")
    if user_choice == "1":
        amount = float(input("Enter the amount you want to add: "))
        expenses.append(amount)
        total_spent = total_spent + amount
        print("Expense saved successfully.")
    elif user_choice == "2":
        print("Total amount spent:", total_spent)
    elif user_choice == "3":
        if len(expenses) == 0:
            print("No expenses added.")
        else:
            print("\nExpenses entered:")

            count = 1
            for expense in expenses:
                print(count, "-", expense)
                count = count + 1
    elif user_choice == "4":
        print("Thank you for using this program")
        break
    else:
        print("Please enter a valid choice.")




