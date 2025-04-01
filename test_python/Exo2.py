# LES IMPORTATIONS NECESSAIRES
import tkinter as tk
from tkinter import simpledialog, messagebox
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

# lES VARIABLES GLOBALES
# collecter_entrees_utilisateur
longueur = largeur = hauteur = force = nom = nu = E = sigma_0 = 0
dir_force = (1, 1, 1)
# calculs
aire_x = aire_y = aire_z = norme_u = vec_u = comp_force = tr_sigma = epsilon = 0
aire = (1, 1, 1)
# tenseur identité
I = [[0 for i in range(3)] for j in range(3)]  # Initialisation du tenseur
# Création du tenseur identité
for i in range(3):
    for j in range(3):
        if i == j:
            I[i][j] = 1


def collecter_entrees_utilisateur():
    def valider():
        global longueur, largeur, hauteur, dir_force, force, nom, nu, E, sigma_0
        try:
            # Récupérer et convertir les entrées utilisateur
            longueur = float(champ_ll.get())
            largeur = float(champ_ww.get())
            hauteur = float(champ_hh.get())
            dir_force = tuple(float(coord) for coord in champ_dir_force.get().split(','))
            force = float(champ_force.get())
            nom = champ_nom.get()
            nu = float(champ_nu.get())
            E = float(champ_E.get())
            sigma_0 = float(champ_sigma_0.get())

            fenetre.destroy()  # Fermer la fenêtre après validation
            afficher_donnees()  # Afficher les données pour vérifier

        except ValueError:
            # Gérer les erreurs de conversion
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques valides pour les champs appropriés.")

    def afficher_donnees():
        # Créer une nouvelle fenêtre pour afficher les données
        fenetre_resultat = tk.Tk()
        fenetre_resultat.title("Résultats")
        fenetre_resultat.geometry("800x600")

        # Afficher les données
        tk.Label(fenetre_resultat, text="Données collectées :", font=("Arial", 12)).pack(pady=10)
        tk.Label(fenetre_resultat, text=f"""
            Longueur : {longueur}
            Largeur : {largeur}
            Hauteur : {hauteur}
            Direction Force : {dir_force}
            Force : {force}
            Nom : {nom}
            Nu : {nu}
            E : {E}
            Sigma_0 : {sigma_0}
            """, font=("Arial", 10)).pack(pady=10)

        # Bouton pour fermer la fenêtre
        bouton_fermer = tk.Button(fenetre_resultat, text="Fermer", command=fenetre_resultat.destroy, bg="red",
                                  fg="white")
        bouton_fermer.pack(pady=10)

        fenetre_resultat.mainloop()

    # Fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("Collecte des données utilisateur")

    # Longueur
    tk.Label(fenetre, text="Longueur (en m) :").pack()
    champ_ll = tk.Entry(fenetre)
    champ_ll.pack()

    # Largeur
    tk.Label(fenetre, text="Largeur (en m) :").pack()
    champ_ww = tk.Entry(fenetre)
    champ_ww.pack()

    # Hauteur
    tk.Label(fenetre, text="Hauteur (en m) :").pack()
    champ_hh = tk.Entry(fenetre)
    champ_hh.pack()

    # Direction de la force
    tk.Label(fenetre, text="Direction de la force (ex : (1,2,3)):").pack()
    champ_dir_force = tk.Entry(fenetre)
    champ_dir_force.pack()

    # Force
    tk.Label(fenetre, text="Force (en N) :").pack()
    champ_force = tk.Entry(fenetre)
    champ_force.pack()

    # Nom
    tk.Label(fenetre, text="Nom :").pack()
    champ_nom = tk.Entry(fenetre)
    champ_nom.pack()

    # Coefficient de Poisson (nu)
    tk.Label(fenetre, text="Nu (Coefficient de Poisson) :").pack()
    champ_nu = tk.Entry(fenetre)
    champ_nu.pack()

    # Module d'élasticité (E)
    tk.Label(fenetre, text="E (Module d'élasticité en Pa) :").pack()
    champ_E = tk.Entry(fenetre)
    champ_E.pack()

    # Contrainte initiale (sigma_0)
    tk.Label(fenetre, text="Sigma_0 (Contrainte initiale en Pa) :").pack()
    champ_sigma_0 = tk.Entry(fenetre)
    champ_sigma_0.pack()

    # Bouton pour valider
    bouton_valider = tk.Button(fenetre, text="Valider", command=valider, bg="green", fg="white")
    bouton_valider.pack()

    # Lancer la fenêtre
    fenetre.mainloop()


def calculs_internes():
    global longueur, largeur, hauteur, dir_force, force, nom, nu, E, sigma_0
    global aire, aire_x, aire_y, aire_z, norme_u, vec_u, comp_force, sigma, tr_sigma

    # Aire des sections perpendiculaires aux axes
    aire_x = largeur * hauteur
    aire_y = longueur * hauteur
    aire_z = longueur * largeur
    aire = (aire_x, aire_y, aire_z)  # Regroupons les donnees sous un tuple

    # Création du vecteur unitaire
    norme_u = math.sqrt(sum(i ** 2 for i in dir_force))
    vec_u = tuple(i / norme_u for i in dir_force)

    # Composantes de la force appliquée
    comp_force = tuple(force * i for i in vec_u)

    # Trace de sigma
    tr_sigma = sum(sigma[i][i] for i in range(3))
    import tkinter as tk


