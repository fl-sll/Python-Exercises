from shopclassEAK import ShopListEAK    # import the class from shopclassEAK.py

def itemsEAK():     # function to take user input
    items = []      # create empty list
    num = int(input("Enter number of items ordered: "))     # takes user no. of food ordered
    while num < 1:
        print("Number of items should be at least 1.")      # prompts user to enter again if no. of food ordered doesn't make sense
        num = int(input("Enter number of items ordered: "))
    for i in range(num):
        name = input(f"Enter name of food {i+1}: ")         # takes user input for name of food ordered
        amount = float(input("Enter amount in pounds: "))   # takes user input for amount of food ordered
        while amount <= 0:
            print("Amount of food must be more than 0")     # prompts user to enter again if amount of food ordered doesn't make sense
            amount = float(input("Enter amount in pounds: "))
        print()
        cart = ShopListEAK(name, amount)        # put name and amount of food ordered into the class
        cart._PriceListEAK()                    # change the prices of food from default
        items.append(cart)                      # append the name and amount to empty list
    return items                                # return the list

def displayEAK(ilist):          # function to display every food ordered

    print()
    print("Here's a summary of the items purchased: ")
    print("-" * 40)
    for i in range(len(ilist)):
        print(f"Item: {ilist[i].getNameEAK()}")         # display name of food ordered
        print(f"Amount ordered: {ilist[i].getAmountEAK()} pounds")      # display amount of food ordered
        print("Price per pound:", '${:.2f}'.format(ilist[i].getPriceEAK()))     # display price of food ordered
        print("Price of order:", '${:.2f}'.format(ilist[i].getOrderEAK()))      # display price according to amount of food ordered
        print()

def totalCostEAK(ilist):    # function to calculate total price of order
    total = 0.0             # set a new variable to store value of total price
    for i in range(len(ilist)):
        total += ilist[i].getOrderEAK()     # add price of order to variable
    return total        # return total price

def main():         #function to execute everything
    item_list = itemsEAK()      # create new variable and assign the value to items function
    displayEAK(item_list)       # display the summary of order according to the list
    print("Total cost:", '${:.2f}'.format(totalCostEAK(item_list)))     # calculate the total cost according to the list

main()      # execute the program