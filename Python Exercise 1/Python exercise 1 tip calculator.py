subtotal = float(input("Enter the subtotal: "))
tip = float(input("Enter tip amount (as a %): "))

print("Subtotal: ", "$", "{:0,.2f}".format(subtotal))
tip1 = (subtotal * (tip/100))
print("Tip: ", "$","{:0,.2f}".format(tip1))

total = subtotal + tip1
print("Total: ", "$" "{:0,.2f}".format(total))
