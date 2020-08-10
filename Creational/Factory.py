# Used when we want a common interface to create different objects


class Dog:
    """ PRODUCT ONE """
    def speak(self):
        print("Woof")


class Cat:
    """ PRODUCT TWO """
    def speak(self):
        print("Meow")


class Factory:
    """FACTORY"""
    def get_pet(self, pet_type="dog"):
        myDict = dict(dog=Dog(), cat=Cat())
        return myDict.get(pet_type)


factory = Factory()
cat = factory.get_pet("cat")
cat.speak()
