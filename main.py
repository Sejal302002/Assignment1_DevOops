# main.py
from calculator import add, subtract, multiply, divide
from advanced import square_root, power, percentage

def show_menu():
    """Displays the main menu for the calculator."""
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Percentage")
    print("8. Exit")

def main():
    """Main function to run the calculator UI."""
    print("Welcome to the Team Calculator!")
    while True:
        show_menu()
        choice = input("Please enter your choice (1-8): ")

        if choice == '1':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {add(a, b)}")
        elif choice == '2':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {subtract(a, b)}")
        elif choice == '3':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {multiply(a, b)}")
        elif choice == '4':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {divide(a, b)}")
        elif choice == '5':
            a = float(input("Enter the number: "))
            print(f"Result: {square_root(a)}")
        elif choice == '6':
            base = float(input("Enter the base: "))
            exp = float(input("Enter the exponent: "))
            print(f"Result: {power(base, exp)}")
        elif choice == '7':
            num = float(input("Enter the number: "))
            percent = float(input("Enter the percentage: "))
            print(f"Result: {percentage(num, percent)}")
        elif choice == '8':
            print("Thank you for using the calculator!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()