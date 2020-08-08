class Car():
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return (self.model + self.tires + self.engine)


class Builder():
    def __init__(self):
        self.car = None

    def createNewCar(self):
        self.car = Car()


class SkylarkBuilder(Builder):
    def add_model(self):
        self.car.model = "Skylark Model"

    def add_engine(self):
        self.car.engine = "Skylark Engine"

    def add_tires(self):
        self.car.tires = "Skylark Tires"


class Director():
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self):
        self.builder.createNewCar()
        self.builder.add_engine()
        self.builder.add_tires()
        self.builder.add_model()

    def get_car(self):
        return self.builder.car


builder = SkylarkBuilder()
director = Director(builder)
director.construct_car()
print(director.get_car())
