# Comparison results
print(10 > 9)
print(10 == 9)
print(10 < 9)

#if-else
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# bool() function
print(bool("Hello"))
print(bool(15))

# variables
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Values that are True
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# Values that are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool([]))

# A function can return a Boolean value
def myFunction():
    return True

print(myFunction())

# Boolean value in if-else
if myFunction():
    print("YES!")
else:
    print("NO!")

# isinstance() returns a Boolean value
x = 200
print(isinstance(x, int))