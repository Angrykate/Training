
MENU = """Choisissez parmis les 5 options suivantes: 
    1-) Ajouter un élement à la liste
    2-) Retirer un élement de la liste
    3-) Afficher la liste 
    4-) Vider la liste
    5-) Quitter"""
Liste = []
user_choice=''
print("MENU".center(24,'*'))
while not user_choice == '5':
    print(MENU)
    user_choice = input("👉 Votre choix: ")
    if user_choice not in ["1","2","3","4","5"]:
        print("Veuillez entrez une option valide...")
        continue
    match user_choice:
        case '1':
            element=input("Entrez le nom de l'élement à ajouter à la liste: ")
            Liste.append(element)
            print(f"l'élement {element} a bien été ajouté à votre liste")
        case '2':
            if not Liste:
                print("La liste ne contient aucun élement")
            else:
                element = input("Entrez le nom de l'élement à retirer de la liste: ")
                if element in Liste:
                    Liste.remove(element)
                    print(f"l'élement {element} a bien été retiré de la liste")
                else:
                    print(f"l'élement {element} n'est pas dans la liste")
        case '3':
            if not Liste:
                print('La liste est vide')
            else:
                print("Voici le contenu de votre liste: ")
                for i,element in enumerate(Liste):
                    print(f"{i+1}- {element}")
        case '4':
            Liste.clear()
            print("La liste été vidée de son contenu")
        case '5':
            print("A Bientot")
    print("-"*50)




