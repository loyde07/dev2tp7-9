# Mayala-Luneko Loyde 

import unittest
from TP7fraction import Fraction

class TestFraction(unittest.TestCase):

    def test_init(self):
        f= Fraction(1,2) # initialisation de fraction 
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)

        f = Fraction(6, 8) # simplification irréductibles des fractions 
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4) 

        f = Fraction(-4, 6) # le numérateur négatif 
        self.assertEqual(f.numerator, -2)
        self.assertEqual(f.denominator, 3)

        f = Fraction(1, -3) # le cas du dénominateur négatif 
        self.assertEqual(f.numerator, -1)
        self.assertEqual(f.denominator, 3)

        f = Fraction(-5, -10) # les deux argurments sont négatifs 
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)

        f = Fraction(0, 5) # le numérateur est nul 
        self.assertEqual(f.numerator, 0)
        self.assertEqual(f.denominator, 1)

        f = Fraction(7, 1) # le dénominateur est égal à 1
        self.assertEqual(f.numerator, 7)
        self.assertEqual(f.denominator, 1)


        with self.assertRaises(ValueError): # fraction dont le dénumérateur est égale à 0
            Fraction(1, 0)
        with self.assertRaises(TypeError): # fraction dont le dénominateur est une chaine de caractère (donc c'est un nom entier)
            Fraction(1, "2")
        with self.assertRaises(TypeError):  # fraction dont le numérateur est un nombre flottant (donc c'est un non entier)
            Fraction(2.5, 3)  

    def test_str(self):
        f = Fraction(3, 4)
        self.assertEqual(str(f), "3/4")

        f= Fraction(5,2)
        self.assertEqual(str(f), "5/2")

        f= Fraction(-3, 4)
        self.assertEqual(str(f), "-3/4")

        f= Fraction(1, -2)
        self.assertEqual(str(f), "-1/2")

        f= Fraction(0, 5)
        self.assertEqual(str(f), "0/1")

        f = Fraction(-10, 5)
        self.assertEqual(str(f), "-2/1")

        f9 = Fraction(7, 7)
        self.assertEqual(str(f9), "1/1")

        f = Fraction(9, 4)
        self.assertEqual(str(f), "9/4")

        f = Fraction(3, 1) 
        self.assertEqual(str(f), "3/1")


    def test_add(self):
        f1 = Fraction(2, 3) # les deux fractions positives 
        f2 = Fraction(3, 4)
        self.assertEqual(f1 + f2, Fraction(17, 12)) # donc 17/12

        f1 = Fraction(-2, 3) # une seul fraction négatives 
        f2 = Fraction(1, 6)
        self.assertEqual(f1 + f2, Fraction(-1, 2))

        f1 = Fraction(-1, 2) # les deux fractions négatives 
        f2 = Fraction(-1, 3)
        self.assertEqual(f1 + f2, Fraction(-5, 6))

        f1 = Fraction(3, 7) # addition de fractions dont l'une à un numérateur égale à 0
        f2 = Fraction(0, 1)
        self.assertEqual(f1 + f2, Fraction(3, 7))

        f1 = Fraction(-2, -4) # tous les arguments sont négatifs
        f2 = Fraction(-2, -4)
        self.assertEqual(f1 + f2, Fraction(1, 1))
        
        f1 = Fraction(3, -4)  # fraction avec un dénominateur négatif
        f2 = Fraction(5, 4)
        self.assertEqual(f1 + f2, Fraction(1, 2))

        with self.assertRaises(ValueError):  # addition de fractions dont l'une à un dénominateur égale à 0 
            f1 = Fraction(2, 6)
            f2 = Fraction(1, 0)  
            f1 + f2 # comment régler ce souci ? => test coverage
        with self.assertRaises(TypeError): # addition avec un type non fraction 
            Fraction(1, 2) + "pas une fraction"

    def test_sub(self):
        f1 = Fraction(2, 3) # deux fractions positives 
        f2 = Fraction(3, 4)
        self.assertEqual(f1 - f2, Fraction(-1, 12)) 

        f1 = Fraction(-3, 4) # une fraction est négative 
        f2 = Fraction(1, 4)
        self.assertEqual(f1 - f2, Fraction(-1, 1))

        f1 = Fraction(-3, 5) # deux fractions négative 
        f2 = Fraction(-2, 5)
        self.assertEqual(f1 - f2, Fraction(-1, 5))

        f1 = Fraction(0, 7) # soustraction de fractions dont l'une à un numérateur égale à 0
        f2 = Fraction(2, 1)
        self.assertEqual(f1 - f2, Fraction(-2, 1))

        f1 = Fraction(3, 5)  # soustraction dont la deuxième fraction est négative 
        f2 = Fraction(-2, 5) 
        self.assertEqual(f1 - f2, Fraction(5, 5))

        f1 = Fraction(1, 3)  # soustraction avec des fractions inférieures à 1 
        f2 = Fraction(1, 4)  
        self.assertEqual(f1 - f2, Fraction(1, 12))

         
        f1 = Fraction(5, 4)  # soustractions avec des fractions supérieures à 1
        f2 = Fraction(3, 4)  
        self.assertEqual(f1 - f2, Fraction(2, 4))  # donc 1/2

        with self.assertRaises(ValueError) :  # soustraction de fractions dont l'une à un dénominateur égale à 0 
            f1 = Fraction(8,6)
            f2 = Fraction(2,0)
            f1 - f2 # comment régler ce problème ? => test coverage
        with self.assertRaises(TypeError):  # Soustraction avec un type non fraction
            Fraction(5,2) - "pas une fraction"

    def test_mul(self): # deux fractions positives
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        self.assertEqual(f1 * f2, Fraction(1, 2))

        f1 = Fraction(-2, 3)  # une fraction négative
        f2 = Fraction(3, 4)
        self.assertEqual(f1 * f2, Fraction(-1, 2))

        f1 = Fraction(-5, 8)  # deux fractions négatives
        f2 = Fraction(-7, 9)
        self.assertEqual(f1 * f2, Fraction(35, 72))

        f1 = Fraction(0, 1)  # multiplication avec une fraction nulle
        f2 = Fraction(11, 12)
        self.assertEqual(f1 * f2, Fraction(0, 1))  # donc 0

        f1 = Fraction(3, 3)  # multiplication avec une fraction égale à 1
        f2 = Fraction(8, 7)
        self.assertEqual(f1 * f2, Fraction(8, 7))  # donc 8/7

        f1 = Fraction(-1, -5)  
        f2 = Fraction(3, -2)  
        self.assertEqual(f1 * f2, Fraction(-3, 10))

        with self.assertRaises(TypeError):  # multiplication avec un type non fraction
            Fraction(5,6) * "pas une fraction"


    def test_div(self): # deux fractions positives
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        self.assertEqual(f1 / f2, Fraction(8, 9)) # donc 8/9 

        f1 = Fraction(-9, 16)  # une fraction négative
        f2 = Fraction(3, 4)
        self.assertEqual(f1 / f2, Fraction(-3, 4))  # donc -3/4

        f1 = Fraction(-9, 16)  # deux fractions négatives
        f2 = Fraction(-3, 4)
        self.assertEqual(f1 / f2, Fraction(3, 4))  # donc 3/4

        f1 = Fraction(0, 1)  # division avec une fraction nulle
        f2 = Fraction(5, 7)
        self.assertEqual(f1 / f2, Fraction(0, 1))  # donc 0

        f1 = Fraction(5, 6)  # divison avec des fractions inférieures à 1
        f2 = Fraction(2, 3)  
        self.assertEqual(f1 / f2, Fraction(5, 4))  # donc 5/4

        f1 = Fraction(15, 7)  # fraction supérieure à 1
        f2 = Fraction(5, 4)
        self.assertEqual(f1 / f2, Fraction(60, 35))  # donc 60/35

        with self.assertRaises(ZeroDivisionError):
            Fraction(2,3) / Fraction(0, 1)
        with self.assertRaises(TypeError):
            Fraction(2,3) / "pas une fraction"

    def test_as_mixed_number(self):
        f = Fraction(9, 4) # fraction plus grande que 1 
        self.assertEqual(f.as_mixed_number(), "2 1/4")

        f = Fraction(8, 4) # fraction entière
        self.assertEqual(f.as_mixed_number(), "2")

        f= Fraction(64,12)
        self.assertEqual(f.as_mixed_number(), "5 1/3")

        f = Fraction(-16, 5) # fraction avec un numérateur négatif 
        self.assertEqual(f.as_mixed_number(), "-3 1/5")

        f = Fraction(16, -5)  # fraction avec le dénominateur négatif
        self.assertEqual(f.as_mixed_number(), "-3 1/5")

        f = Fraction(5, 8)  # fraction inférieure à 1
        self.assertEqual(f.as_mixed_number(), "5/8")

        f = Fraction(4, 4)  # fraction égale à 1
        self.assertEqual(f.as_mixed_number(), "1")
              

    def test_pow(self):
        f = Fraction(5, 7) # fraction positive 
        self.assertEqual(f**3, Fraction(125, 343)) # avec exposant positif 
        self.assertEqual(f**-2, Fraction(49, 25)) # avec exposant négatif

        f = Fraction(0, 5)  # fraction nulle
        self.assertEqual(f**3, Fraction(0, 1)) # 0 

        f = Fraction(7, 3)  # 
        self.assertEqual(f**0, Fraction(1, 1)) # avec exposant égale à 0 ( = 1)

        f = Fraction(0, 5)  # fraction nulle
        self.assertEqual(f**3, Fraction(0, 1))

        f = Fraction(11, 8)  
        self.assertEqual(f**-1, Fraction(8, 11)) # exposant égale à 1 donc inversion de fraction 

        with self.assertRaises(TypeError):
            Fraction(5,7) ** 1.5
        with self.assertRaises(TypeError) : 
            Fraction(5,7)** "pas un entier"


    def test_eq(self):
        self.assertTrue(Fraction(3, -6) == Fraction(-1, 2))
        self.assertTrue(Fraction(6, 9) == Fraction(2, 3)) 
        self.assertFalse(Fraction(0, 5) == Fraction(7, 4))
        self.assertFalse(Fraction(5, -7) == Fraction(7, -10))

        with self.assertRaises(TypeError):
            Fraction(3,4) == "pas une fraction"



    def test_is_integer(self):
        self.assertTrue(Fraction(-8, 4).is_integer()) 
        self.assertTrue(Fraction(50, 10).is_integer()) 
        self.assertFalse(Fraction(25, -7).is_integer()) 
        self.assertFalse(Fraction(10, 3).is_integer()) 


    def test_float(self):
        self.assertEqual(float(Fraction(1, 2)), 0.5)
        self.assertEqual(float(Fraction(-3, 8)), -0.375)
        self.assertEqual(float(Fraction(5, 4)), 1.25)
        self.assertEqual(float(Fraction(-7, -2)), 3.5)
        

    def test_is_proper(self):
        self.assertTrue(Fraction(3, 4).is_proper())
        self.assertTrue(Fraction(-1, 3).is_proper())
        self.assertFalse(Fraction(4, 3).is_proper())


    def test_is_zero(self):
        self.assertTrue(Fraction(0, 1).is_zero())
        self.assertTrue(Fraction(0, -5).is_zero())
        self.assertFalse(Fraction(15, 8).is_zero())
        self.assertFalse(Fraction(7, -8).is_zero())


    def test_is_unit(self):
        self.assertTrue(Fraction(1, 7).is_unit())
        self.assertFalse(Fraction(2, 3).is_unit())
        self.assertTrue(Fraction(1, 1).is_unit())
        self.assertFalse(Fraction(2, -7).is_unit())

    def test_is_adjacent_to(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        self.assertTrue(f1.is_adjacent_to(f2))

        f3 = Fraction(3,4)
        f4 = Fraction(5,6)
        self.assertFalse(f3.is_adjacent_to(f4))

        f5 = Fraction(-3, 10)
        f6 = Fraction(-4, 9)
        self.assertFalse(f5.is_adjacent_to(f6))

        with self.assertRaises(TypeError):  # Test avec un type incorrect (non fraction)
            f1.is_adjacent_to("pas une fraction")


if __name__ == "__main__":
    unittest.main()
