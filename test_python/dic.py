import numpy as np
import matplotlib.pyplot as plt

# Données du problème
E = 3e10  # Module de Young en Pa
nu = 0.2  # Coefficient de Poisson
F = 1200  # Force en N
l = 0.1  # Largeur de la section en m
h = 0.1  # Hauteur de la section en m
L = 2.0  # Longueur du matériau en m

# Dimensions de la section
A = l * h  # Aire de la section en m^2

# Calcul de la contrainte en x, y, z (80% en x, 10% en y, 10% en z)
force_x = 0.8 * F
force_y = 0.1 * F
force_z = 0.1 * F

# Contrainte dans les directions x, y, z (σ = F / A)
sigma_xx = force_x / A
sigma_yy = force_y / A
sigma_zz = force_z / A

# Calcul de la déformation dans les directions x, y, z (ε = σ / E)
epsilon_xx = (sigma_xx - nu*(sigma_yy+sigma_zz)) / E  # Déformation longitudinale en x
epsilon_yy = (sigma_yy - nu*(sigma_xx+sigma_zz)) / E  # Déformation transversale en y
epsilon_zz = (sigma_zz - nu*(sigma_xx+sigma_yy)) / E

# Tracer les graphiques

# 1. Graphique des contraintes dans les directions x, y et z
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

# 2. Histogramme des déformations dans les directions x, y et z
plt.figure(figsize=(10, 6))
deformation_values = np.array([epsilon_xx, epsilon_yy, epsilon_zz])

plt.bar(x_positions, deformation_values, color=['red', 'green', 'orange'], alpha=0.7, label='Déformations')
plt.title("Histogramme des déformations dans les directions x, y et z", fontsize=14)
plt.xticks(x_positions, ['$\epsilon_{xx}$', '$\epsilon_{yy}$', '$\epsilon_{zz}$'])
plt.ylabel('Déformation', fontsize=12)
plt.legend()
plt.show()

# 3. Contrainte vs Déformation (Comportement du matériau)
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

# 4. Visualisation 3D des contraintes et déformations dans le matériau

# Création des axes
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Coordonnées pour les 3 directions (x, y, z)
x_vals = np.array([0, 1, 2])
y_vals = np.array([0, 1, 2])
z_vals = np.array([0, 1, 2])

# Valeurs des contraintes et déformations
sigma_vals = [sigma_xx, sigma_yy, sigma_zz]
epsilon_vals = [epsilon_xx, epsilon_yy, epsilon_zz]

# Plot des contraintes en 3D
sc = ax.scatter(x_vals, y_vals, z_vals, c=sigma_vals, cmap='viridis', label='Contraintes')

# Annoter les directions
for i in range(len(sigma_vals)):
    ax.text(x_vals[i], y_vals[i], z_vals[i], f'{sigma_vals[i]:.2e}', color='black')

ax.set_xlabel('Direction x')
ax.set_ylabel('Direction y')
ax.set_zlabel('Direction z')

# Ajouter une légende et un titre
plt.title('Visualisation 3D des contraintes et déformations', fontsize=14)
plt.legend()
plt.colorbar(sc, label='Contrainte (Pa)')

plt.show()
