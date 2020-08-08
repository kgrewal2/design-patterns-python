class Component(object):
    levelSep = "  "

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass


class Child(Component):
    def __init__(self, *args, **kwargs):
        self.name = args[0]

    def component_function(self, level):
        print(level * self.levelSep, self.name)


class Composite(Component):
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]
        self.children = []

    def append_children(self, child):
        self.children.append(child)

    def remove_children(self, child):
        self.children.remove(child)

    def component_function(self, level):
        print(level * self.levelSep, self.name)
        for i in self.children:
            i.component_function(level + 1)


sub1 = Composite("SubMenu1")
sub11 = Child("SubMenu11")
sub12 = Child("SubMenu12")

sub1.append_children(sub11)
sub1.append_children(sub12)

top = Composite("Top")
sub2 = Child("SubMenu2")
top.append_children(sub1)
top.append_children(sub2)

top.component_function(0)
