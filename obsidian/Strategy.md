Паттерн проектирования Strategy - это шаблон, который позволяет легко заменять алгоритмы или стратегии для выполнения определенных операций в программе в зависимости от конкретной ситуации.

Примером использования паттерна может быть задача расчета стоимости доставки. Есть несколько методов расчета: один для расчета стоимости доставки внутри страны, другой для расчета стоимости доставки международной почтой. Вместо того, чтобы включать каждый метод внутрь класса, который обрабатывает доставку, мы можем реализовать паттерн Strategy.

Сначала мы создаем абстрактный класс или интерфейс для определения стратегий для вычисления стоимости доставки:

```py
class ShippingMethod:
    def calculate_cost(self, package):
        pass
```

Затем мы создаем классы-стратегии, которые реализуют этот интерфейс:

```py
class NationalShipping(ShippingMethod):
    def calculate_cost(self, package):
        #расчет стоимоти доставки по Национальному тарифу
        return cost

class InternationalShipping(ShippingMethod):
    def calculate_cost(self, package):
        #расчет стоимоти международной доставки
        return cost
```

Когда мы хотим использовать один из этих методов расчета, мы просто создаем экземпляр объекта соответствующей стратегии:

```py
national = NationalShipping()
international = InternationalShipping()
```

Затем мы можем вызвать функцию calculate_cost() этого объекта и выполнить необходимый расчет, при этом не заботясь о том, каким именно методом расчета мы пользуемся:

```py
national_cost = national.calculate_cost(package)
international_cost = international.calculate_cost(package)
```
Паттерн Strategy позволяет делегировать ответственность за выполнение определенного действия классам-стратегиям, что обеспечивает гибкость и расширяемость кода, а также уменьшает количество повторного кода. Он часто используется в объектно-ориентированных языках программирования, таких как Python, для реализации алгоритмов, которые могут меняться в зависимости от конкретных условий, например, в зависимости от типа входных данных или контекста выполнения программы.