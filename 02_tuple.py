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
