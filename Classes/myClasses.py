class Shark:
    def __init__(self,name,age): #constructor method
        self.name = name
        self.age = age
    
    def swim(self):
        print(self.name, "is swimming")

    def be_awesome(self):
        print(self.name, "is being awesome")
    
    def old(self):
        print(self.name, "is", self.age, "years old")