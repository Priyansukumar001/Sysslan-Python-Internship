from datetime import datetime

records = []

while True:
    print("\n===== Record Management System =====")
    print("1. Add Record")
    print("2. Save Records to File")
    print("3. Retrieve Records from File")
    print("4. Read File Line by Line")
    print("5. Create Log Entry")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = input("Enter Age: ")

        record = {
            "Name": name,
            "Age": age
        }

        records.append(record)
        print("Record Added Successfully!")

    elif choice == "2":
        with open("records.txt", "w") as file:
            for record in records:
                file.write(f"{record['Name']},{record['Age']}\n")

        print("Records Saved Successfully!")

    elif choice == "3":
        try:
            with open("records.txt", "r") as file:
                print("\nStored Records:")
                for line in file:
                    name, age = line.strip().split(",")
                    print("Name:", name, "| Age:", age)

        except FileNotFoundError:
            print("No records file found!")

    elif choice == "4":
        try:
            with open("records.txt", "r") as file:
                print("\nFile Content:")
                for line in file:
                    print(line.strip())

        except FileNotFoundError:
            print("File not found!")

    elif choice == "5":
        current_time = datetime.now()

        with open("log.txt", "a") as log:
            log.write(f"Log Entry Created at {current_time}\n")

        print("Log Entry Added Successfully!")

    elif choice == "6":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")