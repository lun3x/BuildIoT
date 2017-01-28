class Servo:
    def __init__(self, n):
        self.n = n

class Button:
    def __init__(self, n):
        self.n = n
        self.when_pressed = self.foo
        self.when_released = self.bar

    def foo(self):
        pass

    def bar(self):
        pass
