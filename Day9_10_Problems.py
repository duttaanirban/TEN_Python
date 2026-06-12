# #DAY1
# #1. sum of two numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# sum = a + b
# print("The sum of", a, "and", b, "is", sum)

# #2. Area of Rectangle
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# area = length * width
# print("The area of the rectangle is:", area)

# #3. Simple Interest
# p = float(input("Enter the principal amount: "))
# r = float(input("Enter the rate of interest: "))
# t = float(input("Enter the time in years: "))
# simple_interest = (p * r * t) / 100
# print("The simple interest is:", simple_interest)

# #4. Celsius to Fahrenheit
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print("The temperature in Fahrenheit is:", fahrenheit)

# #5. salary with HRA and DA
# basic_salary = float(input("Enter the basic salary: "))
# hra = 0.2 * basic_salary  # HRA is 20% of basic salary
# da = 0.1 * basic_salary   # DA is 10% of basic salary
# gross_salary = basic_salary + hra + da
# print("The gross salary is:", gross_salary)

# #DAY2
# #1. positive, negative or zero
# num = float(input("Enter a number: "))
# if num > 0:
#     print("The number is positive.")
# elif num < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")
    
# #2. largest number
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# if num1 > num2:
#     print("The largest number is:", num1)
# else:
#     print("The largest number is:", num2)
    
# #3. largest number among three
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))
# if num1 >= num2 and num1 >= num3:
#     print("The largest number is:", num1)
# elif num2 >= num1 and num2 >= num3:
#     print("The largest number is:", num2)
# else:    
#     print("The largest number is:", num3)
    
# #4. even or odd
# num = int(input("Enter an integer: "))
# if num % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

# #5. leap year
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")
    
# #DAY3
# #1. print 1 to 100
# for i in range(1, 101):
#     print(i, end=' ')
    
# #2. even numbers 1 to 100
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i, end=' ')

# #3. sum of first n natural numbers
# n = int(input("Enter a positive integer: "))
# sum_natural = n * (n + 1) // 2
# print("The sum of the first", n, "natural numbers is:", sum_natural)

# #4. multiplication table
# num = int(input("Enter a number to display its multiplication table: "))
# print("Multiplication table of", num)
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)
    
# #5. factorial of a number
# num = int(input("Enter a non-negative integer: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print("The factorial of", num, "is:", factorial)

# #DAY4
# #1. square of a number
# num = float(input("Enter a number: "))
# square = num ** 2
# print("The square of", num, "is:", square)

# #2. maximum of two numbers
# def max_of_two(a, b):
#     return max(a, b)

# print(max_of_two(5, 10))

# #3. simple interest function
# def simple_interest(principal, rate, time):
#     return (principal * rate * time) / 100

# print(simple_interest(1000, 5, 2))

# #4. even or odd function
# def even_or_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# print(even_or_odd(7))

# #5. area of circle function
# import math
# def area_of_circle(radius):
#     return math.pi * radius ** 2
# print(area_of_circle(5))

# #DAY5
# #1. list of 10 numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in numbers:
#     print(i, end=' ')

# #2. largest number in a list
# numbers = [3, 5, 7, 2, 8]
# largest = max(numbers)
# print("The largest number in the list is:", largest)

#3. sum of elements in a list
# numbers = [1, 2, 3, 4, 5]
# total_sum = 0
# for num in numbers:
#     total_sum += num
# print("The sum of the elements in the list is:", total_sum)

# #4. count even numbers
# numbers = [1, 2, 3, 4, 5, 6]
# even_count = sum(1 for num in numbers if num % 2 == 0)
# print("The count of even numbers in the list is:", even_count)

# #5. remove duplicates from a list
# numbers = [1, 2, 3, 2, 4, 1, 5]
# unique_numbers = list(set(numbers))
# print("The list after removing duplicates is:", unique_numbers)

# #MIXED PROBLEMS
# #1. Reverse a number
# num = int(input("Enter a number: "))
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = (reverse * 10) + digit
#     num //= 10
# print("The reverse of the number is:", reverse)

# #2. plaindrome number
# num = int(input("Enter a number: "))
# original_num = num
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = (reverse * 10) + digit
#     num //= 10
# if original_num == reverse:
#     print(original_num, "is a palindrome number.")
# else:    
#     print(original_num, "is not a palindrome number.")
    
# #3. count digit
# num = int(input("Enter a number: "))
# count = 0
# while num > 0:
#     num //= 10
#     count += 1
# print("The number of digits is:", count)

# #4. sum of digits
# num = int(input("Enter a number: "))
# total_sum = 0
# while num > 0:
#     digit = num % 10
#     total_sum += digit
#     num //= 10
# print("The sum of the digits is:", total_sum)

# #5. fibonacci series
# n = int(input("Enter the number of terms in the Fibonacci series: "))
# a, b = 0, 1
# print("Fibonacci series:")
# for _ in range(n):
#     print(a, end=' ')
#     a, b = b, a + b
    
