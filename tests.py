import unittest
from calculating_the_area import ShapeCalculator


class TestShapeCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ShapeCalculator()

    def test_circle_area(self):
        self.assertAlmostEqual(
            self.calculator.circle_area(3), 28.2743, places=4
        )
    
    def test_triangle_area(self):
        self.assertAlmostEqual(self.calculator.triangle_area(3, 4, 5), 6)
    
    def test_is_right_triangle(self):
        self.assertTrue(self.calculator.is_right_triangle(3, 4, 5))
        self.assertFalse(self.calculator.is_right_triangle(1, 2, 3))


if __name__ == "__main__":
    unittest.main()
