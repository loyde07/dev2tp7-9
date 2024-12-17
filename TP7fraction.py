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
        - den !=0 

        POST : retourne la fraction à son état simple et sous forme irreductible :
        - Le numérateur et le dénominateur sont divisés par leur plus grand commun diviseur (GCD).
        - Si le dénominateur est négatif, le signe est transféré au numérateur.

        RAISES : 
        - ValueError : si le dénominateur est nul 
        - TypeError : si les arguements ne sont pas des entiers 
        """

        if not isinstance(num, int) or not isinstance(den, int) : 
            raise TypeError("Le numérateur et le dénominateur doit être des entiers")
        if den == 0: 
            raise ValueError("Le dénominateur ne peut pas être zéro") 
        
        if num == 0 :
            den =1
        
        gcd = math.gcd(num, den)# pour avoir un entier      
        num = num // gcd 
        den = den // gcd 
        
        if den < 0 :
            num = -num
            den = -den  # on rend le dénominateur posiitf 
        
        self._num = num  # attribut privé
        self._den = den  # idem 
            
    @property
    def numerator(self):
        return self._num
    
    @property
    def denominator(self):
        return self._den 

        
# ------------------ Textual representations ------------------

    def __str__(self) :
        """Return a textual representation of the reduced form of the fraction

        PRE : -
        
        POST : retourne la fraction sous cette forme : "num/den" où "num" est le numérateur et "den" est le dénominateur
        """
        return f"{self._num}/{self._den}"

    def as_mixed_number(self) :
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : - 

        POST : Retourne la fraction sous forme de nombre mixte :
        - Si la fraction est un entier, retourne la fraction comme un entier .
        - Si la fraction n'est pas un entier, retourne la fraction dans une représentation sous forme de 
        nombre mixte, c'est-à-dire un entier (donc la partie entière) et la fraction restante
        - Si la fraction est négative, retourne le nombre mixte avec le signe négatif appliqué sur le nombre entier 
        - Si la fraction est négative avec une partie fractionnaire, le signe négatif est appliqué à la partie entière
        - Si la fraction n'a pas de partie fractionnaire (quand le reste = 0), seule la partie entière est retournée, avec ou sans signe selon le cas
        """

        if self.numerator % self.denominator == 0:  # Si la fraction est un entier
            return str(self.numerator // self.denominator)
    
    # Calculer la partie entière et le reste
        abs_num = abs(self.numerator)  # Valeur absolue du numérateur
        fraction_entiere = abs_num // self.denominator
        le_reste = abs_num % self.denominator

        if fraction_entiere == 0 and le_reste != 0:
            return f"{le_reste}/{self.denominator}"

        if self.numerator < 0:  # Si la fraction est négative
            return f"-{fraction_entiere} {le_reste}/{self.denominator}" if le_reste != 0 else f"-{fraction_entiere}"
        else:
            return f"{fraction_entiere} {le_reste}/{self.denominator}" if le_reste != 0 else f"{fraction_entiere}"

    
# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : "other" est une instance de Fraction 

         POST : Retourne une fraction qui est le resultat d'une addition entre fraction 
         
         RAISES : TypeError : si "other" n'est pas une instance de Fraction 
         """
        if not isinstance(other, Fraction) :
            raise TypeError("ça doit être une fraction ") # on vérifie si other est un descendant / une instance de Fraction 
        add_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        add_denominator = self.denominator * other.denominator
        return Fraction(add_numerator, add_denominator)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE :  
        - "other" doit être une instance de la classe Fraction
        - Le numérateur de `other` ne doit pas être égal à zéro (pour éviter la division par zéro)

        POST : Retourne une fraction qui est le résultat d'une soustraction entre fraction

        RAISES : TypeError : Si "other" n'est pas une instance de Fraction.
        """
        if not isinstance(other, Fraction) :
            raise TypeError("Ce n'est pas une instance de la classe Fraction ")
        sub_numerator = self.numerator * other.denominator - self.denominator * other.numerator 
        sub_denominator = self.denominator * other.denominator
        return Fraction(sub_numerator, sub_denominator)
        
        


    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : "other" doit être une instance de la classe Fraction.

        POST : Retourne une fraction qui est le resultat d'une multiplication entre fraction 
        
        RAISES : TypeError : Si "other" n'est pas une instance de Fraction.
        """
        if not isinstance(other, Fraction) : 
            raise TypeError("Ce n'est pas une instance de la classe Fraction ")
        mul_numerator = self.numerator * other.numerator
        mul_denominator = self.denominator * other.denominator
        return  Fraction(mul_numerator, mul_denominator)
        


    def __truediv__(self, other): 
        """Overloading of the / operator for fractions

        PRE : "other" doit être une instance de la classe Fraction.

        POST : Retourne une fraction qui est le resultat d'une division entre fraction 

        RAISES : 
        - TypeError : Si "other" n'est pas une instance de Fraction.
        - ZeroDivisionError : Si "other" est une fraction nulle.

        """
        if not isinstance(other, Fraction) :
            raise TypeError("Ce n'est pas une instance de la classe Fraction ")
        if other.numerator == 0: 
            raise ZeroDivisionError("La division par une fraction nulle n'est pas permise")    
        
        truediv_numerator =  self.numerator * other.denominator
        truediv_denominator = self.denominator * other.numerator 
        return Fraction(truediv_numerator, truediv_denominator)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions.

        PRE : "other" (exposant) doit être un entier

        POST : Retourne une fraction qui est le resultat de la puissance entre fraction de l'exposant "other".

        RAISES : TypeError : Si "other" n'est pas un entier.
        """ 
        if not isinstance(other, int):  
            raise TypeError("L'exposant doit être un entier")
        
        if self.numerator == 0 and other > 0 : 
            return Fraction(0,1)

        if other < 0 :
            new_num = self.denominator ** abs(other) # on inverse les roles : le numérateur devient le dénominateur de la fraction, élevée à la puissance 
            new_den = self.numerator ** abs(other) # idem, le dénominateur devient le numérateur de fraction élevée à la puissance
        else : 
            new_num = self.numerator ** other
            new_den = self.denominator ** other

        gcd = math.gcd(new_num, new_den) # pour simplification de la fraction 
        new_num //= gcd 
        new_den //= gcd
        return Fraction(new_num, new_den)
        

    def __eq__(self, other) : 
        """Overloading of the == operator for fractions
        
        PRE : "other" doit être une instance de la classe Fraction.

        POST : Retourne True si les fractions son égale, si ce n'est pas le cas ça retourne False

        RAISE : TypeError : Si "other" n'est pas un entier.
        
        """
        if not isinstance(other, Fraction):
            raise TypeError("Les objets doivent être des instances de la classe Fraction")
        return self.numerator * other.denominator == self.denominator * other.numerator 
        
    def __float__(self) :
        """Returns the decimal value of the fraction

        PRE : -
        
        POST : Retourne la valeur decimale de la fractions sous forme de nombre flottant 
        """
        return round(self.numerator/ self.denominator, 3)
        
    
# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)



# ------------------ Properties checking  ------------------

    def is_zero(self):
        """
        PRE : -

        POST : Retourne True si la fraction est égale à zéro, sinon retourne False.
        """
        return self.numerator == 0  # si le num est égale à 0 alors la fraction vaut 0
        


    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)
        
        PRE : -

        POST : Retourne True si la fraction est un entier, sinon retourne False. 
        """
        return self.numerator % self.denominator == 0 
        

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : - 

        POST : Retourne True si la valeur absolue de la fraction est inférieur à 1, sinon retourne False 
        """
        return abs(self.numerator) <  abs(self.denominator) 

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : - 

        POST : - Retourne True si le numérateur est égale à 1 dans la forme réduite de la fraction, sinon retourne False.
        """
        return self.numerator == 1

    def is_adjacent_to(self, other) : 
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : "other" doit être une instance de la classe Fraction

        POST : Retourne True si la fraction est adjacente, sinon ça renvoie False 
        """
        if  not isinstance(other, Fraction) :
            raise TypeError("Ce n'est pas une instance de la classe Fraction")
        diff_num = abs(self.numerator * other.denominator - other.numerator * self.denominator)
        return diff_num == 1  
