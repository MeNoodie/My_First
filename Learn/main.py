class car():
    def __init__(self, brand , Type):
        self.name = brand 
        self.type = Type

c1 = car("Bmw" , "sport")
print(c1.__dict__)

