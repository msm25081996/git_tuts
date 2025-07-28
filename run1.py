try:
    num = int(input("Enter a number: "))
    for digit in str(num):
        print(f"ASCII value of '{digit}' is {ord(digit)}")
except ValueError:
    print("Invalid input! Please enter a valid number.")