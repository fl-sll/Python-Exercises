def calc_new_height():
    width = float(input("Enter the current width: "))
    height = float(input("Enter the current height: "))
    ratio = width / height
    width1 = float(input("Enter the desired width: "))
    x = width1 / ratio
    print(f"The corresponding height is: {x}")
    return
calc_new_height()