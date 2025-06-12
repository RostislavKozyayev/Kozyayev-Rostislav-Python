# Создайте класс "Машина" с атрибутами "марка", "модель" и "год выпуска".
# Напишите метод, который выводит информацию о машине в формате
# "Марка: марка, Модель: модель, Год выпуска: год".

# Создание класса "Машина"
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year}")

# Создание объекта и использование метода
car1 = Car("Toyota", "Camry", 2020)
car1.display_info()