class SubSystemA:
    def method1(self):
        print("SubSystemA > Method1")

    def method2(self):
        print("SubSystemA > Method2")


class SubSystemB:
    def method1(self):
        print("SubSystemB > Method1")

    def method2(self):
        print("SubSystemB > Method2")


class Facade:
    def __init__(self):
        self._subsystemA = SubSystemA()
        self._subsystemB = SubSystemB()

    def method_All(self):
        self._subsystemA.method1()
        self._subsystemB.method2()


facade = Facade()
facade.method_All()
