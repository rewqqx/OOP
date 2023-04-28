from abc import ABC, abstractmethod


class Game(ABC):
    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def end(self):
        pass

    def play(self):
        self.initialize()
        self.start()
        self.end()


class TicTacToe(Game):
    def initialize(self):
        print("TicTacToe: Initialize")

    def start(self):
        print("TicTacToe: Start")

    def end(self):
        print("TicTacToe: End")


class Chess(Game):
    def initialize(self):
        print("Chess: Initialize")

    def start(self):
        print("Chess: Start")

    def end(self):
        print("Chess: End")


if __name__ == "__main__":

    ticTacToe = TicTacToe()
    chess = Chess()

    ticTacToe.start()
    chess.start()