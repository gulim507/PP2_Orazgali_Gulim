a = 5
b = 2
if a > b: print("a is greater than b")

#2 example
a = 6
b = 345
print("A") if a > b else print("B")

#3 example
a = 367
b = 256
print("A") if a > b else print("=") if a == b else print("B")

#4 example
age=18

status="adult" if age>=20 else "child"
print(status)

#5 example
username="Gulim"
display=username if username else "guest"
print("Welcome," , display)
