Used to store all the information required for executing an action, including the methods to call, method arguments, and the object that implements the method.

class Command:
    def execute(self):
        pass


class Copy(Command):
    def execute(self):
        print("Copying")


class Paste(Command):
    def execute(self):
        print("Pasting")


class Save(Command):
    def execute(self):
        print("Saving")


class Macro:
    def __init__(self):
        self.commands = []

    def add(self, command):
        self.commands.append(command)

    def sum(self):
        for c in self.commands:
            c.execute()


macro = Macro()
macro.add(Copy())
macro.add(Paste())
macro.add(Save())
macro.sum()
