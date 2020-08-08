class SingletonGovt:
    __instance__ = None
    value = ""

    def __init__(self):
        if SingletonGovt.__instance__ is None:
            SingletonGovt.__instance__ = self
        else:
            raise Exception("Can't create another instance")

    @staticmethod
    def get_instance():
        if not SingletonGovt.__instance__:
            SingletonGovt()
        else:
            return SingletonGovt.__instance__

    def __str__(self):
        return self.value


government = SingletonGovt()
government.value = "Karandeep"
print(government)

same_government = SingletonGovt.get_instance()
same_government.value = "Grewal"
print(same_government)

another_government = SingletonGovt.get_instance()
another_government.value = "Nothing"
print(another_government)
