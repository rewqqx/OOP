class Product:
    def __init__(self):
        self.name = ""
        self.price = 0


class ProductA(Product):
    def __init__(self):
        super().__init__()
        self.name = "ProductA"
        self.price = 10


class ProductB(Product):
    def __init__(self):
        super().__init__()
        self.name = "ProductB"
        self.price = 20


class Factory:
    def create_product(self, product_type):
        pass


class ConcreteFactory(Factory):
    def create_product(self, product_type):
        if product_type == "A":
            return ProductA()
        elif product_type == "B":
            return ProductB()
        else:
            return None


if __name__ == "__main__":
    factory = ConcreteFactory()

    productA = factory.create_product("A")
    productB = factory.create_product("B")

    if productA.price != productB.price:
        print("Factory Method works, variables contain different values.")
    else:
        print("Factory Method failed, both variables contain same value.")
