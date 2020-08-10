import sys

# Defines a simpler communication between classes. Promotes loose coupling.


class Colleague:
    def __init__(self, mediator, id):
        self.mediator = mediator
        self.id = id

    def getID(self):
        return self.id

    def send(self, message):
        pass

    def receive(self, message):
        pass


class ConcreteColleague(Colleague):
    def __init__(self, mediator, id):
        super().__init__(mediator, id)

    def send(self, message):
        print("Message", message, "sent by Colleague", str(self.id))
        self.mediator.distribute(self, message)

    def receive(self, message):
        print("Message", message, "received by Colleague", str(self.id))


class Mediator:
    def add(self, colleague):
        pass

    def distribute(self, sender, message):
        pass


class ConcreteMediator(Mediator):
    def __init__(self):
        Mediator.__init__(self)
        self._colleagues = []

    def add(self, colleague):
        self._colleagues.append(colleague)

    def distribute(self, sender, message):
        for c in self._colleagues:
            if c.getID() != sender.getID():
                c.receive(message)


mediator = ConcreteMediator()

c1 = ConcreteColleague(mediator, 1)
c2 = ConcreteColleague(mediator, 2)
c3 = ConcreteColleague(mediator, 3)

mediator.add(c1)
mediator.add(c2)
mediator.add(c3)

c1.send("Hello")
c3.send("Bye")
