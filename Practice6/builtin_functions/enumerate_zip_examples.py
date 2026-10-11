names = ["Alice", "Bob", "Charlie"]
grades = [90, 85, 95]

# enumerate
print("Enumerate:")
for index, name in enumerate(names):
    print(index, name)

# zip
print("Zip:")
for name, grade in zip(names, grades):
    print(name, grade)

# zip with two lists
subjects = ["Math", "English", "Programming"]

print("Students and subjects:")
for name, subject in zip(names, subjects):
    print(name, subject)

# sorted
students = [("Alice", 90), ("Bob", 85), ("Charlie", 95)]

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

print("Sorted students:")
for student in sorted_students:
    print(student)