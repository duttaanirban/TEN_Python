# ==========================================
# ASSIGNMENT 1 - EMI CALCULATOR
# ASSIGNMENT 2 - TAX CALCULATOR
# ASSIGNMENT 3 - ATTENDANCE CALCULATOR
# ==========================================

def emi_calculator():
    print("\n===== EMI CALCULATOR =====")

    principal = float(input("Enter Loan Amount: "))
    annual_rate = float(input("Enter Annual Interest Rate (%): "))
    years = int(input("Enter Loan Tenure (Years): "))

    monthly_rate = annual_rate / (12 * 100)
    months = years * 12

    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / \
          ((1 + monthly_rate) ** months - 1)

    total_payment = emi * months
    total_interest = total_payment - principal

    print("\n----- EMI DETAILS -----")
    print(f"Monthly EMI      : ₹{emi:.2f}")
    print(f"Total Payment    : ₹{total_payment:.2f}")
    print(f"Total Interest   : ₹{total_interest:.2f}")


def tax_calculator():
    print("\n===== TAX CALCULATOR =====")

    income = float(input("Enter Annual Income: "))

    tax = 0

    if income <= 300000:
        tax = 0

    elif income <= 600000:
        tax = (income - 300000) * 0.05

    elif income <= 900000:
        tax = (300000 * 0.05) + ((income - 600000) * 0.10)

    elif income <= 1200000:
        tax = (300000 * 0.05) + (300000 * 0.10) + \
              ((income - 900000) * 0.15)

    else:
        tax = (300000 * 0.05) + (300000 * 0.10) + \
              (300000 * 0.15) + ((income - 1200000) * 0.20)

    print("\n----- TAX REPORT -----")
    print(f"Annual Income : ₹{income:,.2f}")
    print(f"Tax Payable   : ₹{tax:,.2f}")
    print(f"Net Income    : ₹{income-tax:,.2f}")


def attendance_calculator():
    print("\n===== ATTENDANCE CALCULATOR =====")

    attended = int(input("Classes Attended: "))
    total = int(input("Total Classes Conducted: "))
    target = float(input("Target Attendance %: "))

    current = (attended / total) * 100

    print("\n----- ATTENDANCE REPORT -----")
    print(f"Current Attendance : {current:.2f}%")

    if current >= target:
        print("Requirement Met ✅")

    else:
        extra_classes = 0
        a = attended
        t = total

        while (a / t) * 100 < target:
            a += 1
            t += 1
            extra_classes += 1

        print("Requirement Not Met ❌")
        print(f"Attend next {extra_classes} classes continuously")
        print(f"to reach {target}% attendance.")


# ===========================
# MAIN MENU
# ===========================

while True:

    print("\n")
    print("=" * 40)
    print("       PYTHON MINI PROJECTS")
    print("=" * 40)
    print("1. EMI Calculator")
    print("2. Tax Calculator")
    print("3. Attendance Calculator")
    print("4. Exit")
    print("=" * 40)

    choice = input("Enter Choice (1-4): ")

    if choice == "1":
        emi_calculator()

    elif choice == "2":
        tax_calculator()

    elif choice == "3":
        attendance_calculator()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")