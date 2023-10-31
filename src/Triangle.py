

from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        if not self.is_valid(a, b, c):
            raise ValueError("figure must be a Figure instance")
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self, a, b, c):
        return (a + b > c) and (a + c > b) and (b + c > a)

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return s * (s - self.a) * (s - self.b) * (s - self.c) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c
