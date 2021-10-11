x = int(input("Enter the number of packages purchased: "))

if x >= 10 and x <= 19:
    discount = 10
elif x >= 20 and x <= 49:
    discount = 20
elif x >= 50 and x <= 99:
    discount = 30
elif x >= 100:
    discount = 40
else:
    discount = 0

discount_amount = ((discount) / 100) * x * 99
total_amount = ((x * 99) - discount_amount)
format_discount_amount = "{:.2f}".format(discount_amount)
format_total_amount = "{:.2f}".format(total_amount)

print("Discount Amount @", discount,"% : $", format_discount_amount)
print("Total Amount: $", format_total_amount)
