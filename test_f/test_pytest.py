

from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle


class TestRunPerimeter:
    def test_triangle_perimeter(self):
        triangle = Triangle(13, 14, 15)
        assert triangle.perimeter == 42

    def test_rectangle_perimeter(self):
        rectangle = Rectangle(10, 20)
        assert rectangle.perimeter == 30

    def test_square_perimeter(self):
        square = Square(10)
        assert square.perimeter == 40

    def test_circle_perimeter(self):
        circle = Circle(5)
        assert circle.perimeter == 31.4

    def test_triangle_area(self):
        triangle = Triangle(13, 14, 15)
        assert triangle.area == 84


class TestRunArea:

    def test_rectangle_area(self):
        rectangle = Rectangle(10, 20)
        assert rectangle.area == 200

    def test_square_area(self):
        square = Square(10)
        assert square.area == 100

    def test_circle_area(self):
        circle = Circle(5)
        assert circle.area == 78.5
