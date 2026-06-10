import random
import string

print("Level 2 - Core Python Programs")
print("1. Validate Email Address")
print("2. Generate Random Password")
print("3. Count Characters and Words")
print("4. Generate Fibonacci Sequence")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    email = input("Enter email address: ")

    if "@" in email and "." in email:
        at_pos = email.index("@")
        dot_pos = email.rindex(".")

        if at_pos > 0 and dot_pos > at_pos + 1 and dot_pos < len(email) - 1:
            print("Valid Email Address")
        else:
            print("Invalid Email Address")
    else:
        print("Invalid Email Address")

elif choice == 2:
    length = int(input("Enter password length: "))

    characters = string.ascii_letters + string.digits

    password = ""
    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)

elif choice == 3:
    text = input("Enter a text: ")

    char_count = len(text)
    word_count = len(text.split())

    print("Total Characters:", char_count)
    print("Total Words:", word_count)

elif choice == 4:
    n = int(input("Enter number of terms: "))

    a, b = 0, 1

    print("Fibonacci Sequence:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

else:
    print("Invalid Choice")