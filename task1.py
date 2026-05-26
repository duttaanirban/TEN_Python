# Taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
favorite_subject = input("Enter your favourite subject: ")

# Calculating birth year
birth_year = 2024 - age

# Displaying profile card
print("\n===== PERSONAL PROFILE CARD =====")
print(f"Name             : {name}")
print(f"Age              : {age}")
print(f"City             : {city}")
print(f"Favourite Subject: {favorite_subject}")
print(f"Birth Year       : {birth_year}")
print("=================================")