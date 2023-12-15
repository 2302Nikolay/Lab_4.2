#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Во всех заданиях обязательно должны присутствовать:
- метод инициализации __init__ , метод должен контролировать значения аргументов на корректность;
- ввод с клавиатуры read;
- вывод на экран display .
11. Линейное уравнение . Поле first — дробное число, коэффициент ; поле
second — дробное число, коэффициент . Реализовать метод вычисления корня
линейного уравнения. Метод должен проверять неравенство коэффициента нулю.
Решить задачу максимально задействовав перегрузки операторов.
"""


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

    def sol_lin_equ(self):
        """
        Вычисляется значение линейного уравнения, с использованием переданных в конструктор параметров
        """
        return (self.second * -1.0) / self.first

    def display(self):
        """
        Метод выводит на консоль линейное уравнение вида Ax+B с подставленными параметрами
        """
        print(f"(y = {self.first}x + {self.second})")

    @classmethod
    def read(cls):
        """
        Статичный метод для создания экземпляра класса
        """
        a = float(input("Введите коэффициент A: "))
        b = float(input("Введите коэффициент B: "))

        return cls(a, b)

    def __eq__(self, other):
        return self.sol_lin_equ() == other.sol_lin_equ()

    def __ne__(self, other):
        return self.sol_lin_equ() != other.sol_lin_equ()

    def __add__(self, other):
        self.sol_lin_equ() + other.sol_lin_equ()

    def __sub__(self, other):
        return self.sol_lin_equ() - other.sol_lin_equ()

    def __truediv__(self, other):
        return self.sol_lin_equ() / other.sol_lin_equ()


if __name__ == "__main__":
    pair = Pair.read()
    pair2 = Pair(5.2, 10.4)
    pair.display()
    pair2.display()
    print(pair.sol_lin_equ())
    print(pair2.sol_lin_equ())
    # Перегрузка оператора ==
    print(pair == pair2)
    # Перегрузка оператора !=
    print(pair != pair2)
    # Перегрузка оператора +
    print(pair + pair2)
    # Перегрузка оператора -
    print(pair - pair2)
    # Перегрузка оператора
    print(pair / pair2)
