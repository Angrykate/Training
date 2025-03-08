import random
# Règles du jeu
print("""REGLES DU JEU:
    - Le jeu comporte deux joueurs : vous et un ennemi.
    - Vous commencez tous les deux avec 50 points de vie. 
    - Votre personnage dispose de 3 potions qui vous permettent de récupérer des points de vie.
    - L'ennemi ne dispose d'aucune potion.
    - Chaque potion vous permet de récupérer un nombre aléatoire de points de vie,compris entre 20 et 50.
    - Votre attaque inflige à l'ennemi des dégâts aléatoires compris entre 5 et 15 points de vie.
    - L'attaque de l'ennemi vous inflige des dégâts aléatoires compris entre 10 et 20 points de vie.
    - Lorsque vous utilisez une potion, vous passez le prochain tour.
    
""")
pov=''
while pov not in ["o","n"]:
    pov = input("Avez vous compris (o/n)? ")
if pov == 'n':
    print("Relit bien !!")
    exit()
print("-*-"*50)
print("")

# Données du jeu
PLAYER_HEALTH = 50
ENNEMI_HEALTH = 50
SKIP_TURN = False
POTION_NUMBER = 3

# Programme principal
while True:
    if SKIP_TURN:
        print("Vous passez votre tour...")
        SKIP_TURN = False
    else:
        user_choice = input("Souhaitez-vous attaquer (1) ou prendre une potion (2) ? ")
        match user_choice:
            case "1":
                Player_attack = random.randint(5, 15)
                ENNEMI_HEALTH -= Player_attack
                print(f"Vous avez infligé {Player_attack} points de dégats à l'ennemi ⚔ ")
            case "2":
                if POTION_NUMBER > 0:
                    recovery_health = random.randint(20, 50)
                    PLAYER_HEALTH += recovery_health
                    POTION_NUMBER -= 1
                    print(f"Vous avez recupérer {recovery_health} points de vie ❤ ({POTION_NUMBER} restantes)")
                    SKIP_TURN = True
                else:
                    print("Vous n'avez plus de potion...")
                    continue
            case _:
                continue
    if ENNEMI_HEALTH > 0:
        Ennemi_attack = random.randint(10, 20)
        PLAYER_HEALTH -= Ennemi_attack
        print(f"L'ennemi vous a infligé {Ennemi_attack} points de dégats ⚔ ")
    else:
        print("Vous avez gagné!💪")
        break
    if PLAYER_HEALTH <= 0:
        print("Vous avez perdu!😢")
        break
    else:
        print(f"Il vous reste {PLAYER_HEALTH} points de vie")
        print(f"Il reste {ENNEMI_HEALTH} points de vie à l'ennemi")
    print("-"*50)
print("Fin du jeu")
