Tasks = []
while True:

    print("\n==========To-Do List==========")
    print("1. Add tasks")
    print("2. View tasks ")
    print("3. Exit ")

    user_choice = input("Enter your choice:")
    if user_choice == "1":
        task = input("Enter a task: ")
        if task.strip() == "":
            print("Task cannot be empty!")
        else:
            Tasks.append(task)
            print("Task added!")
    elif user_choice == "2":
        if len(Tasks) == 0:
            print("No tasks added!")
        else:
            print("\nYour Tasks:")
            count = 1
            for task in Tasks:
                print(count, "-", task)
                count = count + 1
    elif user_choice == "3":
        print("Thank you for using this  program")
        break

    else:
        print("Please enter a valid choice")
