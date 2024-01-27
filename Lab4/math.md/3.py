import math
number_of_sides = float(input())
length_of_sides = float(input())
angle = math.pi / number_of_sides
area = number_of_sides * (length_of_sides ** 2) / (4 * math.tan(angle)) #S = n*(l**2)//4tan(pi/n)
print(area)