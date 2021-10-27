def pyramid():
    height = int(input("Enter height of pyramid: "))
    for i in range(height):
        print(" " * (height-i), "*" * (i+1), end = "")
        print("*" * (i), " " * (height-i), end="")
        print()
    for i in range(height-2, -1, -1):
        print(" " * (height-i), "*" * (i+1), end = "")
        print("*" * (i), " " * (height-i), end="")
        print()
pyramid()