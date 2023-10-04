#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Pair:
    """
    Класс, хранящий введенные коэффициенты A и B в полях first и second
    """

    def __init__(self, first, second):
        """
        Конструктор класса, принимает два параметра, валидирует их и сохраняет в поля
        """
        # Проверка, является ли first(A) дробным числом
        if not isinstance(first, float):
            raise TypeError("Значение first должно быть дробным числом")

        # Проверка, является ли second(B) дробным числом
        if not isinstance(second, float):
            raise TypeError("Значение second должно быть дробным числом")

        # Проверка, не равен ли second(A) нулю
        if first == 0:
            raise ValueError("Параметр A не должен быть равен нулю")

        # Записываем значения в поля
        self.first = first
        self.second = second

    def SolLinEqu(self):
        """
        Вычисляется значение линейного уравнения, с использованием переданных в конструктор параметров
        """
        return (self.second * -1.0)/self.first

    def Display(self):
        """
        Метод выводит на консоль линейное уравнение вида Ax+B с подставленными параметрами
        """
        print(f"(y = {self.first}x + {self.second})")

    @classmethod
    def Read(cls):
        """
        Статичный метод для создания экземпляра класса
        """
        a = float(input("Введите коэффициент A: "))
        b = float(input("Введите коэффициент B: "))

        return cls(a, b)


if __name__ == '__main__':
    # Создаем экземпляр класса
    pair = Pair.Read()
    # Отображаем уравнение
    pair.Display()
    # Выводим посчитанное результат вычисления
    print(pair.SolLinEqu())
