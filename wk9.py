import unittest
from wk9 import roman_to_int

class TestRomanToInt(unittest.TestCase):

    def test_valid_uppercase_roman_numerals(self):
        self.assertEqual(roman_to_int("I"), 1)
        self.assertEqual(roman_to_int("IV"), 4)
        self.assertEqual(roman_to_int("IX"), 9)
        self.assertEqual(roman_to_int("XII"), 12)
        self.assertEqual(roman_to_int("XXI"), 21)
        self.assertEqual(roman_to_int("XLII"), 42)
        self.assertEqual(roman_to_int("LX"), 60)
        self.assertEqual(roman_to_int("XC"), 90)
        self.assertEqual(roman_to_int("CXX"), 120)
        self.assertEqual(roman_to_int("CD"), 400)
        self.assertEqual(roman_to_int("DCCC"), 800)
        self.assertEqual(roman_to_int("CM"), 900)
        self.assertEqual(roman_to_int("MCMXCIV"), 1994)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            roman_to_int("ZSW")
        # Add more invalid input test cases here

if __name__ == "__main":
    unittest.main()
