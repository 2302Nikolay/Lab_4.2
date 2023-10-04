class LinearEquation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def root(self):
        if self.a != 0:
            x = -self.b / self.a
            return x
        else:
            raise ValueError("Уравнение не является линейным")


# Пример использования
if __name__ == "__main__":
    equation1 = LinearEquation(5, 10)
    root1 = equation1.root()
    print(f"Корень уравнения: {root1}")

    equation2 = LinearEquation(0, 7)
    try:
        root2 = equation2.root()
        print(f"Корень уравнения: {root2}")
    except ValueError as error:
        print(error)
