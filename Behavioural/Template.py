import sys
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self):
        self.__always_do_this()
        self.do_step_1()
        self.do_step_2()
        self.do_this_or()

    def __always_do_this(self):
        print("Final")

    @abstractmethod
    def do_step_1(self):
        pass

    @abstractmethod
    def do_step_2(self):
        pass

    def do_this_or(self):
        print("Non Overridden behaviour")


class ConcreteClassA(AbstractClass):
    def do_step_1(self):
        print("Step A1")

    def do_step_2(self):
        print("Step A2")


class ConcreteClassB(AbstractClass):
    def do_step_1(self):
        print("Step B1")

    def do_step_2(self):
        print("Step B2")


a = ConcreteClassA()
a.template_method()

b.ConcreteClassB()
b.template_method()
