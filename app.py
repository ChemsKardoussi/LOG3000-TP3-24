"""Application Flask implémentant une calculatrice web simple.

Ce module définit les routes et la logique de parsing des expressions
arithmétiques saisies par l'utilisateur via le formulaire.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Associe chaque symbole d'opérateur à sa fonction de calcul
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculate(expr: str):
    """Parse et évalue une expression arithmétique simple.

    L'expression doit contenir exactement un opérateur (+, -, *, /)
    situé entre deux opérandes numériques (ex. "12+4").

    Args:
        expr (str): L'expression à évaluer.

    Returns:
        float: Le résultat du calcul.

    Raises:
        ValueError: Si l'expression est vide, mal formatée,
            contient plus d'un opérateur ou des opérandes non numériques.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Retirer les espaces pour simplifier le parsing
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Parcourir la chaîne pour localiser l'unique opérateur
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # L'opérateur ne peut pas être en début/fin ni absent
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    # Convertir les opérandes en nombres flottants
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Gère la page principale de la calculatrice.

    En GET, affiche le formulaire vide.
    En POST, évalue l'expression soumise et affiche le résultat
    ou un message d'erreur.

    Returns:
        str: Le rendu HTML de la page index avec le résultat éventuel.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)