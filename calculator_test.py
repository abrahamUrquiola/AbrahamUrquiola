import unittest
from src.calculator import Calculator

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        cal = Calculator()
        result = cal.add(2, 2)
        self.assertEqual(4, result)

    def test_validate_age(self):
        cal = Calculator()
        result = cal.valid_age(5)
        self.assertTrue(result)

    def test_validate_invalid_age(self):
        cal = Calculator()
        result = cal.valid_age(-5)
        self.assertFalse(result)

    def test_max(self):
        cal = Calculator()
        result = cal.max(2, 8, 19)
        self.assertEqual(19, result)

    def test_validate_vocal(self):
        cal = Calculator()
        result = cal.isVocal('a')
        self.assertEqual('is vocal', result)

    def test_validate_consonant(self):
        cal = Calculator()
        result = cal.isVocal('f')
        self.assertEqual('is consonant', result)

    def test_validate_number(self):
        cal = Calculator()
        result = cal.isVocal(5)
        self.assertEqual('is number', result)

    def test_reverse(self):
        cal = Calculator()
        result = cal.inversa('string')
        self.assertEqual('gnirts', result)

    def test_validate_isPalindromo(self):
        cal = Calculator()
        result = cal.palindromo('oruro')
        self.assertTrue(result)

    def test_validate_isNotPalindromo(self):
        cal = Calculator()
        result = cal.palindromo('juan')
        self.assertFalse(result)

    def test_mayor_menor_promedio(self):
        cal = Calculator()
        result = cal.mayMenProm([8, 5, 4, 12, 6, 1])
        self.assertEqual('12 1 6', result)


    def test_binario(self):
        cal = Calculator()
        result = cal.convertBinary(10)
        self.assertEqual('1010', result)

    def test_totalCaracteres(self):
        cal = Calculator()
        result = cal.totalCaracteres('maria tiene un corderito')
        self.assertEqual(24, result)
