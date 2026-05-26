# Taking inputs
bill_amount = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
tip_percent = float(input("Enter tip percentage: "))

# Calculations
tip_amount = (bill_amount * tip_percent) / 100
total_with_tip = bill_amount + tip_amount
amount_per_person = total_with_tip / people

# Using modulus operator (%)
remainder = bill_amount % people

# Displaying summary
print("\n===== BILL SUMMARY =====")
print(f"Original Bill Amount : ₹{bill_amount}")
print(f"Tip Percentage       : {tip_percent}%")
print(f"Tip Amount           : ₹{round(tip_amount, 2)}")
print(f"Total With Tip       : ₹{round(total_with_tip, 2)}")
print(f"Amount Per Person    : ₹{round(amount_per_person, 2)}")
print(f"Remainder using %    : {round(remainder, 2)}")
print("========================")