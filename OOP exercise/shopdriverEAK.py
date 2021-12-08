from shopclassEAK import ShopListEAK

def itemsEAK():
    items = []
    num = int(input("Enter number of items ordered: "))
    while num < 1:
        print("Number of items should be at least 1.")
        num = int(input("Enter number of items ordered: "))
    for i in range(num):
        name = input(f"Enter name of food {i+1}: ")
        amount = float(input("Enter amount in pounds: "))
        while amount <= 0:
            print("Amount of food must be more than 0")
            amount = float(input("Enter amount in pounds: "))
        print()
        cart = ShopListEAK(name, amount)
        cart._PriceListEAK()
        items.append(cart)
    return items

def displayEAK(ilist):
    print()
    print("Here's a summary of the items purchased: ")
    print("-" * 40)
    for i in range(len(ilist)):
        print(f"Item: {ilist[i].getNameEAK()}")
        print(f"Amount ordered: {ilist[i].getAmountEAK()} pounds")
        print("Price per pound:", '${:.2f}'.format(ilist[i].getPriceEAK()))
        print("Price of order:", '${:.2f}'.format(ilist[i].getOrderEAK()))
        print()

def totalCostEAK(ilist):
    total = 0.0
    for i in range(len(ilist)):
        total += ilist[i].getOrderEAK()
    return total

def main():
    item_list = itemsEAK()
    displayEAK(item_list)
    print("Total cost:", '${:.2f}'.format(totalCostEAK(item_list)))

main()