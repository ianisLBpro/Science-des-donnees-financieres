'''
L'optimisation convexe joue un grand rôle aussi bien en finance qu'en sciences économiques. 
Elle sert par exemple au calibrage des modèles d'évaluation d'options en fonction des données du marché ou à l'optimisation d'une fonction utilitaire. 

Nous allons utiliser tour à tour une minimisation globale puis une minimisation locale en utilisant les fonctions de la bibliothèque SciPy.optimize :
- sco.brute() pour la minimisation globale
- sco.fmin() pour la minimisation locale
'''


import numpy as np 
from pylab import plt, mpl 
from mpl_toolkits.mplot3d import Axes3D
import scipy.interpolate as spi

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




'''
Exercice 2 : Optimisation globale
Pour mieux visualiser les traitements réalisés pendant les minimisations,
nous allons améliorer le code de la fonction en ajoutant une option pour afficher les valeurs actuelles des paramètres et de la fonction.
La lecture des résultats permet de détecter que les valeurs de paramètres optimales en fonction des paramètres initaux de la fonction correspondent à x = y = 0.
Dans ce cas, la valeur de la fonction résultante est égale elle aussi à 0. 
On pourrait considérer que c'est le minimum global, mais le paramètrage dans cet exercice est assez grossier avec des étapes de 5 pour les deux paramètres d'entrée.
Nous verrons dans l'exercice 2.1 comment travailler de façon plus précise afin d'obtenir de meilleurs résultats.
'''

# Import du sous-paquetage requis de SciPy pour l'optimisation globale
import scipy.optimize as sco

# Information à afficher lorsque output = True : les valeurs actuelles de x, y et z à chaque évaluation de la fonction
def fo(p):
    x, y = p
    z = np.sin(x) + 0.05 * x ** 2 + np.sin(y) + 0.05 * y ** 2
    if output == True:
        print('%8.4f | %8.4f | %8.4f' % (x, y, z))
    return z
output = True

print("\n" + "=" * 60)
print(" EXERCICE 2 : Optimisation globale (grille grossière, pas=5) ")
print("=" * 60)
print(f"{'x':>8} | {'y':>8} | {'f(x,y)':>8}")
print("-" * 32)

# Opimisation par force brute : on évalue la fonction fo() sur une grille de points définie par les intervalles et les pas spécifiés
sco.brute(fo, ((-10, 10.1, 5), (-10, 10.1, 5)), finish=None)




'''
Exercice 2.1 : Optimisation globale avec une grille plus fine
Dans cet exercice, nous allons utiliser une grille plus fine pour l'optimisation globale.
Les valeurs de paramètres optimales sont dorénavant x = y = -1.4 et la valeur de minimale de fonction pour la minimisation globale est d'environ -1.8.
'''

output = False 
print("\n" + "=" * 60)
print(" EXERCICE 2.1 : Optimisation globale (grille fine, pas=0.1) ")
print("=" * 60)
opt1 = sco.brute(fo, ((-10, 10.1, 0.1), (-10, 10.1, 0.1)), finish=None)
print(f"  Paramètres optimaux (x, y) : {opt1}")
print(f"  Valeur minimale de f(x, y)  : {fm(opt1):.6f}")




'''
Exercice 3 : Optimisation locale
Dans cet exercice, nous allons exploiter les résultats de l'optimisation globale pour réaliser un optimisation convexe locale. 
Nous utiliserons donc la fonction sco.fmin() qui attend en entrée la fonction à minimiser et les valeurs de paramètres initiales. 
Les valeurs en option correspondent à la tolérance des paramètres d'entrée et la tolérance de la valeur de la fonction, 
sans oublier le nombre maximal d'itérations et d'appels de fonction. Cette optimisation améliore encore les résultats obtenus.
'''

output = True 

print("\n" + "=" * 60)
print(" EXERCICE 3 : Optimisation locale (sco.fmin) ")
print("=" * 60)
print(f"{'x':>8} | {'y':>8} | {'f(x,y)':>8}")
print("-" * 32)

# Procédure d'optimisation convexe locale, maxiter est limité ainsi que maxfun pour la pédagogie, mais on pourrait les augmenter pour de meilleurs résultats
opt2 = sco.fmin(fo, opt1, xtol=0.001, ftol=0.001, maxiter=15, maxfun=20)
print(f"\n  Paramètres optimaux (x, y) : {opt2}")
print(f"  Valeur minimale de f(x, y)  : {fm(opt2):.6f}")




