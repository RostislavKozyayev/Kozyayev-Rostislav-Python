# Создайте базовый класс "Форма" со свойствами "цвет" и "тип".
# От этого класса унаследуйте класс "Круг" и добавьте в него свойство "радиус".
# Определите методы вычисления площади и периметра.

from math import pi

# Создание базового класса "Форма"
class Shape:
    def __init__(self, color, shape_type):
        self.color = color
        self.shape_type = shape_type

# Создание класса "Круг" с унаследованными атрибутами
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color, "Круг")
        self.radius = radius

    def area(self):
        print(f"Площадь данного круга равна: {pi * self.radius ** 2} см")

    def perimetr(self):
        print(f"Периметр данного круга равен: {2 * pi * self.radius} см")

# Создание объекта и использование методов (Радиус задаётся в см)
circle1 = Circle("Жёлтый", 20)
circle1.area()
circle1.perimetr()