# #6. prime number
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print(num, "is not a prime number.")
#             break
#     else:
#         print(num, "is a prime number.")
# else:
#     print(num, "is not a prime number.")
    
# #7. prime numbers between 1 and 100
# for num in range(2, 101):
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=' ')

# #8. count vowels
# s = input("Enter a string: ")
# vowels = 'aeiouAEIOU'
# count = sum(1 for char in s if char in vowels)
# print("The number of vowels in the string is:", count)

# #9. reverse a string
# s = input("Enter a string: ")
# reverse = s[::-1]
# print("The reverse of the string is:", reverse)

#10. character frequency
s = input("Enter a string: ")
frequency = {}
for char in s:
    frequency[char] = frequency.get(char, 0) + 1
print("Character frequency in the string:")
for char, freq in frequency.items():
    print(f"'{char}': {freq}")

#FILE HANDLING
#1. create student.txt
f = open("student.txt", "w")

for i in range(3):
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    f.write(f"Name: {name}, Age: {age}\n")
f.close()

#2. read student.txt
f = open("student.txt", "r")
content = f.read()
print(content)
f.close()

#3. count characters
f = open("student.txt", "r")
content = f.read()
char_count = len(content)
print("The number of characters in the file is:", char_count)
f.close()   

#4. count lines
f = open("student.txt", "r")
lines = f.readlines()
line_count = len(lines)
print("The number of lines in the file is:", line_count)
f.close()

#5. count words
f = open("student.txt", "r")
content = f.read()
words = content.split()
word_count = len(words)
print("The number of words in the file is:", word_count)
f.close()

#6. read line by line
f = open("student.txt", "r")

while True:
    line = f.readline()
    if not line:
        break
    print(line, end='')
f.close()

#7. append data
f = open("student.txt", "a")
name = input("Enter student name to append: ")
age = input("Enter student age to append: ")
f.write(f"Name: {name}, Age: {age}\n")
f.close()

#8. search word
f = open("student.txt", "r")
content = f.read()
search_word = input("Enter a word to search: ")
if search_word in content:
    print(f"The word '{search_word}' is found in the file.")
else:
    print(f"The word '{search_word}' is not found in the file.")
f.close()   

#9. count vowels in file
f = open("student.txt", "r")
content = f.read()
vowels = 'aeiouAEIOU'
vowel_count = sum(1 for char in content if char in vowels)
print("The number of vowels in the file is:", vowel_count)
f.close()   

#10. uppercase and lowercase count
f = open("student.txt", "r")
content = f.read()
uppercase_count = sum(1 for char in content if char.isupper())
lowercase_count = sum(1 for char in content if char.islower())
print("The number of uppercase letters in the file is:", uppercase_count)
print("The number of lowercase letters in the file is:", lowercase_count)
f.close()

#11. longest line
f = open("student.txt", "r")
lines = f.readlines()
longest_line = max(lines, key=len)
print("The longest line in the file is:", longest_line)
f.close()

#12. copy file
with open("student.txt", "r") as source_file:
    content = source_file.read()
with open("student_copy.txt", "w") as dest_file:
    dest_file.write(content)
    
#13. replace word
with open("student.txt", "r") as file:
    content = file.read()

content = content.replace("student", "pupil") 
with open("student.txt", "w") as file:
    file.write(content)

#14. marks greater than 75
with open("student.txt", "r") as file:
    for line in file:
        if "Marks:" in line:
            marks = int(line.split("Marks:")[1].strip())
            if marks > 75:
                print(line.strip())
                
#15. binary file employee records
import pickle

records = [
    {"EmpID":101, "Name":"Amit"},
    {"EmpID":102, "Name":"Rahul"}
]

with open("emp.dat", "wb") as f:
    pickle.dump(records, f)

eid = int(input("Enter EmpID: "))

with open("emp.dat", "rb") as f:
    data = pickle.load(f)

for emp in data:
    if emp["EmpID"] == eid:
        print(emp)
        
#ADVANCED QUESTIONS
#1. count blank lines
count = 0

with open("student.txt", "r") as f:
    for line in f:
        if line.strip() == "":
            count += 1

print(count)

#2. count digits, alphabets, and special characters
text = input()

digits = alpha = special = 0

for ch in text:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        alpha += 1
    else:
        special += 1

print("Digits =", digits)
print("Alphabets =", alpha)
print("Special =", special)

#3. display lines starting with vowel
with open("student.txt","r") as f:
    for line in f:
        line = line.strip()
        if line and line[0].lower() in "aeiou":
            print(line)

#4. frequency of given word
word = input("Enter word: ").lower()

with open("student.txt", "r") as f:
    data = f.read().lower()

print(data.split().count(word))

#5. student result file and topper
topper = ""
max_total = 0

with open("result.txt", "r") as f:
    for line in f:
        name, phy, chem, maths = line.strip().split(",")

        total = int(phy) + int(chem) + int(maths)

        if total > max_total:
            max_total = total
            topper = name

print("Topper =", topper)
print("Total Marks =", max_total)