'''
Exercice 3.1 : Valeur minimale supérieure à zéro 
Dans les problèmes d'optimisation complexe, il est souvent conseillé de commencer par la minimisation globale,
car la minimisation locale se fonde sur un algorithme qui peut facilement tomber dans le piège d'un minimum local relatif ignorant d'autres minimums locaux. 
Dans cet exercice, nous montrons que les paramètres de départ x = y = 2 fait aboutir à une valeur minimale supérieure à zéro. 
'''

output = False 
print("\n" + "=" * 60)
print(" EXERCICE 3.1 : Optimisation locale depuis (2, 2) ")
print("=" * 60)
result31 = sco.fmin(fo, (2.0, 2.0), maxiter=250)
print(f"  Paramètres optimaux (x, y) : {result31}")
print(f"  Valeur minimale de f(x, y)  : {fm(result31):.6f}")




'''
Exercice 4 : Optimisation contrainte 
Nous allons modéliser et résoudre le problème d'un investisseur. 

Il peut investir dans 2 actifs risqués au même prix aujourd'hui de 10 USD : 
- L'actif a gain dans 1 an (état u) = 15 USD ou gain dans 1 an (état d) = 5 USD
- L'actif b gain dans 1 an (état u) = 5 USD ou gain dans 1 an (état d) = 12 USD
- Probabilité de l'état u = 0.5 et probabilité de l'état d = 0.5

L'investisseur possède un budget w = 100 USD et il doit décider de la quantité à investir dans chacun des actifs.
Il veut maximiser son utilité espérée, c'est-à-dire son bien-être moyen en tenant compte des différents scénarios possibles.

On cherche les quantités a et b (nombre de titres achetés) qui maximisent :
E[u(w)] = 0.5 * √w_u + 0.5 * √w_d

Avec les contraintes suivantes :
w_u = a*15 + b*5 → richesse si état u
w_d = a*5 + b*12 → richesse si état d
a*10 + b*10 ≤ 100 → on ne peut pas dépenser plus que le budget
a, b ≥ 0 → on ne peut pas vendre à découvert

Nous pouvons donc résoudre ce problème avec scipy.optimize.minimize().
Cette fonction attend en entrée la fonction à minimiser et les conditions sous forme d'égalité ou d'inégalité (une liste d'objets dict).
Elle ne sait que minimiser donc on transforme :
maximiser E[u] ⟺ minimiser -E[u]

C'est pourquoi la fonction Python retourne une valeur négative.
'''

import math 


# La fonction à minimiser pour maximiser l'utilité espérée
def Eu(p):
    s, b = p
    return -(0.5 * math.sqrt(s * 15 + b * 5) +
             0.5 * math.sqrt(s * 5  + b * 12))

# La contrainte d'inégalité : le coût total de l'investissement ne doit pas dépasser le budget (sous forme dict)
cons = ({'type': 'ineq', 'fun': lambda p: 100 - p[0] * 10 - p[1] * 10})

# Les bornes : s et b entre 0 et 1000 (pas de vente à découvert)
bnds = ((0, 1000), (0, 1000))

print("\n" + "=" * 60)
print(" EXERCICE 4 : Optimisation contrainte (portefeuille optimal) ")
print("=" * 60)

# L'optimisation en partant du point initial [5, 5]
result = sco.minimize(Eu, [5, 5], method='SLSQP', bounds=bnds, constraints=cons)
print("\n--- Résultat complet de l'optimiseur ---")
print(result)

print("\n--- Résumé des résultats ---")
# Les valeurs des paramètres optimaux, autrement dit le portefeuille optimal
print(f"  Quantités optimales  → Actif A : {result['x'][0]:.4f} titres | Actif B : {result['x'][1]:.4f} titres")

# En pourcentage, on peut calculer les poids de chaque actif dans le portefeuille optimal
weights = result['x'] * 10 / 100  
print(f"  Poids dans le portfolio → Actif A : {weights[0]*100:.2f}% | Actif B : {weights[1]*100:.2f}%")

# La valeur de fonction minimale négative en tant que valeur de solution optimale
print(f"  Utilité espérée maximale E[u(w)] : {-result['fun']:.6f}")

# Toute la richesse est investie 
print(f"  Budget total investi : {np.dot(result['x'], [10, 10]):.2f} USD (budget = 100 USD)")





