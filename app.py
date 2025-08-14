import json
import os

ORDERS_FILE = "orders.json"

# Load existing orders
if os.path.exists(ORDERS_FILE):
    with open(ORDERS_FILE, "r") as f:
        orders = json.load(f)
else:
    orders = []

def save_orders():
    with open(ORDERS_FILE, "w") as f:
        json.dump(orders, f, indent=4)

def add_order():
    order_id = input("Order ID: ")
    item = input("Item Name: ")
    quantity = int(input("Quantity: "))
    status = input("Status: ")
    orders.append({"id": order_id, "item": item, "quantity": quantity, "status": status})
    save_orders()
    print("Order added!\n")

def list_orders(filter_status=None):
    for o in orders:
        if filter_status and o["status"] != filter_status:
            continue
        print(f"ID: {o['id']}, Item: {o['item']}, Qty: {o['quantity']}, Status: {o['status']}")
    print()

def update_status():
    order_id = input("Order ID to update: ")
    for o in orders:
        if o["id"] == order_id:
            new_status = input("New status: ")
            o["status"] = new_status
            save_orders()
            print("Status updated!\n")
            return
    print("Order not found.\n")

def menu():
    while True:
        print("1. Add Order")
        print("2. List Orders")
        print("3. Update Status")
        print("4. Filter by Status")
        print("5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_order()
        elif choice == "2":
            list_orders()
        elif choice == "3":
            update_status()
        elif choice == "4":
            status = input("Status to filter by: ")
            list_orders(filter_status=status)
        elif choice == "5":
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    menu()
