# Here is a list of student names.
students = ["Gulim", "Aruzhan", "Dana", "Madi"]


# Here is an example of sorting names by their length.
sorted_students = sorted(
    students,
    key=lambda name: len(name)
)

print("Sorted by name length:", sorted_students)


# Here is a list of students with their scores.
scores = [
    ("Gulim", 95),
    ("Aruzhan", 88),
    ("Dana", 92),
    ("Madi", 75)
]


# Here is an example of sorting students by score.
sorted_scores = sorted(
    scores,
    key=lambda student: student[1],
    reverse=True
)

print("Sorted by score:", sorted_scores)