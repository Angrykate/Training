import random
print("***Le jeu du nombre mystère***")
print("Trouve le nombre se trouvant entre 0 et 100")
nbr_essai=5
number=random.randint(0,100)
user_choice=-1
while nbr_essai>0:
    print("Il te reste "+str(nbr_essai)+" essai"+("s" if nbr_essai>1 else ""))
    user_choice=input("Devine le nombre: ")
    if not user_choice.isdigit():
        print("Veuillez entrez un nombre  valide!")
        continue
    if int(user_choice) > number:
        print("Le nombre mystère est plus petit que "+user_choice)
    elif int(user_choice) < number:
        print("Le nombre mystère est plus grand que "+user_choice)
    else:
        print("Bravo! Le nombre mystère était bien "+str(number))
        print('Tu as trouvé le nombre en '+str(6-nbr_essai)+" essais")
        break
    nbr_essai -= 1
else:
    print("Dommage! Le nombre mystère était "+str(number))

print("Fin du jeu!")
