# Module : static

## Raison d’être du module
Le module `static` regroupe les ressources statiques de l’interface web (fichiers servis tels quels au navigateur), principalement la mise en forme visuelle de la calculatrice.

## Principaux fichiers et responsabilités
- `style.css` : définit les styles CSS (mise en page, couleurs, espacements, apparence des boutons et du résultat).

## Dépendances ou hypothèses
- Ce dossier suit la convention Flask : les fichiers sont exposés depuis `/static`.
- Les classes/identifiants CSS sont utilisés par le template `templates/index.html`.
- Aucune logique Python n’est exécutée ici.
