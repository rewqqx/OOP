class Receiver:
    def compute(self, x, y):
        return x + y


class Command:
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self, x, y):
        pass


class ConcreteCommand(Command):
    def execute(self, x, y):
        return self.receiver.compute(x, y)


class Invoker:
    def __init__(self):
        self.history = []

    def execute(self, command, x, y):
        result = command.execute(x, y)
        self.history.append(command)
        return result

    def undo(self):
        command = self.history.pop()
        return command.execute(-1, -1)


if __name__ == "__main__":

    invoker = Invoker()

    receiver = Receiver()
    print(invoker.execute(ConcreteCommand(receiver), 1, 2))
