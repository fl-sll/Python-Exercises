import math

mass = float(input("Enter the mass of the cart (in kg): "))
F = float(input("Enter the force to push the cart (in N): "))
g = 9.8

angle = ((F)/(mass*g))
angle1 = math.asin(angle)
deg_format_angle = math.degrees(angle1)
format_angle = "{:.1f}".format(deg_format_angle)

print("The angle of the ramp is", format_angle, "degrees")