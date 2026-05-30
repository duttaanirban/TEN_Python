# 1. Maximum of three numbers
def find_max(a, b, c):
    return max(a, b, c)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print("Maximum =", find_max(num1, num2, num3))

# 2. calculator using functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Cannot divide by zero"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+,-,*,/): ")

if op == "+":
    print(add(a, b))
elif op == "-":
    print(subtract(a, b))
elif op == "*":
    print(multiply(a, b))
elif op == "/":
    print(divide(a, b))
    
# 3. Check prime number using functions
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False

    return True

n = int(input("Enter number: "))

if is_prime(n):
    print("Prime Number")
else:
    print("Not Prime")
    
# 4. factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter number: "))
print("Factorial =", factorial(n))

# 5. Fibbonacci using funtions
def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter terms: "))
fibonacci(n)

# 6. student grade system
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

marks = float(input("Enter marks: "))
print("Grade =", calculate_grade(marks))

# 7. event/odd checker using functions
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    return "Odd"

n = int(input("Enter number: "))
print(check_even_odd(n))

#8. tmperature converter using functions
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

choice = input("1.C to F  2.F to C : ")

if choice == "1":
    c = float(input("Enter Celsius: "))
    print("Fahrenheit =", celsius_to_fahrenheit(c))

elif choice == "2":
    f = float(input("Enter Fahrenheit: "))
    print("Celsius =", fahrenheit_to_celsius(f))

#9. lambda functions
square = lambda x: x ** 2
cube = lambda x: x ** 3

n = int(input("Enter number: "))

print("Square =", square(n))
print("Cube =", cube(n))

#10. password validation using functions
def validate_password(password):

    if len(password) < 8:
        return False

    has_digit = False

    for ch in password:
        if ch.isdigit():
            has_digit = True

    return has_digit

pwd = input("Enter password: ")

if validate_password(pwd):
    print("Valid Password")
else:
    print("Invalid Password")
    
#11. ATM balance checker using functions
balance = 10000

def check_balance():
    print("Balance =", balance)

check_balance()

#12 Electricity bill calculator using functions
def calculate_bill(units):

    if units <= 100:
        bill = units * 2

    elif units <= 300:
        bill = (100 * 2) + ((units - 100) * 3)

    else:
        bill = (100 * 2) + (200 * 3) + ((units - 300) * 5)

    return bill

units = int(input("Enter units consumed: "))
print("Bill Amount = ₹", calculate_bill(units))

#13. voting eligibility checker using functions
def is_eligible(age):
    return age >= 18

age = int(input("Enter age: "))

if is_eligible(age):
    print("Eligible to Vote")
else:
    print("Not Eligible")

#14. area calculator using functions
def area_circle(r):
    return 3.14 * r * r

def area_rectangle(l, b):
    return l * b

choice = input("1.Circle 2.Rectangle : ")

if choice == "1":
    r = float(input("Radius: "))
    print("Area =", area_circle(r))

elif choice == "2":
    l = float(input("Length: "))
    b = float(input("Breadth: "))
    print("Area =", area_rectangle(l, b))

#15. simple payroll system using functions
def calculate_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    gross = basic + hra + da
    return gross

basic_salary = float(input("Enter Basic Salary: "))

gross_salary = calculate_salary(basic_salary)

print("Gross Salary = ₹", gross_salary)