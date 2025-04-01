print("Ce programme vous permet d'effectuer des conversions de devises")
devices = ["Euro (€)", "Dollar ($)", "FCFA (₣)"]

# Afficher les combinaisons de conversions
index = 1
for i in range(len(devices)):
    for j in range(len(devices)):
        if i != j:
            print(f"{index} - {devices[i]} vers {devices[j]}")
            index += 1
print(f"{index} - Quitter")

# Fonction de conversion (à adapter selon les taux de change)
def conversion(unit1, unit2, taux):
    while True:
        valeur_initiale = input(f"Conversion {unit1} -> {unit2}. Donnez la valeur en {unit1} (Entrez un nombre négatif pour arrêter) : ")
        try:
            valeur_float = float(valeur_initiale)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue
        if valeur_float < 0:
            return
        valeur_convertie = round(valeur_float * taux, 2)
        print(f"Résultat de la conversion : {valeur_float} {unit1} = {valeur_convertie} {unit2}")

# Taux de change (à adapter selon les taux actuels)
taux_change = {
    (0, 1): 1.1,  # Euro -> Dollar
    (0, 2): 655.96,  # Euro -> FCFA
    (1, 0): 0.91,  # Dollar -> Euro
    (1, 2): 600,  # Dollar -> FCFA
    (2, 0): 0.0015,  # FCFA -> Euro
    (2, 1): 0.0017  # FCFA -> Dollar
}

while True:
    choix = input("Votre choix : ")
    if choix == str(index):
        print("À bientôt")
        break
    if not choix.isdigit() or int(choix) not in range(1, index):
        print("Veuillez entrer une valeur correcte !")
        continue
    choix = int(choix) - 1
    i, j = choix // (len(devices) - 1), choix % (len(devices) - 1)
    if j >= i:
        j += 1
    conversion(devices[i], devices[j], taux_change[(i, j)])
