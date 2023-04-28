class Target:
    def request(self):
        pass


class Adaptee:
    def special_request(self):
        pass


class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        self.adaptee.special_request()


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    Adapter(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.special_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter(adaptee)
    adapter.request()

