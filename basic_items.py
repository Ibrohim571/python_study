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

print(dog.name)

cat1 = Cat("name", "beshkent", "grey")

print(cat1.address)

class RestApi:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens

dev_config = RestApi("sk-dev-key", max_tokens=50)