from no2class import Cylinder

def main():
    cyl = Cylinder(1, "red", 1)
    print(f"Radius is {cyl.getRadius()}")
    print(f"Height is {cyl.getHeight()}")
    print(f"Color is {cyl.toString(cyl.getColor())}")
    print(f"Area is {'{:.2f}'.format(cyl.getArea())}")
    print(f"Volume i {'{:.2f}'.format(cyl.getVolume())}")
    new_radius = int(input("Enter new radius: "))
    new_height = int(input("Enter new height: "))
    new_color = input("Enter new color: ")
    cyl.setRadius(new_radius)
    cyl.setHeight(new_height)
    cyl.setColor(new_color)
    print(f"New Radius is {cyl.getRadius()}")
    print(f"New Color is {cyl.toString(cyl.getColor())}")
    print(f"New Area is {'{:.2f}'.format(cyl.getArea())}")
    print(f"New Volume is {'{:.2f}'.format(cyl.getVolume())}")

main()