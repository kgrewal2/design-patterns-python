# Change the object's behaviour when its state changes.


class ATMState():
    name = "state"
    allowed = []

    def go_next(self, state):
        if state.name in self.allowed:
            print("Current State changes from", self, "to", state.name)
            self.__class__ = state
        else:
            print("Give State change not possible")

    def __str__(self):
        return self.name


class OffState(ATMState):
    name = "off"
    allowed = ["on"]


class OnState(ATMState):
    name = "on"
    allowed = ["off"]


class ATM():
    def __init__(self):
        self.current = OffState()

    def set_state(self, state):
        self.current.go_next(state)


atm = ATM()
atm.set_state(OnState)
atm.set_state(OffState)
atm.set_state(OnState)
