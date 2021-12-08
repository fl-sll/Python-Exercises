class ShopListEAK:
    def __init__(self,name,amount):
        self.__name = name
        self.__amount = amount
        self.__price = 0.0      # set default price to 0.0
        self.__order = 0.0      # set default order to 0.0
    
    def _PriceListEAK(self):    # set values of food
        if self.__name == "Dry Cured Iberian Ham":
            self.__price = 177.80
        elif self.__name == "Wagyu Steaks":
            self.__price = 450.00
        elif self.__name == "Matsutake Mushrooms":
            self.__price = 272.00
        elif self.__name == "Kopi Luwak Coffee":
            self.__price = 306.50
        elif self.__name == "Moose Cheese":
            self.__price = 487.20
        elif self.__name == "White Truffles":
            self.__price = 3600.00
        elif self.__name == "Blue Fin Tuna":
            self.__price = 3603.00
        elif self.__name == "Le Bonnotte Potatoes":
            self.__price = 270.81
        else:
            self.__price = 0.0

    def getNameEAK(self):   # gives name of food
        return self.__name
    
    def getAmountEAK(self): # gives amount of food
        return self.__amount
    
    def getPriceEAK(self):  # fives price of food
        return self.__price
    
    def getOrderEAK(self):  # gives order(amount*price) of food
        self.__order = self.__price * self.__amount
        return self.__order