

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, r):
        super().__init__("Triangle")
        if r <= 0:
            raise ValueError("figure must be a Figure instance")
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

    def perimeter(self):
        return 2 * 3.14 * self.r
