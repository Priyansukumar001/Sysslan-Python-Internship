
import os
import csv
import shutil
import requests
from bs4 import BeautifulSoup
from datetime import datetime

while True:
    print("\n===== LEVEL 5 MENU =====")
    print("1. Web Scraping using BeautifulSoup")
    print("2. Read CSV Data")
    print("3. Create Folder Backup")
    print("4. Personal Utility Tool")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Task 1: Web Scraping
    if choice == "1":
        url = input("Enter Website URL: ")

        try:
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")

                print("\nPage Title:")
                print(soup.title.text)

                print("\nHeadings Found:")
                for heading in soup.find_all(["h1", "h2", "h3"]):
                    print("-", heading.text.strip())
            else:
                print("Failed to fetch webpage.")

        except Exception as e:
            print("Error:", e)

    # Task 2: Read CSV File
    elif choice == "2":
        file_name = input("Enter CSV File Name: ")

        try:
            with open(file_name, "r", newline="") as file:
                reader = csv.reader(file)

                print("\nCSV Data:")
                for row in reader:
                    print(" | ".join(row))

        except FileNotFoundError:
            print("CSV file not found!")

    # Task 3: Backup Folder
    elif choice == "3":
        source_folder = input("Enter Folder Path: ")

        if os.path.exists(source_folder):

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            backup_folder = source_folder + "_backup_" + timestamp

            shutil.copytree(source_folder, backup_folder)

            print("Backup Created Successfully!")
            print("Backup Folder:", backup_folder)

        else:
            print("Folder not found!")

    # Task 4: Personal Utility Tool
    elif choice == "4":

        while True:
            print("\n===== PERSONAL UTILITY TOOL =====")
            print("1. Save Note")
            print("2. View Notes")
            print("3. Delete Notes")
            print("4. Back to Main Menu")

            sub_choice = input("Enter choice: ")

            if sub_choice == "1":
                note = input("Enter Note: ")

                with open("notes.txt", "a") as file:
                    file.write(note + "\n")

                print("Note Saved Successfully!")

            elif sub_choice == "2":

                if os.path.exists("notes.txt"):

                    with open("notes.txt", "r") as file:
                        print("\nSaved Notes:")
                        print(file.read())

                else:
                    print("No Notes Found!")

            elif sub_choice == "3":

                if os.path.exists("notes.txt"):
                    os.remove("notes.txt")
                    print("Notes Deleted Successfully!")
                else:
                    print("No Notes Found!")

            elif sub_choice == "4":
                break

            else:
                print("Invalid Choice!")

    # Exit Program
    elif choice == "5":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice!")
