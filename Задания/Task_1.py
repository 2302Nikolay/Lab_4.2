#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    @classmethod
    def read(cls):
        line = input("Введите коэффициент А (Пример: 2/3): ")
        line2 = input("Введите коэффициент В (Пример: 2/3): ")

        parts = list(map(int, line.split("/", maxsplit=1)))
        parts2 = list(map(int, line2.split("/", maxsplit=1)))

        if parts[1] == 0 and parts2[1] == 0:
            raise ValueError()

        return cls(parts, parts2)

    def display(self):
        print(
            f"Y = {self.first[0]}/{self.first[1]}*X + {self.second[0]}/{self.second[1]}"
        )

    def sol_lin_equ(self):
        return (
            (self.first[1] / self.first[0]) * -1.0 / (self.second[1] / self.second[0])
        )

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

    def __float__(self):
        self.first[0] /= self.first[1]
        self.second[0] /= self.second[1]
        return self


if __name__ == "__main__":
    pair = Pair.read()
    pair2 = Pair.read()
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
