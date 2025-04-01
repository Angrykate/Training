print("Veuillez entrez 2 nombres valides")
while True:
    first = input("Veuillez entrez le premier nombre: ")
    second = input("Veuillez entrez le second nombre: ")
    if not (first.isdigit() and second.isdigit()):
        print("\nVeuillez entrez des nombres valides!!")
        continue
    else:
        résultat = int(first)+int(second)
        print(f"\nLe résultat de l'addition de {first} et de {second} est égal à {résultat}")
        break