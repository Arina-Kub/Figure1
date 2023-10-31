

from src.Figure import Figure


class Square(Figure):
    def __init__(self, a):
        super().__init__("Square")
        if a <= 0:
            raise ValueError("figure must be a Figure instance")
        self.a = a

    def area(self):
        return self.a ** 2

    def perimeter(self):
        return self.a * 4
