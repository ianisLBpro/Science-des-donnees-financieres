'''
Recherche_nb_Pi.py

L'algorithme pour ce projet s'inspire de celui de la simulation de Monte Carlo et va permettre de trouver une partie des décimales du nombre π.

Nous savons que la superficie, c'est à dire l'aire "A" d'un cercle est obtenur par la formule A = π * r^2. 
En conséquence, π = A / r^2. Pour un cercle de rayon r = 1, Pi est donc égal à A. 

Notre algorithme va simuler la mise en place de points au hasard avec les coordonnées x, y, sachant que x et y font partie de l'intervalle [-1, 1].
Le carré autour d'un cercle inscrit a donc une longueur de côté de 2, donc une aire de 4. 

L'aire du cercle inscrit est donc inférieure à cette valeur, et nous permet de l'estimer par une méthode de Monte Carlo. 

L'algorithme va générer un nombre de points aléatoires dans le carré, et compter le nombre de points qui tombent à l'intérieur du cercle.
Puis nous diviserons le nombre de points dans le cercle par le nombre total de points. 
'''



import random  
import numpy as np
from pylab import mpl, plt
import numba
import time


# Configuration de l'affichage des graphiques
plt.style.use('seaborn-v0_8')
mpl.rcParams['font.family'] = 'serif'

print(f'\nValeur réelle de π : {np.pi:.5f}')




'''
Exercice 1 : Estimation de π par la méthode de Monte Carlo et visualisation des points aléatoires
'''

print("\n" + "="*100)
print("Exercice 1 : Estimation de π par la méthode de Monte Carlo et visualisation des points aléatoires")
print("="*100)

# Génération de points aléatoires (10_000) dans le carré [-1, 1] x [-1, 1]
rn = [(random.random() * 2 - 1, random.random() * 2 - 1)
      for _ in range(10_000)]

# Conversion en tableau NumPy pour faciliter les opérations
rn = np.array(rn)
print(rn[:5])  

# Visualisation des points et du cercle inscrit
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(1,1,1)
# Tracé le cercle unité 
circ = plt.Circle((0, 0), radius=1, edgecolor='g', lw=2.0, facecolor='None')
# Tracé le carré de côté 2
box = plt.Rectangle((-1, -1), 2, 2, edgecolor='b', alpha=0.3)
# Tracé le cercle unité 
ax.add_patch(circ)
# Tracé le carré de côté 2
ax.add_patch(box)
# Dépose les points aléatoires
plt.plot(rn[:, 0], rn[:, 1], 'r.')
# Configuration des limites, axes et du titre
plt.ylim(-1.1, 1.1)
plt.xlim(-1.1, 1.1)
plt.xlabel('x')
plt.ylabel('y') 
plt.title('Points aléatoires dans un carré et un cercle inscrit')
plt.grid()
plt.show()

# Distances des points à l'origine (0, 0)
distances = np.sqrt(rn[:, 0]**2 + rn[:, 1]**2)
# Comptage des points qui tombent à l'intérieur du cercle (distance <= 1)
points_dans_cercle = np.sum(distances <= 1)
# Estimation de π en multipliant la fraction de points dans le cercle par l'aire du carré (4)
pi_estime = 4 * points_dans_cercle / len(rn)
print(f'\nNombre de points : {len(rn)}')
print(f'Points dans le cercle : {points_dans_cercle}')
print(f'Fraction de points dans le cercle : {points_dans_cercle / len(rn):.5f}')
print(f'Estimation de π : {pi_estime:.5f}')




'''
Exercice 2 : Estimation de π avec une fonction Python
'''

print("\n" + "="*70)
print("Exercice 2 : Estimation de π avec une fonction Python ")
print("="*70)

n = 10_000_000
def mcs_pi_py(n):
    circle = 0 
    for _ in range(n):
        x, y = random.random(), random.random()
        if (x ** 2 + y **2) ** 0.5 <= 1:
            circle += 1
    return 4 * circle / n

t0 = time.time()
print(f'\nEstimation de π avec fonction Python et {n} points : {mcs_pi_py(n):.5f}')
print(f'Temps de calcul : {time.time() - t0:.5f} secondes')




'''
Exercice 3 : Estimation de π avec Numpy 
'''

print("\n" + "="*70)
print("Exercice 3 : Estimation de π avec Numpy")
print("="*70)

# Génération de points aléatoires avec Numpy
n = 10_000_000
# Génération de points aléatoires dans le carré [-1, 1] x [-1, 1]
rn = np.random.random((n, 2)) * 2 - 1
# Calcul des distances à l'origine en norme euclidienne pour tous les points
distance = np.sqrt((rn ** 2).sum(axis=1))
distance[:8].round(3)
# Comptage des points qui tombent à l'intérieur du cercle 
frac = (distance <= 1.0).sum() / len(distance)
# Estimation de π en multipliant la fraction de points dans le cercle par l'aire du carré (4)
pi_mcs = frac * 4
print(f'\nNombre de points : {n}')
print(f'Points dans le cercle : {(distance <= 1.0).sum()}')
print(f'Fraction de points dans le cercle : {frac:.5f}')
t0 = time.time()
print(f'Estimation de π avec Numpy et {n} points : {pi_mcs:.5f}')
print(f'Temps de calcul : {time.time() - t0:.5f} secondes')




'''
Exercice 4 : Estimation de π avec Numba 
'''

print("\n" + "="*70)
print("Exercice 4 : Estimation de π avec Numba")
print("="*70)

mcs_pi_nb = numba.jit(mcs_pi_py)
t0 = time.time()
print(f'\nEstimation de π avec Numba et {n} points : {mcs_pi_nb(n):.5f}')
print(f'Temps de calcul : {time.time() - t0:.5f} secondes')





