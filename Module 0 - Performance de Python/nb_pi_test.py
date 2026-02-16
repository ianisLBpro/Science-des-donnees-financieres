# L'algorithme que nous allons découvrir s'inspire de la méthode de Monte Carlo et va permettre de trouver les décimales de π (pi).
# L'idée simple :
# Imaginez un carré avec un cercle inscrit à l'intérieur. Si vous lancez des fléchettes aléatoirement dans le carré, la proportion de fléchettes qui tombent dans le cercle vous dit quelque chose sur π.

# Les maths :

# Un carré 2×2 a une aire = 4
# Un cercle de rayon 1 a une aire = π
# Ratio : aire_cercle / aire_carré = π / 4
# Donc : π = 4 × (points_dans_cercle / points_totaux)
# Ce que le code fait :

# ✓ Génère 10000 points aléatoires dans le carré (-1 à 1)
# ✓ Calcule la distance de chaque point au centre (0,0)
# ✓ Compte combien de points sont à distance ≤ 1 (dans le cercle)
# ✓ Applique la formule : π ≈ 4 × (points_cercle / 10000)
# ✓ Affiche et compare avec la vraie valeur de π
# Pourquoi ça marche : Plus vous avez de points, meilleure est l'estimation ! C'est le hasard qui calcule π pour vous 😊


### Estimation de π par la méthode de Monte Carlo ###
import random  
import numpy as np
from pylab import mpl, plt 


# plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

rn = [(random.random() * 2 - 1, random.random() * 2 - 1)
      for _ in range(10000)]

rn = np.array(rn)
print(rn[:5])  # Affiche les 5 premiers points générés

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(1,1,1)
circ = plt.Circle((0, 0), 
                  radius=1, 
                  edgecolor='g', 
                  lw=2.0, 
                  facecolor='none')
box = plt.Rectangle((-1, -1), 2, 2, 
                    edgecolor='b',
                    alpha=0.3)
ax.add_patch(circ)
ax.add_patch(box)
plt.plot(rn[:, 0], rn[:, 1], 'r.')
plt.ylim(-1.1, 1.1)
plt.xlim(-1.1, 1.1)
plt.xlabel('x')
plt.ylabel('y') 
plt.title('Points aléatoires dans un carré et un cercle inscrit')
plt.grid()
plt.show()

# Calcul de π
distances = np.sqrt(rn[:, 0]**2 + rn[:, 1]**2)
points_dans_cercle = np.sum(distances <= 1)
pi_estime = 4 * points_dans_cercle / len(rn)

print(f'\nNombre de points : {len(rn)}')
print(f'Points dans le cercle : {points_dans_cercle}')
print(f'Estimation de π : {pi_estime:.4f}')
print(f'Valeur réelle de π : {np.pi:.4f}')


### Version avec Numpy ### 
n = int(1e7)
rn = np.random.random((n, 2)) * 2 - 1
distance = np.sqrt((rn ** 2).sum(axis=1))
distance[:0].round(3)
frac = (distance <= 1.0).sum() / len(distance)
pi_mcs = frac * 4
print(f'\nEstimation de π avec Numpy et {n} points : {pi_mcs:.4f}')


### Version simple en Python (plus lent)###
def mcs_pi_py(n):
    circle = 0 
    for _ in range(n):
        x, y = random.random(), random.random()
        if (x ** 2 + y **2) ** 0.5 <= 1:
            circle += 1
    return 4 * circle / n

print(f'\nEstimation de π avec fonction Python et {n} points : {mcs_pi_py(n):.4f}')



