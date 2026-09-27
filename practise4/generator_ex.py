# 1. Squares up to N
def squares(n):
    for i in range(n + 1):
        yield i * i


for number in squares(5):
    print(number)


# 2. Even numbers from 0 to n
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


n = int(input("Enter n: "))
print(",".join(str(number) for number in even_numbers(n)))


# 3. Numbers divisible by 3 and 4
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


for number in divisible_by_3_and_4(50):
    print(number)


# 4. Squares from a to b
def squares_range(a, b):
    for i in range(a, b + 1):
        yield i * i


for number in squares_range(2, 6):
    print(number)


# 5. Numbers from n down to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1


for number in countdown(5):
    print(number)