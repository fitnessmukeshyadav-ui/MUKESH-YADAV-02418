inventory = []
next_id = 1101

def add_item():
    global next_id
    name = input("Enter item Name: ").strip()
    try:
        qty = int(input("Enter Quantity: "))
        if qty < 0:
            print("Invalid quantity. Quantity must be a non-negative whole number. Item not added.")
            return
        price = float(input("Enter Price: "))
        if price < 0:
            print("Invalid price. Price must be non-negative. Item not added.")
            return
    except ValueError:
        print("Invalid input. Enter numeric values.")
        return

    item_id = f"I{next_id}"
    next_id += 1
    price = int(price) if price.is_integer() else price
    inventory.append({"id": item_id, "name": name, "quantity": qty, "price": price})
    print(f"Item added.\nID: {item_id} | {name} | Qty: {qty} | Price: {price}")
    if qty < 5:
        print(f"Low stock alert: {name} ({qty})")

def view_items():
    if not inventory:
        print("Inventory is empty.")
        return
    print(f"{'ID':<6} | {'Name':<15} | {'Qty':<5} | {'Price':<8}")
    print("-" * 42)
    for item in inventory:
        print(f"{item['id']:<6} | {item['name']:<15} | {item['quantity']:<5} | {item['price']:<8}")

def update_item():
    item_id = input("Enter Item ID to update: ").strip().upper()
    for item in inventory:
        if item["id"] == item_id:
            try:
                qty = int(input("New Quantity: "))
                price = float(input("New Price: "))
                if qty < 0 or price < 0:
                    print("Quantity and price must be non-negative.")
                    return
                item["quantity"] = qty
                item["price"] = int(price) if price.is_integer() else price
                print(f"Item {item_id} updated.")
                if qty < 5:
                    print(f"Low stock alert: {item['name']} ({qty})")
            except ValueError:
                print("Invalid numeric input.")
            return
    print(f"Item ID {item_id} not found.")

def delete_item():
    item_id = input("Enter Item ID to delete: ").strip().upper()
    for i, item in enumerate(inventory):
        if item["id"] == item_id:
            removed = inventory.pop(i)
            print(f"Item '{removed['name']}' deleted. Items left: {len(inventory)}")
            return
    print(f"Item ID {item_id} not found.")

def search_item():
    query = input("Enter Item ID or Name to search: ").strip().lower()
    found = [i for i in inventory if query in i["id"].lower() or query in i["name"].lower()]
    if not found:
        print("No matching items found.")
        return
    for item in found:
        print(f"ID: {item['id']} | {item['name']} | Qty: {item['quantity']} | Price: {item['price']}")

def total_stock_value():
    if not inventory:
        print("Total stock value: 0")
        return
    breakdown = [f"{item['name']}: {item['quantity'] * item['price']}" for item in inventory]
    total = sum(item["quantity"] * item["price"] for item in inventory)
    print(" | ".join(breakdown))
    print(f"Total stock value: {total}")

def low_stock_report():
    low_items = [item for item in inventory if item["quantity"] < 5]
    if not low_items:
        print("No low stock items.")
        return
    for item in low_items:
        print(f"Low stock (below 5): {item['id']} | {item['name']} | Qty: {item['quantity']}")

def main():
    while True:
        print("\\===== INVENTORY MANAGEMENT SYSTEM =====")
        print("\n1. Add item \n 2. View items\n 3. Update item \n 4. Delete item \n 5. Total stock value \n 6. Low Stock report \n 7. Search item \n 8. Exit")
        choice = input("Choose option: ").strip()
        if choice == "1": add_item()
        elif choice == "2": view_items()
        elif choice == "3": update_item()
        elif choice == "4": delete_item()
        elif choice == "5": total_stock_value()
        elif choice == "6": low_stock_report()
        elif choice == "7": search_item()
        elif choice == "8": break
        else: print("Invalid option.")

if __name__ == "__main__":
    main()
