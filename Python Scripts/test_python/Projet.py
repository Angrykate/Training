import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Paramètres du circuit
R = 1000  # Résistance en ohms
L = 0.1   # Inductance en henrys
C = 1e-6  # Capacité en farads

# Équation différentielle
def rlc_parallel(t, y):
    v, dv = y
    d2v = - (1 / (R * C)) * dv - (1 / (L * C)) * v
    return [dv, d2v]

# Conditions initiales
v0 = 5.0  # Tension initiale en volts
dv0 = 0.0  # Dérivée initiale de la tension
y0 = [v0, dv0]

# Temps de simulation
t_span = (0, 0.01)  # Intervalle de temps en secondes
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Résolution de l'équation différentielle
solution = solve_ivp(rlc_parallel, t_span, y0, t_eval=t_eval)

# Extraction des résultats
t = solution.t
v = solution.y[0]

# Affichage des résultats
plt.figure(figsize=(10, 6))
plt.plot(t, v, label="Tension $v(t)$")
plt.title("Réponse en régime libre du circuit RLC parallèle")
plt.xlabel("Temps (s)")
plt.ylabel("Tension (V)")
plt.grid()
plt.legend()
plt.show()

# Équation différentielle du système
def rlc_parallel(t, y):
    i, di_dt = y
    d2i_dt2 = -(R / L) * di_dt - (1 / (L * C)) * i
    return [di_dt, d2i_dt2]

# Conditions initiales
i0 = 0.0  # Intensité initiale
di_dt0 = 0.0  # Dérivée initiale de l'intensité
y0 = [i0, di_dt0]

# Plage de temps pour la simulation
t_span = (0, 0.05)  # De 0 à 50 ms
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Résolution numérique de l'EDO
solution = solve_ivp(rlc_parallel, t_span, y0, t_eval=t_eval, method='RK45')

# Extraction des résultats
t = solution.t
i = solution.y[0]

# Visualisation des résultats
plt.figure(figsize=(8, 5))
plt.plot(t, i, label="Courant $i(t)$", color='blue')
plt.title("Réponse d'un circuit RLC parallèle")
plt.xlabel("Temps (s)")
plt.ylabel("Intensité (A)")
plt.grid()
plt.legend()
plt.show()