import pandas as pd
import matplotlib.pyplot as plt

# Lecture des données
data = pd.read_csv("donnees_crue.csv")

# Statistiques simples
moyenne = data["debit"].mean()
maximum = data["debit"].max()

print("Débit moyen :", moyenne)
print("Débit maximum :", maximum)

# Détection seuil de vigilance
seuil = 50

print("\nJours en vigilance :")

jours_crue = data[data["debit"] > seuil]

print(jours_crue)

# Graphique
# Graphique
plt.plot(data["jour"], data["debit"], marker='o')

plt.axhline(y=seuil, linestyle='--')

plt.title("Evolution du débit de la rivière")
plt.xlabel("Jour")
plt.ylabel("Débit")

plt.grid()

# Sauvegarde du graphique
plt.savefig("graphique_crue.png")

plt.show()