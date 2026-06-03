# BUG 1 - RUNTIME ERROR
# Type  : ZeroDivisionError
# Cause : Dividing by len(marks) when list is empty
# Fix   : Check if list contains values before division

# marks = []

# average = sum(marks) / len(marks)

# print("Average:", average)

# Fixed Code
# marks = []

# if len(marks) > 0:
#     average = sum(marks) / len(marks)
#     print("Average:", average)
# else:
#     print("No marks available.")

# BUG 2 - LOGICAL ERROR
# Type  : Wrong Formula
# Cause : Average calculated using 4 instead of total students
# Fix   : Divide by len(marks)

# marks = [80, 75, 90, 85, 70]

# average = sum(marks) / 4

# print("Average:", average)

# Fixed Code
# marks = [80, 75, 90, 85, 70]
# average = sum(marks) / len(marks)
# print("Average:", average)

# Final Working code
marks = []

for i in range(5):
    mark = float(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

print("\n----- RESULT -----")
print("Total Marks :", total)
print("Average Marks :", average)
print("Highest Marks :", highest)
print("Lowest Marks :", lowest)