import math

length = float(input("Enter the side length of the hexagon: "))

area = (((3*math.sqrt(3))/2)*math.pow(length, 2))
format_area = "{:.3f}" .format(area)
print("The area of a hexagon with side length", length, "is", format_area)