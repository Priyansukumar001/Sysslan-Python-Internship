# Predefined 3x3 grid
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Task 1: Display the grid
print("3x3 Number Grid:")
for row in grid:
    for num in row:
        print(num, end=" ")
    print()

# Task 2: Check whether a number exists in the grid
search_num = int(input("\nEnter a number to search: "))

found = False
for row in grid:
    if search_num in row:
        found = True
        break

if found:
    print(f"{search_num} exists in the grid.")
else:
    print(f"{search_num} does not exist in the grid.")

# Task 3: Calculate and display the sum of each row
print("\nSum of each row:")
for i, row in enumerate(grid):
    print(f"Row {i+1}: {sum(row)}")

# Task 4: Verify whether all numbers are unique
all_numbers = []

for row in grid:
    all_numbers.extend(row)

if len(all_numbers) == len(set(all_numbers)):
    print("\nAll numbers in the grid are unique.")
else:
    print("\nDuplicate numbers found in the grid.")