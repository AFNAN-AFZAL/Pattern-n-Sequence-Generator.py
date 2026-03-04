# --- Task 3: Patterns and Sequence Builder ---

def star_triangle(n):
    # Pattern 1: Standard Star Triangle
    for i in range(1, n + 1):
        print("*" * i)

def reverse_star(n):
    # Pattern 2: Reverse Star Triangle
    for i in range(n, 0, -1):
        print("*" * i)

def number_triangle(n):
    # Pattern 3: Number sequence 1, 12, 123...
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

def number_pyramid(n):
    # Pattern 4: Centered Number Pyramid
    for i in range(1, n + 1):
        # 1. Print spaces to center the numbers
        print(" " * (n - i), end="")
        # 2. Print numbers (using odd numbers 1, 3, 5 to make a perfect triangle)
        for j in range(1, (2 * i)):
            print(j, end="")
        print()

# --- Main Program Menu ---
while True:
    print("\n--- PATTERN MENU ---")
    print("1. Star Triangle")
    print("2. Reverse Star")
    print("3. Number Triangle")
    print("4. Number Pyramid")
    print("5. Exit")
    
    choice = input("\nSelect (1-5): ")

    if choice == "5":
        print("Exiting...")
        break

    try:
        size = int(input("Enter pattern size: "))
        if size <= 0:
            print("Please enter a positive number.")
            continue

        if choice == "1":
            star_triangle(size)
        elif choice == "2":
            reverse_star(size)
        elif choice == "3":
            number_triangle(size)
        elif choice == "4":
            number_pyramid(size)
        else:
            print("Invalid selection.")

    except ValueError:
        print("Error: Please enter a whole number.")