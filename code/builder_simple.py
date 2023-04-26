class House:
    def __init__(self):
        self.material = None
        self.doors = None
        self.windows = None

    def __str__(self):
        return f"House of {self.material} with {self.doors} doors and {self.windows} windows."


class Builder:
    def build_material(self):
        pass

    def build_doors(self):
        pass

    def build_windows(self):
        pass


class ConcreteBuilderWoodenHouse(Builder):
    def __init__(self):
        self.house = House()

    def build_material(self):
        self.house.material = "wood"

    def build_doors(self):
        self.house.doors = 4

    def build_windows(self):
        self.house.windows = 8


class ConcreteBuilderBrickHouse(Builder):
    def __init__(self):
        self.house = House()

    def build_material(self):
        self.house.material = "brick"

    def build_doors(self):
        self.house.doors = 2

    def build_windows(self):
        self.house.windows = 6


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_material()
        self.builder.build_doors()
        self.builder.build_windows()
        return self.builder.house


if __name__ == "__main__":
    wooden_director = Director(ConcreteBuilderWoodenHouse())
    brick_director = Director(ConcreteBuilderBrickHouse())

    wooden_house = wooden_director.construct()
    brick_house = brick_director.construct()

    if wooden_house.material != brick_house.material:
        print("Builder works, houses with different material")
    else:
        print("Builder failed, both houses contain same material")
