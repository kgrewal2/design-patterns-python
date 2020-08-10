import copy

# Create new instance of object using cloning method. Used when creating the object is resource intensive or time-consuming


class Car:
    def __init__(self):
        self.engine = "3200cc"
        self.color = "Blue"
        self.seats = "5"

    def __str__(self):
        return '{} | {} | {}'.format(self.engine, self.color, self.seats)


class Prototype:
    def __init__(self):
        self._toBeCloneObjects = {}

    def registerObject(self, name, obj):
        self._toBeCloneObjects[name] = obj

    def unregisterObject(self, name):
        del self._toBeCloneObjects[name]

    def clone(self, name, **args):
        clonedObject = copy.deepcopy(self._toBeCloneObjects.get(name))
        clonedObject.__dict__.update(args)
        return clonedObject


defaultCar = Car()
prototype = Prototype()
prototype.registerObject('basicCar', defaultCar)

carOne = prototype.clone('basicCar', color="red")
print(carOne)
