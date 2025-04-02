import math

def circle_stats(radius):
 area = math.pi * radius ** 2
 circumference = 2 * math.pi * radius
 return area, circumference
print(circle_stats(3))
print(circle_stats(6))
print(circle_stats(9))
print(circle_stats(12))
print(circle_stats(15))