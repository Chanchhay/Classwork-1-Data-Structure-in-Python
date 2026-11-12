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
