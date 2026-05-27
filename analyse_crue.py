import pandas as pd
import matplotlib.pyplot as plt

print("Analyse démarrée")

# Lecture des données
data = pd.read_csv("donnees_crue.csv")

# Statistiques
moyenne = data["debit"].mean()
maximum = data["debit"].max()

print("Débit moyen :", moyenne)
print("Débit maximum :", maximum)

# Seuil
seuil = 50

jours_crue = data[data["debit"] > seuil]

print("\nJours en vigilance :")
print(jours_crue)

# Graphique
plt.plot(data["jour"], data["debit"], marker='o', label="Débit")

plt.axhline(y=seuil, linestyle='--', label="Seuil de vigilance")

plt.title("Evolution du débit de la rivière")
plt.xlabel("Jour")
plt.ylabel("Débit")

plt.legend()
plt.grid()

# Sauvegarde
plt.savefig("graphique_crue.png")

# Affichage
plt.show()