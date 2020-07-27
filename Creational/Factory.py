# PRODUCT ONE
class Dog:
    def speak(self):
        print("Woof")

# PRODUCT TWO
class Cat:
    def speak(self):
        print("Meow")

# FACTORY
class Factory:
    def get_pet(self,pet_type="dog"):
        myDict = dict(dog=Dog(),cat=Cat())
        return myDict.get(pet_type)

factory=Factory()
cat=factory.get_pet("cat")
cat.speak()
