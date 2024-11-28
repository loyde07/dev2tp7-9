# Mayala-Luneko Loyde 

from TP7fraction import Fraction

fraction1 = Fraction(7, 5)
fraction2 = Fraction(1, 8)
fraction3 = Fraction(7, 2)
fraction4 = Fraction(8, 4)
fraction5 = Fraction(0, 1)

if __name__ == "__main__":
    # Addition
    try:
        addition = fraction1 + fraction2
        print(f"Addition: {addition}")
    except Exception as e:
        print(f" Une erreur s'est produite lors de l'addtion: {e}")

    # Subtraction
    try:
        soustraction = fraction1 - fraction2
        print(f"Soustraction: {soustraction}")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la soustraction: {e}")

    # Multiplication
    try:
        multiplication = fraction1 * fraction2
        print(f"Multiplication: {multiplication}")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la multiplication: {e}")

    # Division
    try:
        division = fraction1 / fraction2
        print(f"Division: {division}")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la division: {e}")

    # Power
    try:
        puissance = fraction3**2
        print(f"Puissance: {puissance}")
    except Exception as e:
        print(f" Une erreur s'est produite lors du calcul élevé à la puissance: {e}")

    # equal
    try:
        equality = fraction1 == fraction2
        print(f"Egalite: {equality}")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'égalité: {e}")

    try:
        as_mixed_number = fraction1.as_mixed_number()
        print(f"As mixed number: {as_mixed_number}")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la conversion en nombre mixte: {e}")

        # is_integer
    try:
        is_integer = fraction4.is_integer()
        print(f"Est un entier: {is_integer}")
    except Exception as e:
        print(f"Une erreur s'est produite lors du test d'entier: {e}")

        # float
    try:
        as_float = float(fraction1)
        print(f"Valeur flottante: {as_float}")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la conversion en flottant: {e}")

        # is_proper
    try:
        is_proper = fraction1.is_proper()
        print(f"Est une fraction propre: {is_proper}")
    except Exception as e:
        print(f"Une erreur s'est produite lors du test de fraction propre: {e}")

        # is_zero
    try:
        is_zero = fraction5.is_zero()
        print(f"Est nul: {is_zero}")
    except Exception as e:
        print(f"Une erreur s'est produite lors du test de zéro: {e}")

        # is_unit
    try:
        is_unit = fraction2.is_unit()
        print(f"Est une fraction unité: {is_unit}")
    except Exception as e:
        print(f"Une erreur s'est produite lors du test de fraction unité: {e}")

        # is_adjacent_to
    try:
        is_adjacent = fraction1.is_adjacent_to(fraction2)
        print(f"Les fractions sont adjacentes: {is_adjacent}")
    except Exception as e:
        print(f"Une erreur s'est produite lors du test d'adjacence: {e}")


