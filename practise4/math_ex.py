import math

# 1. Degree to radian
degree = 15
radian = degree * math.pi / 180
print("Radian:", radian)


# 2. Area of a trapezoid
height = 5
base1 = 5
base2 = 6

area = (base1 + base2) * height / 2
print("Area of trapezoid:", area)


# 3. Area of a regular polygon
n = 4
side = 25

area = n * side ** 2 / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", area)


# 4. Area of a parallelogram
base = 5
height = 6

area = base * height
print("Area of parallelogram:", area)