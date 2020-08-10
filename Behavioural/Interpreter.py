from abc import ABC, abstractmethod

# Specifies how sentences are evaluated in a language.


class Expression():
    @abstractmethod
    def interpret(self, context):
        pass


class TerminalExpression(Expression):
    def __init__(self, string):
        self.string = string

    def interpret(self, context):
        if (self.string.__contains__(context)):
            return True
        return False


class OrExpression(Expression):
    expr1 = None
    expr2 = None

    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context):
        return self.expr1.interpret(context) or self.expr2.interpret(context)


a = TerminalExpression("a")
b = TerminalExpression("b")
exp = OrExpression(a, b)
print(exp.interpret("c"))
