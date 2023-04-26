# Суть
Строитель (Builder) - это пораждающий паттерн проектирования, который позволяет создавать комплексные объекты, разделяя процесс конструирования от представления объекта.
# Что решает
1. Проблему создания комплексных объектов с множеством полей и вложенных объектов
2. Упрощает логику констрокторов классо
Решается это путем вынесения конструирования объекта за пределы собственного класса в отдельные объекты, называемые строителями.
# Структура и пример кода
1. Сложный класс, экземпляры которого нужно создать.
2. Строители - объекты, которые заполняют разные поля и объекты внутри целевого экземпляра
3. Директор - определяет порядок вызова строительных шагов
В этом примере класс House представляет комплексный объект, который мы хотим создать с помощью паттерна Строитель. Класс Builder представляет интерфейс для создания объекта. Классы ConcreteBuilderWoodenHouse и ConcreteBuilderBrickHouse наследуются от класса Builder и реализуют методы для создания каждого типа дома.
```py
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
```
# Когда применять
1. Когда очень много перегрузок конструкрора или получается большое количество полей в конструкторе
2. Когда нужно создавать множество разных представлений объекта.
3. Когда нужно собирать очень сложные составные объекты.
# Плюсы и минусы
Плюсы
1. Пошаговое создание экземпляра
2. Переиспользование кода создания объекта
3. Изолирование сложного кода от его основной бизнесс-логики.
Минусы
1. Усложнение кода программы из-за введения новых классов.
2. Привязка к возможностям директоров строительства.
# Отношения с другими паттернами
1. Является более сложным преемником архитектуры [[Factory]]
2. Может быть реализован при помощи [[Singleton]]
