import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- CONFIGURATION DE LA SIMULATION ---
num_points = 15       # Nombre de maillons
segment_length = 0.4  # Distance maximale entre deux maillons
G = 0.3               # Constante gravitationnelle
mass = .01            # Masse de chaque maillon
num_iterations = 60   # Rigidité du fil
dt = 0.1              # Pas de temps

# Position initiale : une forme de U inversé dans le vide
th = np.linspace(0, np.pi, num_points)
x_coords = 2 * np.cos(th)
y_coords = 1 * np.sin(th)

positions = np.stack((x_coords, y_coords), axis=-1)
old_positions = positions.copy()

# --- PRÉPARATION DU GRAPHIQUE ---
fig, ax = plt.subplots(figsize=(7, 7))

# La chaîne (ligne violette et points noirs)
line, = ax.plot([], [], color='purple', linestyle='-', marker='o', markerfacecolor='black', markersize=6)

# Le Centre de Gravité (Gros point rouge)
cg_point, = ax.plot([], [], 'ro', markersize=10, label="Centre de Gravité")

# Configuration des axes
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_title("Chaîne dans le vide et son Centre de Gravité (Point Rouge)")
ax.grid(True)
ax.set_aspect('equal')
ax.legend(loc="upper right")

# --- FONCTION DE MISE À JOUR (Chaque frame) ---
def update(frame):
    global positions, old_positions
    
    # 1. Calcul des forces gravitationnelles mutuelles
    forces = np.zeros_like(positions)
    for i in range(num_points):
        for j in range(num_points):
            if i == j:
                continue
            delta_r = positions[j] - positions[i]
            dist = np.linalg.norm(delta_r)
            
            if dist < 0.1: 
                dist = 0.1  # Évite les divisions par zéro
                
            force_mag = G * (mass * mass) / (dist ** 2)
            forces[i] += force_mag * (delta_r / dist)

    # 2. Intégration de Verlet
    for i in range(num_points):
        temp = positions[i].copy()
        acceleration = forces[i] / mass
        positions[i] += (positions[i] - old_positions[i]) + acceleration * (dt ** 2)
        old_positions[i] = temp

    # 3. Contrainte du fil (rigidité)
    for _ in range(num_iterations):
        for i in range(num_points - 1):
            p1 = positions[i]
            p2 = positions[i + 1]
            
            delta = p2 - p1
            distance = np.linalg.norm(delta)
            
            if distance == 0:
                continue
                
            difference = segment_length - distance
            percent = (difference / distance) / 2
            offset = delta * percent
            
            positions[i] -= offset
            positions[i + 1] += offset

    # 4. Calcul du centre de gravité (Moyenne des positions X et Y)
    # Formule : CG = somme(position_i * masse_i) / somme(masses)
    # Comme toutes les masses sont égales à 1.0, c'est une simple moyenne :
    cg_x = np.mean(positions[:, 0])
    cg_y = np.mean(positions[:, 1])

    # 5. Mise à jour du graphique
    line.set_data(positions[:, 0], positions[:, 1])
    cg_point.set_data([cg_x], [cg_y])
    
    return line, cg_point

# --- LANCEMENT DE L'ANIMATION ---
ani = animation.FuncAnimation(fig, update, frames=200, interval=20, blit=True)

plt.show()
