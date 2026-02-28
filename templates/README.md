# Module : templates

## Raison d’être du module
Le module `templates` contient les vues HTML rendues par Flask pour afficher l’interface utilisateur de la calculatrice.

## Principaux fichiers et responsabilités
- `index.html` : page principale de l’application; affiche l’interface de calcul, envoie l’expression au serveur et montre le résultat retourné.

## Dépendances ou hypothèses
- Ce dossier suit la convention Flask : les vues sont chargées via `render_template`.
- Le template dépend du style défini dans `static/style.css`.
- La variable `result` fournie par `app.py` est disponible lors du rendu.
