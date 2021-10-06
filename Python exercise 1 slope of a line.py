x1 = float(input("Enter coordinate of x1:"))
y1 = float(input("Enter coordinate of y1:"))
x2 = float(input("Enter coordinate of x2:"))
y2 = float(input("Enter coordinate of y2:"))

slope = ((y2 - y1) / (x2 - x1))

format_slope = "{:.5f}" .format(slope)

print("The slope for the line that connects two points","(", x1, ",", y1, ")", "and", "(", x2, ",", y2, ")", "is", format_slope)
