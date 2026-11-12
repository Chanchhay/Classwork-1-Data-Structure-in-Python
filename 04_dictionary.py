"""Page 4 - Dictionary practice: product inventory."""

print("\n" + "=" * 55)
print("PAGE 4: DICTIONARY PRACTICE")
print("=" * 55)

# Task 1: Create an inventory with three products.
inventory = {"Laptop": 5, "Mouse": 10, "Keyboard": 0}
print("\nTask 1 - Inventory:", inventory)

# Task 2: Safely get a product's stock even if the product is missing.
print("\nTask 2 - Monitor stock (default 0):", inventory.get("Monitor", 0))

# Task 3: Add two products and update one existing stock number.
inventory.update({"Monitor": 7, "Webcam": 4, "Mouse": 12})
print("\nTask 3 - Updated inventory:", inventory)

# Task 4: Print products and their stock using items().
print("\nTask 4 - Product stock list:")
for product, stock in inventory.items():
    print(f" - {product}: {stock}")

# Task 5: Remove a sold-out product using pop().
removed_stock = inventory.pop("Keyboard")
print("\nTask 5 - Removed Keyboard (stock):", removed_stock)
print("Inventory after removal:", inventory)

# Task 6: Add a new product only if it is not already present.
inventory.setdefault("Headphones", 6)
print("\nTask 6 - Inventory after setdefault:", inventory)

# Task 7: Add up all stock numbers using values() and sum().
total_stock = sum(inventory.values())
print("\nTask 7 - Total stock:", total_stock)

# Task 8: Create a backup, then clear the original dictionary.
inventory_backup = inventory.copy()
inventory.clear()
print("\nTask 8 - Backup:", inventory_backup)
print("Original inventory after clear:", inventory)
