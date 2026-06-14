import os
import shutil

while True:
    print("\n===== Level 4 Menu =====")
    print("1. Organize Files by Type")
    print("2. Generate Student Report")
    print("3. Daily Task List Manager")
    print("4. Analyze Numerical Data")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Task 1: Organize Files
    if choice == "1":
        folder_path = input("Enter folder path: ")

        if os.path.exists(folder_path): 
            for file in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file)

                if os.path.isfile(file_path):
                    extension = file.split(".")[-1]

                    target_folder = os.path.join(folder_path, extension.upper())

                    if not os.path.exists(target_folder):
                        os.mkdir(target_folder)

                    shutil.move(file_path, os.path.join(target_folder, file))

            print("Files Organized Successfully!")
        else:

            
            print("Folder not found!")

    # Task 2: Student Report
    elif choice == "2":
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks: "))

        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        else:
            grade = "Fail"

        print("\n----- Student Report -----")
        print("Name :", name)
        print("Marks:", marks)
        print("Grade:", grade)

    # Task 3: Task Manager
    elif choice == "3":
        task = input("Enter Task: ")

        with open("tasks.txt", "a") as file:
            file.write(task + "\n")

        print("Task Saved Successfully!")

        print("\nSaved Tasks:")
        with open("tasks.txt", "r") as file:
            for line in file:
                print("-", line.strip())

    # Task 4: Numerical Data Analysis
    elif choice == "4":
        try:
            with open("numbers.txt", "r") as file:
                numbers = [float(line.strip()) for line in file]

            print("Total:", sum(numbers))
            print("Average:", sum(numbers) / len(numbers))
            print("Maximum:", max(numbers))

        except FileNotFoundError:
            print("numbers.txt file not found!")

    # Exit
    elif choice == "5":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice!")