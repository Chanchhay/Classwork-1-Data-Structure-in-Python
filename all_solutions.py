"""Python Data Structures Practice - Complete Homework (Pages 1-4).

Run: python all_solutions.py
"""



# ------------------------------------------------------------------------
# 01_list.py
# ------------------------------------------------------------------------

"""Page 1 - List practice: shopping list operations."""

print("\n" + "=" * 55)
print("PAGE 1: LIST PRACTICE")
print("=" * 55)

# Task 1: Create at least five items, including "milk" twice.
shopping_list = ["milk", "rice", "apples", "milk", "bananas"]
print("\nTask 1 - Shopping list:", shopping_list)

# Task 2: Display the second item, last item, and list length.
print("\nTask 2 - Second item:", shopping_list[1])
print("Last item:", shopping_list[-1])
print("Total items:", len(shopping_list))

# Task 3: Append "eggs" and insert "bread" at the second position.
shopping_list.append("eggs")
shopping_list.insert(1, "bread")
print("\nTask 3 - List after adding eggs and bread:", shopping_list)
# Inserting at index 1 shifts later items one position to the right.

# Task 4: Remove one occurrence of "milk".
length_before = len(shopping_list)
shopping_list.remove("milk")
print("\nTask 4 - List after removing one milk:", shopping_list)

# Task 5: Check whether milk remains and whether length changed.
print("\nTask 5 - Milk still exists:", "milk" in shopping_list)
print("Length before removal:", length_before)
print("Length after removal:", len(shopping_list))
print("Removing an item reduces the length by one:", length_before - len(shopping_list) == 1)

# Task 6: Print each item, then print the number of items.
print("\nTask 6 - Shopping items:")
for item in shopping_list:
    print(" -", item)
print("Total items:", len(shopping_list))

# Note: The worksheet does not include Task 7.

# Task 8: Remove the final item.
removed_item = shopping_list.pop()
print("\nTask 8 - Removed last item:", removed_item)
print("Updated list:", shopping_list)

# Task 9: Keep an unsorted copy and alphabetically sort the list.
unsorted_copy = shopping_list.copy()
shopping_list.sort()
print("\nTask 9 - Sorted list:", shopping_list)
print("Unsorted copy (unchanged):", unsorted_copy)


# ------------------------------------------------------------------------
# 02_tuple.py
# ------------------------------------------------------------------------

"""Page 2 - Tuple practice: student data and courses."""

print("\n" + "=" * 55)
print("PAGE 2: TUPLE PRACTICE")
print("=" * 55)

# Task 1: Student registration.
student = ("Dara", 20, "Computer Science", "Year 3")
print("\nTask 1 - Student Registration")
print("Name:", student[0])
print("Major:", student[2])
print("Number of tuple items:", len(student))
print("Year (negative index):", student[-1])

# Task 2: Course enrollment.
courses = ("Python", "Database", "Networking", "Python", "Web Development")
print("\nTask 2 - Course Enrollment")
print("How many times Python appears:", courses.count("Python"))
print("Index of Networking:", courses.index("Networking"))
print("Registered courses:")
for course in courses:
    print(" -", course)

# Task 3: Convert a tuple to a list, update it, and convert back.
registered_courses = ("Python", "Database", "Networking")
course_list = list(registered_courses)
course_list.append("Cloud Computing")
registered_courses = tuple(course_list)
print("\nTask 3 - Updated Student Courses:", registered_courses)


# ------------------------------------------------------------------------
# 03_set.py
# ------------------------------------------------------------------------

"""Page 3 - Set practice: file backup comparison."""

print("\n" + "=" * 55)
print("PAGE 3: SET PRACTICE")
print("=" * 55)

# Task 1: Create yesterday's and today's file sets.
yesterday = {"a.txt", "b.txt", "c.txt"}
today = {"b.txt", "c.txt", "d.txt"}
print("\nTask 1 - Yesterday:", sorted(yesterday))
print("Today:", sorted(today))

# Task 2: Find added and deleted files using set difference.
new_files = today - yesterday
deleted_files = yesterday - today
print("\nTask 2 - New files:", sorted(new_files))
print("Deleted files:", sorted(deleted_files))

# Task 3: Find unchanged files using intersection.
unchanged_files = yesterday & today
print("\nTask 3 - Unchanged files:", sorted(unchanged_files))

# Task 4: Find all changes using symmetric difference.
all_changes = yesterday ^ today
print("\nTask 4 - All changed files:", sorted(all_changes))

# Task 5: Find all files ever seen using union.
all_files = yesterday | today
print("\nTask 5 - All files ever seen:", sorted(all_files))
# sorted() is for predictable display; the underlying objects remain sets.


# ------------------------------------------------------------------------
# 04_dictionary.py
# ------------------------------------------------------------------------

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
