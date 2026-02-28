"""Module d'opérateurs arithmétiques de base pour la calculatrice.

Chaque fonction reçoit deux opérandes numériques et retourne
le résultat de l'opération correspondante.
"""


def add(a, b):
    """Additionne deux nombres.

    Args:
        a (float): Premier opérande.
        b (float): Deuxième opérande.

    Returns:
        float: La somme a + b.
    """
    return a + b


def subtract(a, b):
    """Soustrait le deuxième opérande du premier (a - b).

    Args:
        a (float): Opérande de départ.
        b (float): Opérande à soustraire.

    Returns:
        float: La différence a - b.
    """
    return a - b


def multiply(a, b):
    """Multiplie deux nombres (a × b).

    Args:
        a (float): Premier facteur.
        b (float): Deuxième facteur.

    Returns:
        float: Le produit a * b.
    """
    return a * b


def divide(a, b):
    """Divise le premier opérande par le deuxième (a / b).

    Args:
        a (float): Le numérateur.
        b (float): Le dénominateur.

    Returns:
        float: Le quotient a / b.
    """
    return a / b
