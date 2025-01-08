import unittest
from main import calculate

class TestCalculator(unittest.TestCase):
    """Класс для тестирования функций текстового калькулятора."""

    def test_addition(self):
        """Тест на сложение."""
        self.assertEqual(calculate("два плюс два"), 4)
        self.assertEqual(calculate("десять плюс двадцать"), 30)

    def test_subtraction(self):
        """Тест на вычитание."""
        self.assertEqual(calculate("пять минус два"), 3)
        self.assertEqual(calculate("двадцать минус десять"), 10)

    def test_multiplication(self):
        """Тест на умножение."""
        self.assertEqual(calculate("три умножить на пять"), 15)
        self.assertEqual(calculate("шесть умножить на четыре"), 24)

    def test_division(self):
        """Тест на деление."""
        self.assertEqual(calculate("десять поделить на два"), 5)
        self.assertEqual(calculate("двадцать поделить на четыре"), 5)

    def test_negative_numbers(self):
        """Тест на отрицательные числа."""
        self.assertEqual(calculate("минус три плюс пять"), 2)
        self.assertEqual(calculate("минус десять умножить на два"), -20)

    def test_complex_expression(self):
        """Тест на сложные выражения с несколькими операциями."""
        self.assertEqual(calculate("три плюс два умножить на четыре"), 20)
        self.assertEqual(calculate("двадцать минус десять поделить на два"), 5)

    def test_division_by_zero(self):
        """Тест на деление на ноль."""
        with self.assertRaises(ZeroDivisionError):
            calculate("два поделить на ноль")


if __name__ == "__main__":
    unittest.main()
