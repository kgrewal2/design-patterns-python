class House(object):
    def accept(self, visitor):
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print("Work done by ", hvac_specialist)

    def work_on_electrician(self, electrician):
        print("Work done by ", electrician)

    def __str__(self):
        return self.__class__.__name__


class Visitor(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Hvac_specialist(Visitor):
    def visit(self, house):
        house.work_on_hvac(self)


class Electrician(Visitor):
    def visit(self, house):
        house.work_on_electrician(self)


hvac = Hvac_specialist("Jack")
electrician = Electrician("John")

house = House()
house.accept(hvac)
house.accept(electrician)
