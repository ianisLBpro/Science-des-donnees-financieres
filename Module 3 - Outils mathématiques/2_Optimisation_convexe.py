'''
L'optimisation convexe joue un grand rôle aussi bien en finance qu'en sciences économiques. 
Elle sert par exemple au calibrage des modèles d'évaluation d'options en fonction des données du marché 
ou à l'optimisation d'une fonction utilitaire. 

'''

import numpy as np 
from pylab import plt, mpl 
from mpl_toolkits.mplot3d import Axes3D

plt.style.use('seaborn-v0_8')
mpl.rcParams['font.family'] = 'serif'


# Définition de la fonction fm()
def fm(p):
    x, y = p 
    return (np.sin(x) + 0.05 * x ** 2 + np.sin(y) + 0.05 * y ** 2)

'''
Exercice 1 : Interpolation par splines linéaires 3D (sous-ensemble des données)
Utilisez la fonction fm() pour créer une grille de points (x, y) et calculer les valeurs correspondantes de fm(x, y).

'''

x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)
Z = fm((X, Y))

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(projection='3d') 
surf = ax.plot_surface(X, Y, Z, rstride=2, cstride=2, cmap='coolwarm', linewidth=0.5, antialiased=True)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.title('Interpolation par splines linéaires 3D')
plt.show()

