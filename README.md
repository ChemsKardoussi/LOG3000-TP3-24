# Nom de projet :
Calculatrice Web Flask 
## Numéro d'équipe
Équipe 24
## Objectif 
Ce projet consiste a développer une applicaiton web de calculatrice avec Flask (Python). L'idee de base est de permettre d'éffectuer des opération simples (addition, soustraction, multiplication et division) directment depuis l'interface. 

Le veritable objectif est surtout de mettre en pratique tout ce qu'on a appris sur le travail en équipe et les bonnes pratique en génie logiciel. Il nous a été fourni un code peu propre, avec peu de documentation et quelques bug caché. Notre mission est de reprendre ce code et de structrer le projet, pour être en mesure de documenter chaque partie et ajouter des tests pour détecter les problèmes cachés.
# Structure du projet

```
LOG3000-TP3-24/
├── app.py                    # Point d'entrée principal de l'application Flask
├── operators.py              # Contient les fonctions de base : add, subtract, multiply, divide
│
├── templates/                # Module contenant les pages HTML
│   └── index.html           # Interface principale de la calculatrice
│
├── static/                   # Module contenant les fichiers statiques 
│   └── style.css            # Feuille de style principale
│
├── tests/                    # Module contenant les tests automatisés
│   ├── test_operators.py    # Tests unitaires pour les opérateurs
│   └── README.md            # Documentation des tests
│
├── .gitignore               # Fichiers à ignorer par Git
└── 
## Prérequis d'installation 
- Python 3.8 ou plus recent
- pip (Normalament installé automatiquement avec python)
- Git (Pour cloner le depot et gérer les versions)
```
## Instructions d'installation 

1. Cloner le dépôt et se placer dans le dossier du projet :

```bash
git clone <URL_DU_DEPOT>
cd LOG3000-TP3-24
```

2. Créer un environnement virtuel Python :

```bash
python -m venv .venv
```

3. Activer l'environnement virtuel :

- **Windows (PowerShell)**

```powershell
.\.venv\Scripts\Activate.ps1
```

- **macOS / Linux**

```bash
source .venv/bin/activate
```

4. Installer les dépendances nécessaires :

```bash
pip install Flask
```

5. Lancer l'application :

```bash
python app.py
```

6. Ouvrir la calculatrice dans le navigateur :

```text
http://127.0.0.1:5000/
```
