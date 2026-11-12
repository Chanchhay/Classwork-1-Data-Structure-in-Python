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
