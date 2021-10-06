edge1 = float(input("Enter length of edge1: "))
edge2 = float(input("Enter length of edge2: "))
edge3 = float(input("Enter length of edge3: "))

pair1 = edge1 + edge2 > edge3
pair2 = edge1 + edge3 > edge2
pair3 = edge2 + edge3 > edge1

perimeter = edge1 + edge2 + edge3

if pair1 and pair2 and pair3:
    print("The perimeter is", perimeter)
else:
    print("Perimeter cannot be calculated: the input is invalid.")