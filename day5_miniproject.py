# Smart Inventory Management System

inventory = {}
categories = set()


def add_product():
    pid = input("Enter Product ID: ")

    if pid in inventory:
        print("Product ID already exists!")
        return

    name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    qty = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))
    supplier = input("Enter Supplier: ")

    inventory[pid] = {
        "name": name,
        "category": category,
        "quantity": qty,
        "price": price,
        "supplier": supplier
    }

    categories.add(category)
    print("Product Added Successfully!")


def update_inventory():
    pid = input("Enter Product ID: ")

    if pid not in inventory:
        print("Product not found!")
        return

    print("1. Update Quantity")
    print("2. Update Price")

    choice = input("Enter choice: ")

    if choice == "1":
        inventory[pid]["quantity"] = int(input("New Quantity: "))
    elif choice == "2":
        inventory[pid]["price"] = float(input("New Price: "))

    print("Inventory Updated Successfully!")


def search_product():
    keyword = input("Enter Product ID or Name: ").lower()

    found = False

    for pid, product in inventory.items():
        if pid.lower() == keyword or product["name"].lower() == keyword:
            print("\nProduct Found")
            print("ID:", pid)
            print("Name:", product["name"])
            print("Category:", product["category"])
            print("Quantity:", product["quantity"])
            print("Price:", product["price"])
            print("Supplier:", product["supplier"])
            found = True

    if not found:
        print("Product not found!")


def display_inventory():
    if not inventory:
        print("Inventory is empty!")
        return

    print("\n" + "=" * 80)
    print(f"{'ID':<10}{'NAME':<20}{'CATEGORY':<15}{'QTY':<10}{'PRICE':<10}")
    print("=" * 80)

    for pid, product in inventory.items():
        print(
            f"{pid:<10}"
            f"{product['name']:<20}"
            f"{product['category']:<15}"
            f"{product['quantity']:<10}"
            f"{product['price']:<10}"
        )


def low_stock_alert():
    threshold = 10

    print("\nLow Stock Products")

    found = False

    for pid, product in inventory.items():
        if product["quantity"] < threshold:
            print(f"{product['name']} -> Qty: {product['quantity']}")
            found = True

    if not found:
        print("No low stock products.")


def out_of_stock_alert():
    print("\nOut Of Stock Products")

    found = False

    for pid, product in inventory.items():
        if product["quantity"] == 0:
            print(product["name"])
            found = True

    if not found:
        print("No out of stock products.")


def category_management():
    print("\nAvailable Categories")
    for category in categories:
        print(category)


def inventory_report():
    total_items = 0
    total_value = 0

    for product in inventory.values():
        total_items += product["quantity"]
        total_value += product["quantity"] * product["price"]

    print("\nInventory Report")
    print("Total Items :", total_items)
    print("Total Value :", total_value)

    print("\nCategory Summary")
    for category in categories:
        count = 0
        for product in inventory.values():
            if product["category"] == category:
                count += 1
        print(category, ":", count)


def delete_product():
    pid = input("Enter Product ID to delete: ")

    if pid in inventory:
        del inventory[pid]
        print("Product Deleted Successfully!")
    else:
        print("Product not found!")


while True:
    print("\n===== SMART INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Update Inventory")
    print("3. Search Product")
    print("4. Display Inventory")
    print("5. Low Stock Alert")
    print("6. Out Of Stock Alert")
    print("7. Category Management")
    print("8. Inventory Report")
    print("9. Delete Product")
    print("10. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        update_inventory()

    elif choice == "3":
        search_product()

    elif choice == "4":
        display_inventory()

    elif choice == "5":
        low_stock_alert()

    elif choice == "6":
        out_of_stock_alert()

    elif choice == "7":
        category_management()

    elif choice == "8":
        inventory_report()

    elif choice == "9":
        delete_product()

    elif choice == "10":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")