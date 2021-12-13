import math

class Circle:
    def __init__(self,radius = 1.0,color = "red"):
        self.__radius = radius
        self.__color = color
    
    def getRadius(self):
        return self.__radius
    
    def getColor(self):
        return self.__color
    
    def getArea(self):
        return math.pi * self.__radius

    def setRadius(self, new_radius):
        self.__radius = new_radius

    def setColor(self, new_color):
        self.__color = new_color

    def toString(self, statement):
        s1 = str(statement)
        return s1

class Cylinder(Circle):
    def __init__(self, radius, color, height = 1.0):
        super().__init__(radius, color)
        self.__height = height

    def getHeight(self):
        return self.__height
    
    def setHeight(self, new_height):
        self.__height = new_height
    
    def getVolume(self):
        return Circle.getArea(self) * self.__height