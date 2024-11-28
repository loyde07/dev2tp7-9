# Mayala-Luneko Loyde 

import unittest
from TP7fraction import Fraction

class TestFraction(unittest.TestCase):

    def test_init(self):
        f= Fraction(1,2)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)
        f = Fraction(6, 8)
        self.assertEqual(f.numerator, 3) # simplification du numérateur
        self.assertEqual(f.denominator, 4) # simplification du dénominateur 

        f = Fraction(-4, 6)
        self.assertEqual(f.numerator, -2)
        self.assertEqual(f.denominator, 3)

        f = Fraction(1, -3)
        self.assertEqual(f.numerator, -1)
        self.assertEqual(f.denominator, 3)

        f = Fraction(-5, -10)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)

        with self.assertRaises(ValueError): # le dénominateur ne peut pas être 0
            Fraction(1, 0)

        with self.assertRaises(TypeError):
            Fraction(1, "2")

    def test_str(self):
        f = Fraction(3, 4)
        self.assertEqual(str(f), "3/4")

        f= Fraction(5,2)
        self.assertEqual(str(f), "5/2")

    def test_add(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        self.assertEqual(f1 + f2, Fraction(17, 12)) # donc 17/12
 
        with self.assertRaises(TypeError):
            Fraction(1, 2) + "not a fraction"

    def test_sub(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        self.assertEqual(f1 - f2, Fraction(-1, 12)) # donc -1/12

    def test_mul(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        self.assertEqual(f1 * f2, Fraction(1, 2))

    def test_div(self):
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        self.assertEqual(f1 / f2, Fraction(8, 9)) # donc 8/9 

        with self.assertRaises(ZeroDivisionError):
            f1 / Fraction(0, 1)

        with self.assertRaises(TypeError):
            f1 / "not a fraction"

    def test_as_mixed_number(self):
        f = Fraction(7, 3)
        self.assertEqual(f.as_mixed_number(), "2 1/3")

        f = Fraction(8, 4)
        self.assertEqual(f.as_mixed_number(), "2")

        f= Fraction(64,12)
        self.assertEqual(f.as_mixed_number(), "5 1/3")

        f = Fraction(-7, 3)
        self.assertEqual(f.as_mixed_number(), "-2 1/3")
       

    def test_pow(self):
        f = Fraction(5, 7)
        self.assertEqual(f**3, Fraction(125, 343))
        self.assertEqual(f**-2, Fraction(49, 25))

        with self.assertRaises(TypeError):
            f ** 1.5


    def test_eq(self):
        self.assertTrue(Fraction(3, 6) == Fraction(1, 2))
        self.assertFalse(Fraction(3, 6) == Fraction(3, 4))

    def test_is_integer(self):
        self.assertTrue(Fraction(8, 4).is_integer()) 
        self.assertFalse(Fraction(10, 3).is_integer()) 

        self.assertTrue(Fraction(50, 10).is_integer()) 
        self.assertFalse(Fraction(25, 7).is_integer()) 

    def test_float(self):
        self.assertEqual(float(Fraction(1, 2)), 0.5)
        self.assertEqual(float(Fraction(5, 4)), 1.25)
        

    def test_is_proper(self):
        self.assertTrue(Fraction(3, 4).is_proper())
        self.assertFalse(Fraction(4, 3).is_proper())



    def test_is_zero(self):
        self.assertTrue(Fraction(0, 1).is_zero())
        self.assertFalse(Fraction(15, 8).is_zero())


    def test_is_unit(self):
        self.assertTrue(Fraction(1, 7).is_unit())
        self.assertFalse(Fraction(2, 3).is_unit())

    def test_is_adjacent_to(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        self.assertTrue(f1.is_adjacent_to(f2))

        f3 = Fraction(3,4)
        f4 = Fraction(5,6)
        self.assertFalse(f3.is_adjacent_to(f4))


if __name__ == "__main__":
    unittest.main()
