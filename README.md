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


# Installation et exécution

## 1. Cloner le projet

```bash
git clone https://github.com/Lamessiogah/analyse_hydrologique_python.git
```

## 2. Entrer dans le dossier

```bash
cd analyse_hydrologique_python
```

## 3. Installer les dépendances

```bash
pip install pandas matplotlib
```

ou :

```bash
pip3 install pandas matplotlib
```

## 4. Exécuter le programme

```bash
python3 analyse_crue.py
```

---

## Résultat attendu

Le programme :
- affiche les statistiques hydrologiques ;
- détecte les jours de vigilance ;
- génère automatiquement un graphique :
  - `graphique_crue.png`
## Capture d’écran
### Exemple de sortie terminal

```bash
Analyse démarrée

Débit moyen : 37.2
Débit maximum : 75

Jours en vigilance :
   jour  debit
6     7     60
7     8     75
8     9     55

Graphique enregistré : graphique_crue.png
```


### Graphique généré

![Graphique des débits](graphique_crue.png)

---

## Auteur
Lamessi Jérôme OGAH
