import math


class ShapeCalculator:
    """Declaring a class for calculating the area of shapes"""

    def __init__(self):
        """
        Class constructor, if you need to find the area of a shape other than
        a circle and a triangle, then you can declare the shape parameters here
        """
        pass

    def circle_area(self, radius):
        """Calculation of the area of a circle"""

        return math.pi * radius**2

    def triangle_area(self, side1, side2, side3):
        """Calculating the area of a triangle using Heron's formula"""

        half_meter = (side1 + side2 + side3) / 2
        return math.sqrt(
            half_meter
            * (half_meter - side1)
            * (half_meter - side2)
            * (half_meter - side3)
        )

    def is_right_triangle(self, side1, side2, side3):
        """
        Checking that the triangle is rectangular using the equality
        of the squares of the legs and the square of the hypotenuse
        """

        sides = [side1, side2, side3]
        hypotenuse = max(sides)
        sides.remove(hypotenuse)
        return math.isclose(hypotenuse**2, sides[0] ** 2 + sides[1] ** 2)
