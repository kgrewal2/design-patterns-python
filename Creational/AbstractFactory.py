# PRODUCT A1
class Cat:
    def speak(self):
        print("Meow")

# PRODUCT A2
class CatFood:
    def taste(self):
        print("CatFood")

# CONCRETE FACTORY A
class CatFactory:
    def get_pet(self):
        return Cat()
    def get_pet_food(self):
        return CatFood()

# PRODUCT B1
class Dog:
    def speak(self):
        print("Woof")

# PRODUCT B2
class DogFood:
    def taste(self):
        print("DogFood")

# CONCRETE FACTORY B
class DogFactory:
    def get_pet(self):
        return Dog()
    def get_pet_food(self):
        return DogFood()

# ABSTRACT FACTORY
class PetStore:
    def __init__(self,pet_factory=None):
        self.pet_factory=pet_factory
    def show_pet(self):
        pet=self.pet_factory.get_pet()
        food=self.pet_factory.get_pet_food()
        pet.speak()
        food.taste()

dogFactory=DogFactory()
shop=PetStore(dogFactory)
shop.show_pet()
catFactory=CatFactory()
shop=PetStore(catFactory)
shop.show_pet()
