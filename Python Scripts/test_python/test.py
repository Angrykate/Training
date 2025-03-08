import numpy as np
import matplotlib.pyplot as plt

# Paramètres du béton
E = 3e10  # Module de Young en Pa
nu = 0.2  # Coefficient de Poisson
F = 1200  # Force totale appliquée en N
sigma_adm = 30e3 # Contrainte admissible

# Dimensions du matériau
l = 0.1  # Largeur de la section en m
h = 0.1  # Hauteur de la section en m
L = 2  # Longueur du matériau en m

# Aire de la section
A = l * h  # Aire en m²

# Répartition des forces dans les directions x, y et z
F_x = 0.8 * F  # Force dans la direction x
F_y = 0.1 * F  # Force dans la direction y
F_z = 0.1 * F  # Force dans la direction z

# 1. Calcul des contraintes
sigma_xx = F_x / A  # Contrainte de traction en x (N/m²)
sigma_yy = F_y / A  # Contrainte de traction en y (N/m²)
sigma_zz = F_z / A  # Contrainte de traction en z (N/m²)
print(f"Contrainte σ_xx (Pa): {sigma_xx}")
print(f"Contrainte σ_yy (Pa): {sigma_yy}")
print(f"Contrainte σ_zz (Pa): {sigma_zz}")

# 2. Calcul des déformations
epsilon_xx = (sigma_xx - nu*(sigma_yy+sigma_zz)) / E  # Déformation longitudinale en x
epsilon_yy = (sigma_yy - nu*(sigma_xx+sigma_zz)) / E  # Déformation transversale en y
epsilon_zz = (sigma_zz - nu*(sigma_xx+sigma_yy)) / E  # Déformation transversale en z
print(f"Déformation ε_xx: {epsilon_xx}")
print(f"Déformation ε_yy = ε_zz: {epsilon_yy}")

# Calcul de la contrainte de Von Mises
sigma_xy,sigma_yz,sigma_zx = 0,0,0 # Contraintes de cisaillement nulles
sigma_vm = np.sqrt(0.5 * ((sigma_xx - sigma_yy)**2 +
                          (sigma_yy - sigma_zz)**2 +
                          (sigma_zz - sigma_xx)**2 +
                          6*(sigma_xy**2 + sigma_yz**2 + sigma_zx**2)))
print(f"Contrainte de Von Mises : {sigma_vm:.2f} Pa")
if sigma_vm > sigma_adm:
    print("Le matériau dépasse la contrainte admissible, risque de défaillance.")
else:
    print("Le matériau est sous la contrainte admissible, pas de défaillance.")

# 3. Visualisation des résultats : Contraintes
x_values = np.linspace(0, L, 100)  # Positions le long de L
sigma_values_xx = sigma_xx * np.ones_like(x_values)  # Contrainte constante sur toute la longueur
sigma_values_yy = sigma_yy * np.ones_like(x_values)  # Contrainte constante sur toute la longueur
sigma_values_zz = sigma_zz * np.ones_like(x_values)  # Contrainte constante sur toute la longueur

# Affichage des contraintes
plt.figure(figsize=(8, 6))
plt.plot(x_values, sigma_values_xx, label='Contrainte σ_xx', color='b')
plt.plot(x_values, sigma_values_yy, label='Contrainte σ_yy', color='g')
plt.plot(x_values, sigma_values_zz, label='Contrainte σ_zz', color='r')
plt.title('Distribution des Contraintes dans le matériau')
plt.xlabel('Position le long de L (m)')
plt.ylabel('Contrainte (Pa)')
plt.legend()
plt.grid(True)
plt.show()

# Affichage des contraintes dans les directions
plt.figure(figsize=(10, 6))
x_positions = np.array([0, 1, 2])
sigma_values = np.array([sigma_xx, sigma_yy, sigma_zz])

plt.plot(x_positions, sigma_values, label='Contraintes', color='blue', marker='o', linestyle='-', markersize=8)
plt.title("Distribution des contraintes dans les directions x, y et z", fontsize=14)
plt.xticks(x_positions, ['$\sigma_{xx}$', '$\sigma_{yy}$', '$\sigma_{zz}$'])
plt.ylabel('Contrainte (Pa)', fontsize=12)
plt.grid(True)
plt.legend()
plt.show()


# 4. Visualisation des déformations
epsilon_values_xx = epsilon_xx * np.ones_like(x_values)  # Déformation constante sur toute la longueur
epsilon_values_yy = epsilon_yy * np.ones_like(x_values)  # Déformation constante dans y
epsilon_values_zz = epsilon_zz * np.ones_like(x_values)  # Déformation constante dans z

# Affichage des déformations
plt.figure(figsize=(8, 6))
plt.plot(x_values, epsilon_values_xx, label="Déformation ε_xx", color='r')
plt.plot(x_values, epsilon_values_yy, label="Déformation ε_yy", color='g')
plt.plot(x_values, epsilon_values_zz, label="Déformation ε_zz", color='orange')
plt.title("Déformations dans le matériau sous charge")
plt.xlabel("Position le long de L (m)")
plt.ylabel("Déformation")
plt.legend()
plt.grid(True)
plt.show()

# 5. Histogramme des déformations (appliquées)
plt.figure(figsize=(10, 6))
deformation_values = np.array([epsilon_xx, epsilon_yy, epsilon_zz])

plt.bar(x_positions, deformation_values, color=['red', 'green', 'orange'], alpha=0.7, label='Déformations')
plt.title("Histogramme des déformations dans les directions x, y et z", fontsize=14)
plt.xticks(x_positions, ['$\epsilon_{xx}$', '$\epsilon_{yy}$', '$\epsilon_{zz}$'])
plt.ylabel('Déformation', fontsize=12)
plt.legend()
plt.show()

# 6. Comportement du matériau : graphique contrainte-déformation


# affichage 2
plt.figure(figsize=(10, 6))
plt.plot([epsilon_xx], [sigma_xx], label=r'$\sigma_{xx}$ vs $\epsilon_{xx}$', color='red', marker='o')
plt.plot([epsilon_yy], [sigma_yy], label=r'$\sigma_{yy}$ vs $\epsilon_{yy}$', color='green', marker='o')
plt.plot([epsilon_zz], [sigma_zz], label=r'$\sigma_{zz}$ vs $\epsilon_{zz}$', color='orange', marker='o')

plt.title("Comportement du matériau : Contrainte vs Déformation", fontsize=14)
plt.xlabel('Déformation ($\epsilon$)', fontsize=12)
plt.ylabel('Contrainte ($\sigma$)', fontsize=12)
plt.grid(True)
plt.legend()
plt.show()

deformation_values = np.linspace(0, epsilon_xx, 100)  # Deformations allant de 0 à ε_xx
stress_values = E * deformation_values  # Contrainte liée à la déformation

plt.figure(figsize=(8, 6))
plt.plot(deformation_values, stress_values, label="Comportement élastique du béton", color='purple')
plt.title("Comportement du matériau : Relation Contrainte-Déformation")
plt.xlabel("Déformation")
plt.ylabel("Contrainte (Pa)")
plt.legend()
plt.grid(True)
plt.show()

# 7. Visualisation des résultats: Contrainte de Von Mises
fig, ax = plt.subplots()
labels = ['Contrainte admissible', 'Von Mises']
values = [sigma_adm, sigma_vm]
ax.bar(labels, values, color=['blue','orange'])
ax.set_title('Contrainte de Von Mises et Contrainte admissible')
ax.set_xlabel('Composantes de contrainte')
ax.set_ylabel('Valeurs de contrainte (Pa)')
plt.show()
