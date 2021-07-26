# Projet : Base de données immobilières

Table of content :
- [JupyterNoteBook 📝]('./analyse.ipynb)
- [Database SQL 🛠]('./database)
- [Datbase seed script 📊]('./data)

---
## Data dictionary
|Entité|Code propriété|Nom de propriété|Description|Format|Contraintes|
|--|--|--|--|--|--|
|Transaction|date_mutation|Date mutation|Date de signature de l’acte (au format JJ/MM/AAAA) – Une restitution au format AAAA/MM/JJ (norme ISO 8601) est prévue à compter de la mise à jour d’octobre 2019.|Date (JJ/MM/AAAA)|
|Transaction|valeur_fonciere|Valeur foncière|Il s’agit du montant ou de l’évaluation déclaré dans le cadre d’une mutation à titre onéreux. La valeur foncière est le prix net vendeur. La TVA est incluse. Ce prix n’inclut pas, en revanche, les frais de notaires.|Float (precis. 2)|
|Localisation|code_postal|Code postal||Int|
|Localisation|code_departement|Code du département|Référence cadastrale de la parcelle|Int|
|Localisation|code_commune|Code de la commune|Référence cadastrale de la parcelle|Int|
|Localisation|code_type_local|Code type local|1 : maison ; 2 : appartement ; 3 : dépendance (isolée) ; 4 : local industriel et commercial ou assimilés|Int|
|Bien|surface_reel_bati|Surface réel batie|La surface réelle est la surface mesurée au sol entre les murs ou séparations et arrondie au mètre carré inférieur. Les surfaces des dépendances ne sont pas prises en compte.|Float|
|Bien|nb_pieces_principales|Nombre de pièces principales|Les cuisines, salles d’eau et dépendances ne sont pas prises en compte.|Float|