import random

target_units = int(input("Enter target units: "))
workers_per_shift = int(input("Enter workers per shift: "))
defect_rate = float(input("Enter defect rate (%): "))

total_produced = 0

for shift in range(1, 4):
    print(f"\n----- SHIFT {shift} -----")

    shift_produced = 0
    shift_defects = 0

    for cycle in range(1, 21):

        is_defective = random.randint(1, 100) <= defect_rate

        if is_defective:
            shift_defects += 1
            continue

        total_produced += 1
        shift_produced += 1

        if total_produced >= target_units:
            print("\nTarget reached!")
            break

    productivity = shift_produced / workers_per_shift

    print("Items Produced :", shift_produced)
    print("Defective Items:", shift_defects)
    print("Worker Productivity:", round(productivity, 2))

    if total_produced >= target_units:
        break

print("\n========== FINAL REPORT ==========")
print("Total Good Units Produced:", total_produced)
print("Target Units:", target_units)

if total_produced >= target_units:
    print("Status: TARGET ACHIEVED")
else:
    print("Status: TARGET NOT ACHIEVED")