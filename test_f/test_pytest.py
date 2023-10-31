

from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle


def test_triangle_area():
    triangle = Triangle(13, 14, 15)
    assert triangle.area == 84


def test_triangle_perimeter():
    triangle = Triangle(13, 14, 15)
    assert triangle.perimeter == 42


def test_rectangle_area():
    rectangle = Rectangle(10, 20)
    assert rectangle.area == 200


def test_rectangle_perimeter():
    rectangle = Rectangle(10, 20)
    assert rectangle.perimeter == 30


def test_square_area():
    square = Square(10)
    assert square.area == 100


def test_square_perimeter():
    square = Square(10)
    assert square.perimeter == 40


def test_circle_area():
    circle = Circle(5)
    assert circle.area == 78.5


def test_circle_perimeter():
    circle = Circle(5)
    assert circle.perimeter == 31.4
