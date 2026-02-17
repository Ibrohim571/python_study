class Dog:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

class Cat:
    def __init__(self, name, address, color):
        self.name = name
        self.address = address
        self.color = color


dog = Dog("Tuzik", "Bulldog")

print(dog)