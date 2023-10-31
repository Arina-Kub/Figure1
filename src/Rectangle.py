

from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__("Rectangle")
        if not self.is_valid(a, b):
            raise ValueError("figure must be a Figure instance")
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return self.a + self.b
