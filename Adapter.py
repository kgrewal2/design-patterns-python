class Korean:
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"


class British:
    def __init__(self):
        self.name = "British"

    def speak_english(self):
        return "Hello"


class Adapter:
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__


korean = Korean()
british = British()
objects = []
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for object in objects:
    print(object.name, object.speak())
