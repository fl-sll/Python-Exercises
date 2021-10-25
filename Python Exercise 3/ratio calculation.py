def calc_new_height():
    width = float(input("Enter the current width: "))
    height = float(input("Enter the current height: "))
    width1 = float(input("Enter the desired width: "))
    ratio = width / height
    x = width1 / ratio
    print(f"The corresponding height is: {x}")
    return
calc_new_height()