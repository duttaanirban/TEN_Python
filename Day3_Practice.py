# 1. Number printing patterns
n = int(input("Enter rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 2. Multiplication Table
num = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
    
# 3. Even or Odd
num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 4. Sum of N numbers
n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)

# 5. Prime Numbers check
num = int(input("Enter number: "))

if num < 2:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

# 6. Factorial of a number
n = int(input("Enter number: "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)

# 7. Fibonacci Series
n = int(input("How many terms? "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
    
# 8. Reverse a number
num = int(input("Enter number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed Number =", reverse)


# 9. Password Check with limited attempts
correct_password = "admin123"

for attempt in range(3):
    password = input("Enter password: ")

    if password == correct_password:
        print("Login Successful")
        break
else:
    print("Account Locked")
    

# 10. Simple Banking System
balance = 10000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance =", balance)
    elif choice == 2:
        amount = float(input("Enter amount: "))
        balance += amount
        print("Deposit Successful")
    elif choice == 3:
        amount = float(input("Enter amount: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")
    elif choice == 4:
        print("Thank You")
        break
    else:
        print("Invalid Choice")