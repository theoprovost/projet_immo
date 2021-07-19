# Projet : Base de données immobilières

## Import des données et conceptualisation
### Dictionnaire de données

|Code propriété|Nom de propriété|Description|Format|
|--|--|--|--|
|date_mutation|Date mutation|Date de signature de l’acte (au format JJ/MM/AAAA) – Une restitution au format AAAA/MM/JJ (norme ISO 8601) est prévue à compter de la mise à jour d’octobre 2019.|Date|
|valeur_fonciere|Valeur foncière|Il s’agit du montant ou de l’évaluation déclaré dans le cadre d’une mutation à titre onéreux. La valeur foncière est le prix net vendeur. La TVA est incluse. Ce prix n’inclut pas, en revanche, les frais de notaires.||
|code_postal|Code postal||Int|
|code_departement|Code du département|Référence cadastrale de la parcelle|?|
|code_commune|Code de la commune|Référence cadastrale de la parcelle|?|
|code_type_local|Code type local|1 : maison ; 2 : appartement ; 3 : dépendance (isolée) ; 4 : local industriel et commercial ou assimilés|Int|
|surface_reel_bati|Surface réel batie|La surface réelle est la surface mesurée au sol entre les murs ou séparations et arrondie au mètre carré inférieur. Les surfaces des dépendances ne sont pas prises en compte.||
|nb_pieces_principales|Nombre de pièces principales|Les cuisines, salles d’eau et dépendances ne sont pas prises en compte.|Float ?|

### MCD (Modèle Conceptuel de Données)

// TO DO

### MPD (Modèle Physique de Données)

// TO DO

## Création de la base de données

// Ici : script de création de base de données

Spécifications techniques liées au choix du SGBDR (Système de Gestion de Base de Données Relationelles) :

- [Postgresql](https://www.postgresql.org/docs/) min v.13 (LTS)
- [Optionel] [pg_admin](https://www.pgadmin.org/) : Open Source administration and development platform for PostgreSQL

### Creation d'un user et da la BDD

```sql
-- Initial creation of the database and it's owner

DROP ROLE IF EXISTS "immo_admin";

-- CREATE USER|ROLE 'newuser'@'localhost' IDENTIFIED BY 'password';
CREATE ROLE "immo_admin" WITH PASSWORD 'e5679489-a4c8-445a-9036-0838a70de506';

DROP DATABASE IF EXISTS immo_db;

-- CREATE DATABASE 'database_name';
CREATE DATABASE immo_db;

-- Give privelegies to the role created just before
GRANT ALL PRIVILEGES ON DATABASE immo_db TO "immo_admin";
```

### Création des tables


## Cas d'étude

// Ici : requetes SQL et analyse