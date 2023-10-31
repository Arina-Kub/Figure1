

class Figure:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("This method must be implemented in subclass")

    def perimeter(self):
        raise NotImplementedError("This method must be implemented in subclass")

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("figure must be a Figure instance")
        return self.area + figure.area


