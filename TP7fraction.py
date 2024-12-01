# Mayala-Luneko Loyde

import math

class Fraction:

    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : 
        - num et den sont des entiers
        - den !=0, il est non null 

        POST : retourne la fraction à son état simple et sous forme irreductible :
        - Le numérateur et le dénominateur sont divisés par leur plus grand commun diviseur (GCD).
        - Si le dénominateur est négatif, le signe est transféré au numérateur.
        """
    
        if den == 0: 
            raise TypeError("The denomnator can't be zero") 
        gcd = math.gcd(num, den)# pour avoir un entier 
        self.num = num // gcd 
        self.den = den // gcd 
        
        if self.den < 0 :
            self.num = -self.num
            self.den = -self.den  # on rend le dénominateur posiitf 
            
    @property
    def numerator(self):
        return self.num
    
    @property
    def denominator(self):
        return self.den 

        
# ------------------ Textual representations ------------------

    def __str__(self) :
        """Return a textual representation of the reduced form of the fraction

        PRE : 
        - num et den doivent être des nombres entiers 
        - den != 0

        POST : retourne la fraction sous cette forme : "num/den" où "num" est le numérateur et "den" est le dénominateur
        """
        return f"{self.num}/{self.den}"

    def as_mixed_number(self) :
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE :
        - num et den doivent être des entiers.
        - den != 0.

        POST : Retourne la fraction sous forme de nombre mixte :
        - Si la fraction est un entier, retourne la fraction comme une chaine.
        - Si la fraction n'est pas un entier, retourne la fraction dans une représentation sous forme de 
        nombre mixte, c'est-à-dire un entier (donc la partie entière) et la fraction restante
        -  Si la fraction est négative, retourne le nombre mixte avec le signe négatif appliqué.
        - La fraction retournée est toujours sous sa forme réduite
        """

        if self.num % self.den == 0:  # Si la fraction est un entier
            return str(self.num // self.den)
    
    # Calculer la partie entière et le reste
        abs_num = abs(self.num)  # Valeur absolue du numérateur
        fraction_entier = abs_num // self.den
        le_reste = abs_num % self.den

        if self.num < 0:  # Si la fraction est négative
            return f"-{fraction_entier} {le_reste}/{self.den}"
        else:
            return f"{fraction_entier} {le_reste}/{self.den}"

    
# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : 
         - num et den doivent être des entiers 
         - den ! = 0
         - other.den != 0
         POST : Retourne une fraction qui est le resultat d'une addition entre fraction 
         """
        if not isinstance(other, Fraction) :
            raise TypeError("ça doit être une fraction ") # on vérifie si other est un descendant / une instance de Fraction 
        add_numerator = self.num*other.den + self.den*other.num
        add_denominator = self.den*other.den 
        return Fraction(add_numerator, add_denominator)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : 
        - num et den doivent être des entiers 
        - den ! = 0
        - other.den != 0
        POST : Retourne une fraction qui est le résultat d'une soustraction entre fraction
        """
        if not isinstance(other, Fraction) :
            raise TypeError("Ce n'est pas une instance de la classe Fraction ")
        sub_numerator = self.num*other.den - self.den*other.num 
        sub_denominator = self.den*other.den 
        return Fraction(sub_numerator, sub_denominator)
        


    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : 
        - num et den doivent être des entiers 
        - den != 0 
        - other.den != 0
        POST : Retourne une fraction qui est le resultat d'une multiplication entre fraction 
        """
        if not isinstance(other, Fraction) : 
            raise TypeError("Ce n'est pas une instance de la classe Fraction ")
        mul_numerator = self.num * other.num 
        mul_denominator = self.den * other.den 
        return  Fraction(mul_numerator, mul_denominator)
        


    def __truediv__(self, other):# à revoir 
        """Overloading of the / operator for fractions

        PRE : 
        - num et den doivent être des entiers 
        - den != 0 
        other.den != 0 (il ne peut pas avoir de division par 0)
        POST : Retourne une fraction qui est le resultat d'une division entre fraction 
        """
        if not isinstance(other, Fraction) :
            raise TypeError("Ce n'est pas une instance de la classe Fraction ")
        if other.num == 0: 
            raise ZeroDivisionError("Division par uen fraction nulle ")    
        
        truediv_numerator =  self.num * other.den
        truediv_denominator = self.den * other.num 
        return Fraction(truediv_numerator, truediv_denominator)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions.

        PRE : "other" doit être un entier (exposant) 
        POST : Retourne une fraction qui est le resultat de la puissance entre fraction de l'exposant "other".
        """ 
        if not isinstance(other, int):  
            raise TypeError("L'exposant doit être un entier")
        
        if other < 0 :
            new_num = self.den ** abs(other) # on inverse les roles : le numérateur devient le dénominateur de la fraction, élevée à la puissance 
            new_den = self.num ** abs(other) # idem, le dénominateur devient le numérateur de fraction élevée à la puissance
        else : 
            new_num = self.num ** other
            new_den = self.den ** other

        gcd = math.gcd(new_num, new_den) # pour simplification de la fraction 
        new_num //= gcd 
        new_den //= gcd
        return Fraction(new_num, new_den)
        

    def __eq__(self, other) : 
        """Overloading of the == operator for fractions
        
        PRE : 
        -"other" doit être une une instance de la classe Fraction
        - other.den != 0 

        POST : Retourne True si les fractions son égale, si ce n'est pas le cas ça retourne False
        
        """
        if not isinstance(other, Fraction):
            raise TypeError("Les objets doivent être des instances de la classe Fraction")
        return self.num * other.den == self.den * other.num 
        
    def __float__(self) :
        """Returns the decimal value of the fraction

        PRE : 
        - num et den doivent être des entiers 
        - den != 0 
        
        POST : 
        Retourne la valeur decimale de la fractions sous forme de nombre flottant 
        """
        return round(self.num / self.den,3)
        
    
# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)



# ------------------ Properties checking  ------------------

    def is_zero(self):
        """
        PRE : - num et den sont des entiers
               - den != 0
        POST : - Retourne True si la fraction est égale à zéro, sinon retourne False.
        """
        return self.num == 0  # si le num est égale à 0 alors la fraction vaut 0
        


    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)
        
        PRE : 
        - num et den sont des entiers 
        - den != 0 
        POST : Retourne True si la fraction est un entier, sinon ça retourne False. 
        """
        return self.num % self.den == 0 
        

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE :
        - num et den sont des entiers 
        - den != 0 
        POST : Retourne True si la valeur absolue de la fraction est inférieur à 1, sinon ça retourne False 
        """
        return abs(self.num) <  abs(self.den) 

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : 
        - num et den sont des entiers 
        - den != 0 
        POST : - Retourne True si le numérateur est 1 dans la forme réduite de la fraction, sinon retourne False.
        """
        return self.num == 1

    def is_adjacent_to(self, other) : 
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE :
        - others doit etre une instance de la classe Fraction 
        - den != 0 

        POST : Retourne True si la fraction est adjacente, sinon ça renvoie False 
        """
        diff_num = abs(self.num*other.den-other.num*self.den)
        return diff_num == 1  
