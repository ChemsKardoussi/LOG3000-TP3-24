# tests/

## Description
Ce dossier contient les tests automatisés de l'application. Les tests verifient que chaque fonction fait bien ce qu'elle doit faire et permettent de détecter les bogues

## Contenu

### test_operators.py
- Tests pour les opérations mathématiques (add, subtract, multiply, divide)
- 9 tests qui vérifient que les calculs donnent les bons résultats
- Tests spécifiques pour les 3 bugs identifiés :
  - **Bug 1** : Soustraction (subtract) - 1 test
  - **Bug 2** : Multiplication (multiply) - 1 test
  - **Bug 3** : Division (divide) - 1 test

## Lancer les tests

**Installer pytest:**
```bash
py -m pip install pytest
```

**Lancer tous les tests:**
```bash
py -m pytest tests/
```

**Avec plus de détails:**
```bash
py -m pytest tests/ -v
```

**Un fichier spécifique:**
```bash
py -m pytest tests/test_operators.py
```

## Interpréter les résultats

- **PASSED** = Le test a réussi la fonction fonctionne correctement
- **FAILED** = Le test a échoué il y a un bogue à corriger

Chaque test qui échoue indique un problème dans le code qu'il faut corriger

## Structure d'un test

Chaque test vérifie un comportement précis:

```python
def test_add_integer_numbers():
    """Teste l'addition avec des nombres entiers"""
    result = add(7, 4)
    assert result == 11  # Si faux, pytest affiche une erreur
```

Si l'assertion est fausse pytest affiche une erreur et on sait qu'il y a un bogue

## Dépendances

- **pytest** (framework de tests)
- Les modules `app.py` et `operators.py` qu'on teste
