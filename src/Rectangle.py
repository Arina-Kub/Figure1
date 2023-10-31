

from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, a: float, b: float):
        super().__init__("Rectangle")
        if a <= 0 or b <= 0:
            raise ValueError("figure must be a Figure instance")
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return self.a + self.b