def choix_de_la_face():
    def generer_tenseur_de_contraintes():
        """
        Calcule les composantes du tenseur de contraintes en fonction de la face choisie.
        """
        global sigma
        # nonlocal choix_face
        choix_face = var_face.get()

        # Initialisation du tenseur des contraintes
        sigma = [[0 for i in range(3)] for j in range(3)]

        if choix_face == "X":  # Face YZ (normale à X)
            sigma[0][0] = comp_force[0] / aire[0]  # Contrainte normale
            sigma[1][0] = sigma[0][1] = comp_force[1] / aire[0]  # Cisaillement
            sigma[2][0] = sigma[0][2] = comp_force[2] / aire[0]  # Cisaillement
        elif choix_face == "Y":  # Face XZ (normale à Y)
            sigma[1][1] = comp_force[1] / aire[1]
            sigma[0][1] = sigma[1][0] = comp_force[0] / aire[1]
            sigma[2][1] = sigma[1][2] = comp_force[2] / aire[1]
        elif choix_face == "Z":  # Face XY (normale à Z)
            sigma[2][2] = comp_force[2] / aire[2]
            sigma[0][2] = sigma[2][0] = comp_force[0] / aire[2]
            sigma[1][2] = sigma[2][1] = comp_force[1] / aire[2]

        # Appel à la fonction pour afficher les résultats après le calcul
        afficher_donnees()

    # Afficher le résultat
    def afficher_donnees():
        # Créer une nouvelle fenêtre pour afficher les données
        fenetre_resultat = tk.Tk()
        fenetre_resultat.title("Résultats")
        fenetre_resultat.geometry("800x600")

        # Afficher les données sous une forme lisible
        sigma_formate = '\n'.join([f"{ligne}" for ligne in sigma])

        # Afficher les données
        tk.Label(fenetre_resultat, text="Tenseur de contraintes :", font=("Arial", 12)).pack(pady=10)
        tk.Label(fenetre_resultat, text=f"""
            sigma = {sigma_formate}
            """, font=("Arial", 10)).pack(pady=10)
        # Bouton pour fermer la fenêtre
        bouton_fermer = tk.Button(fenetre_resultat, text="Fermer", command=fenetre_resultat.destroy, bg="red",
                                  fg="white")
        bouton_fermer.pack(pady=10)

        fenetre_resultat.mainloop()

    # afficher_donnees()

    choix_face = None
    # Création de la fenêtre Tkinter
    fenetre = tk.Tk()
    fenetre.title("Choix de la face")

    # Variable pour le choix de la face
    var_face = tk.StringVar(value="X")
    tk.Label(fenetre, text="Choisissez la face sur laquelle la force s'applique :").pack()
    tk.Radiobutton(fenetre, text="YZ (normale à X)", variable=var_face, value="X").pack()
    tk.Radiobutton(fenetre, text="XZ (normale à Y)", variable=var_face, value="Y").pack()
    tk.Radiobutton(fenetre, text="XY (normale à Z)", variable=var_face, value="Z").pack()

    # Bouton pour lancer le calcul
    bouton_calculer = tk.Button(fenetre, text="Calculer",
                                command=lambda: [fenetre.destroy(), generer_tenseur_de_contraintes()], bg="green",
                                fg="white")
    bouton_calculer.pack()

    fenetre.mainloop()


def generer_tenseur_de_deformation():
    global sigma, I, tr_sigma, nu, E, epsilon

    # Initialisation du tenseur de déformation
    epsilon = [[0 for i in range(3)] for j in range(3)]

    # Calcul de epsilon = 1/E(sigma - nu*tr_sigma*I)
    for i in range(3):
        for j in range(3):
            epsilon[i][j] = (1 / E) * ((sigma[i][j]) - nu * tr_sigma * (I[i][j]))

    # Afficher le résultat
    def afficher_donnees():
        # Créer une nouvelle fenêtre pour afficher les données
        fenetre_resultat = tk.Tk()
        fenetre_resultat.title("Résultats")
        fenetre_resultat.geometry("800x600")

        # Afficher les données sous une forme lisible
        epsilon_formate = '\n'.join([f"{ligne}" for ligne in epsilon])

        # Afficher les données
        tk.Label(fenetre_resultat, text="Tenseur de déformations :", font=("Arial", 12)).pack(pady=10)
        tk.Label(fenetre_resultat, text=f"""
            epsilon = {epsilon_formate}
            """, font=("Arial", 10)).pack(pady=10)
        # Bouton pour fermer la fenêtre
        bouton_fermer = tk.Button(fenetre_resultat, text="Fermer", command=fenetre_resultat.destroy, bg="red",
                                  fg="white")
        bouton_fermer.pack(pady=10)

        fenetre_resultat.mainloop()

    afficher_donnees()

    print(epsilon)
collecter_entrees_utilisateur()
choix_de_la_face()
generer_tenseur_de_deformation()
