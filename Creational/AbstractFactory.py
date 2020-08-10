# Rather than building a concreate object, we build a family of related or dependent object


class Cat:
    """PRODUCT A1"""
    def speak(self):
        print("Meow")


class CatFood:
    """PRODUCT A2"""
    def taste(self):
        print("CatFood")


class CatFactory:
    """CONCRETE FACTORY A"""
    def get_pet(self):
        return Cat()

    def get_pet_food(self):
        return CatFood()


class Dog:
    """PRODUCT B1"""
    def speak(self):
        print("Woof")


class DogFood:
    """PRODUCT B2"""
    def taste(self):
        print("DogFood")


class DogFactory:
    """CONCRETE FACTORY B"""
    def get_pet(self):
        return Dog()

    def get_pet_food(self):
        return DogFood()


class PetStore:
    """ABSTRACT FACTORY"""
    def __init__(self, pet_factory=None):
        self.pet_factory = pet_factory

    def show_pet(self):
        pet = self.pet_factory.get_pet()
        food = self.pet_factory.get_pet_food()
        pet.speak()
        food.taste()


dogFactory = DogFactory()
shop = PetStore(dogFactory)
shop.show_pet()
catFactory = CatFactory()
shop = PetStore(catFactory)
shop.show_pet()
