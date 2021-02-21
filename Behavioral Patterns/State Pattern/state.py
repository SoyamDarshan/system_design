"""
A pattern in which the object's behaviour is determined by its state.
An object transitions from one state to another (something that needs to trigger a transition)
A formalized construct which manages state and transitions is called a state machine
"""
from abc import ABC


class Switch:
    def __init__(self):
        self.state = OffState()

    def on(self):
        # take the current state and transition it to the next state
        self.state.on(self)

    def off(self):
        self.state.off(self)


class State(ABC):
    def on(self, switch):
        print('Light is already on')

    def off(self, switch):
        print('Light is already off')


class OnState(State):
    def __init__(self):
        print('Light turned on')

    def off(self, switch):
        print('Turning light off')
        switch.state = OffState()


class OffState(State):
    def __init__(self):
        print('Light turned off')

    def on(self, switch):
        print('Turnng light on')
        switch.state = OnState()


if __name__ == '__main__':
    sw = Switch()
    sw.on()
    sw.off()
    sw.on()
    sw.on()
