class Validator:
    def __init__(self):
        self.errors = []

    def email_validator(self, email):
        if "@" not in email:
            self.errors.append(f"This ${email} Email is not correct")
            return False
        return True
    
    def age_validator(self, age):
        if age <= 18 or age >= 50:
            self.errors.append(f"This ${age} is not suitable for this website")
            return False
        return True

class NameValidator(Validator):
        def say_hello(self):
            print("Hi there")
    

    


validator = NameValidator()
validator.email_validator("ijorayevgmail.com")
validator.age_validator(60)
validator.say_hello()



print(validator.errors)