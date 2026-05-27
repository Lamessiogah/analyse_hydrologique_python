# Analyse hydrologique avec Python

## Description
Mini projet réalisé avec Python pour analyser des données hydrologiques simples dans le cadre d’un apprentissage en modélisation et prévision des crues.

Le projet permet :
- de lire des données de débit depuis un fichier CSV ;
- de calculer des statistiques simples ;
- de détecter des seuils de vigilance ;
- de générer une visualisation graphique des débits.

---

## Technologies utilisées
- Python
- pandas
- matplotlib

---

## Fonctionnalités
- Lecture de données hydrologiques
- Analyse statistique
- Détection automatique des jours critiques
- Génération d’un graphique des débits

---

## Fichiers du projet
- `analyse_crue.py` : script principal
- `donnees_crue.csv` : données hydrologiques
- `graphique_crue.png` : graphique généré automatiquement

---

## Exemple de résultat
Le script détecte les jours où le débit dépasse un seuil critique fixé à 50.

---

## Exécution du projet

Installation des dépendances :

```bash
pip install pandas matplotlib
```

Lancement du script :

```bash
python3 analyse_crue.py
```

---

## Auteur
OGAH Lamessi Jérôme
