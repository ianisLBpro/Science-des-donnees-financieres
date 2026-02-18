'''
Module 3 - Outils mathématiques.Approximation_Regression_Interpolation
Ce module couvre les concepts d'approximation, de régression et d'interpolation en utilisant des outils mathématiques.

Il comprend plusieurs exercices pratiques pour illustrer ces concepts :

- Exercice 1 : Approximation de fonctions (ligne 28)
- Exercice 2 : Régression linéaire (ligne 61)
- Exercice 3 : Régression avec monômes de degré 5 et 7 (ligne 100)
- Exercice 4 : Régression avec les fonctions de base individuelles (ligne 131)
- Exercice 5 : Régression avec les fonctions de base sinusoïdales (ligne 188)
- Exercice 6 : Régression avec des données d'entrées bruitées (ligne 227)
- Exercice 7 : Régression avec des données non triées (ligne 266)
- Exercice 8 : Régression avec des dimensions multiples (ligne 305)
- Exercice 9 : Surface de régression pour une fonction à deux paramètres (ligne 344)
- Exercice 10 : Interpolation par splines linéaires et cubiques (ligne 381)
''' 


# Importation des bibliothèques nécessaires pour les calculs numériques et la visualisation
import numpy as np 
from pylab import plt, mpl 

plt.style.use('seaborn-v0_8')
mpl.rcParams['font.family'] = 'serif'




### Exercice 1 : Approximation de fonctions ###

# La fonction f(x) que nous allons utiliser comporte un terme trigonométrique et un terme linéaire
def f(x):
    return np.sin(x) + 0.5 * x 

'''
Nous allons visualiser la fonction f(x) sur l'intervalle [-2π, 2π] pour mieux comprendre son comportement.
La fonction est présentée pour cet intervalle défini grâce à la fonction np.linspace().

La fonction create_plot() est utilisée pour tracer la courbe de f(x) avec des styles et des étiquettes spécifiques.
Elle nous servira également à tracer les mêmes graphiques à plusieurs reprises.
'''

def create_plot(x, y, styles, labels, axlabels):
    plt.figure(figsize=(10, 6))
    for i in range(len(x)):
        plt.plot(x[i], y[i], styles[i], label=labels[i])
        plt.xlabel(axlabels[0])
        plt.ylabel(axlabels[1])
    plt.legend(loc=0)


# Valeurs de x allant de -2π à 2π utilisées pour le tracé et les calculs de f(x)
x = np.linspace(-2 * np.pi, 2 * np.pi, 50) 

# Tracé de la fonction f(x) sur l'intervalle défini
create_plot([x], [f(x)], ['b'], ['f(x)', 'Tracé de la fonction f(x)'], ['x', 'f(x)'])
plt.show()




### Exercice 2 : Regression linéaire ###

'''
Un outil efficace pour l'approximation d'une fonction est la régression. 
Elle permet de travailler avec des fonctions à une ou à plusieurs dimensions. 

Une des approches les plus simples consiste à utiliser comme fonction de base des monômes. 
Exemple : b1 = 1, b2 = x, b3 = x^2, etc.

Des fonctions sont disponibles dans la bibliothèque NumPy pour déterminer les paramètres optimaux :
- np.polyfit() : pour les fonctions à une dimension
- np.polyval() : pour évaluer l'approximation à partir des paramètres obtenus

Paramètres de la fonction np.polyfit() :
- x : coordonnées x (valeur de variable indépendante)
- y : coordonnées y (valeur de variable dépendante)
- deg : degré du polynôme d'ajustement
- full : Si True, renvoie les informations de diagnostic
- w : Pondération pour les coordonnées y 
- cov : Si True, renvoie la matrice de covariance
'''

# La régression suivante est linéaire
# Elle ne permettra pas de tenir compte de la partie trigonométrique sin de la fonction f(x)

# Nous allons utiliser un polynôme de degré 1 pour l'ajustement linéaire
res = np.polyfit(x, f(x), deg=1, full=True)

# Résultats : paramètres, résidus, rang effectif, valeur singulière et valeurs de condition relatives
print(res)

# Evaluation de la régression linéaire à partir des paramètres obtenus
ry = np.polyval(res[0], x)
create_plot([x, x], [f(x), ry], ['b', 'r'], ['f(x)', 'Régression linéaire'], ['x', 'f(x)'])
plt.show()




### Exercice 3 : Régression avec monômes de degré 5 et 7 ###

'''
Pour prendre en compte la partie sinus de la fonction f(x), nous allons utiliser des monômes de degré supérieur.
Les deux prochaines tentatives montrerons les degrés 5 et 7 pour les fonctions de base. 
Nous verrons que les régressions résultantes épousent beaucoup mieux la fonction f(x).
'''

# Polynôme de degré 5 
reg = np.polyfit(x, f(x), deg=5)
ry = np.polyval(reg, x)
create_plot([x, x], [f(x), ry], ['b', 'r'], ['f(x)', 'Régression avec monômes de degré 5'], ['x', 'f(x)'])
plt.show()


# Polynôme de degré 7
reg = np.polyfit(x, f(x), deg=7)   
ry = np.polyval(reg, x)

# Vérification de l'approximation
print(np.allclose(f(x), ry))

# Calcul de l'erreur quadratique moyenne entre f(x) et l'approximation ry
print(np.mean((f(x) - ry) ** 2))

create_plot([x, x], [f(x), ry], ['b', 'r'], ['f(x)', 'Régression avec monômes de degré 7'], ['x', 'f(x)'])
plt.show()




### Exercice 4 : Régression avec les fonctions de base individuelles ###

'''
Dans cet exercice, nous allons tenter d'obtenir des résultats plus précis en utilisant les fonctions de base individuelles.

Pour cela, il faut à cette effet que les fonctions de base individuelles soient définies dans une approche matricielle. 
On utilisera donc un ndarray de NumPy pour stocker les fonctions de base individuelles évaluées aux points x.

La fonction principale utilisée pour cela est np.linalg.lstsq(), qui résout le problème de moindres carrés linéaires.
'''

# Exemple avec avec des monômes de degré 3
matrix = np.zeros((3 + 1, len(x)))                  # Objet ndarray servant de matrice pour les valeurs des fonctions de base
matrix[3, :] = x ** 3                               # Valeurs de fonctions de base de la constante à la cubique 
matrix[2, :] = x ** 2
matrix[1, :] = x
matrix[0, :] = 1

# Résolution du problème de moindres carrés pour trouver les paramètres de la régression
reg = np.linalg.lstsq(matrix.T, f(x), rcond=None)[0]

# Paramètres de de régression optimale 
print(reg.round(4))                         

# Estimation de régression pour les valeurs de la fonction 
ry = np.dot(reg, matrix)
create_plot([x, x], [f(x), ry], ['b', 'r'], ['f(x)', 'Régression avec des monômes de degré 3 (fonctions de base individuelles)'], ['x', 'f(x)'])
plt.show()




### Exercice 5 : Régression avec les fonctions de base sinusoïdales ###

'''
Le résultat avec des monômes de degré 3 n'est pas très satisfaisant, car il ne prend pas en compte la partie sin de la fonction f(x).

Nous allons donc tirer profit des connaissances au sujet de la fonction f(x), on sait qu'elle comporte une partie sinusoïdale.

Nous prévoyons donc de prévoir une fonction sinus dans les fonctions de base individuelles pour l'approximation. 

Le résultat est un ajustement parfait. 
'''

# Fonction de base sinusoïdale
matrix[3, :] = np.sin(x)
reg = np.linalg.lstsq(matrix.T, f(x), rcond=None)[0]

# Paramètres de régression optimaux afin qu'il recouvre la fonction 
reg.round(4)
ry = np.dot(reg, matrix)
print(np.allclose(f(x), ry))

# Régression produit un ajustement parfait, l'erreur quadratique moyenne est donc nulle
print(np.mean((f(x) - ry) ** 2))
create_plot([x, x], [f(x), ry], ['b', 'r'], ['f(x)', 'Régression avec des fonctions de base sinusoïdales'], ['x', 'f(x)'])
plt.show()




### Exercice 6 : Régression avec des données d'entrées bruitées ###

'''
Dans cet exercice, nous allons montrer que la régression fonctionne aussi avec des données d'entrée bruitées.

Nous générons des observations indépendantes bruitées et des observations dépendantes bruitées. 
Nous verrons que les résultats de la régression sont plus proches de la fonction de départ que les points bruités. 

La régression réalise une sorte de moyenne pour éliminer le bruit et se rapprocher de la fonction d'origine.
'''

# Nouvelles valeurs de x déterministes
xn = np.linspace(-2 * np.pi, 2 * np.pi, 50)

# Ajout de bruit dans les valeurs de x 
xn = xn + 0.15 * np.random.standard_normal(len(xn))

# Ajout de bruit dans les valeurs de y 
yn = f(xn) + 0.25 * np.random.standard_normal(len(xn))

# Régression avec des données d'entrée bruitées
reg = np.polyfit(xn, yn, 7)
ry = np.polyval(reg, xn)
create_plot([xn, xn], [yn, ry], ['b.', 'r'], ['Points bruités', 'Régression avec des données d\'entrées bruitées'], ['x', 'f(x)'])
plt.show()




### Exercice 7 : Régression avec des données non triées ###

'''
Nous allons montrer que la régression fonctionne aussi avec des données désordonnées.
Dans les exercices précédents, les données d'entrée étaient ordonnées, 
c'est-à-dire que les valeurs de x étaient triées mais ce n'est pas une condition nécessaire pour la régression.
'''

xu = np.random.rand(50) * 4 * np.pi - 2 * np.pi
yu = f(xu) 

print(xu[:10].round(2))  
print(yu[:10].round(2))

reg = np.polyfit(xu, yu, 5)
ry = np.polyval(reg, xu)

create_plot([xu, xu], [yu, ry], ['b.', 'ro'], ['f(x)', 'Régression avec des données non triées'], ['x', 'f(x)'])
plt.show()




### Exercice 8 : Régression avec des dimensions multiples ###

'''
L'approche par régression à moindres carrés offre un autre aspect intéressant qui est de pouvoir être transposé vers plusieurs dimensions.

Il est nécessaire de prévoir des grilles en deux dimendsions avec des points de données indépendants pour pouvoir visualiser cette fonction.

Ces deux grilles de points de données indépendants et dépendants seront incarnés par x, y et z. 
'''

# Fonction scalaire de deux variables (x, y) passées sous forme de tuple p = (x, y)
def fm(p):
    x, y = p
    return np.sin(x) + 0.25 * x + np.sqrt(y) +0.05 * y ** 2

# Génère des grilles ou objets ndarray en 2D à partir des ndarray en 1D
x = np.linspace(0, 10, 20)
y = np.linspace(0, 10, 20)
X, Y = np.meshgrid(x, y)

# Récupère des objets ndarray 1D à partir des objets ndarray 2D
Z = fm((X, Y))
x = X.flatten()
y = Y.flatten()

# Import des fonctions de visualisation 3D de Matplotlib
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=2, cstride=2, label='Régression dimensions multiples', cmap='coolwarm', linewidth=0.5, antialiased=True)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()




### Exercice 9 : Surface de régression pour une fonction à deux paramètres ###

'''
Dans cet exercice, nous allons faire une régression plus qualitative en utilisant les fonctions np.sin() et np.sqrt().
'''

matrix = np.zeros((len(x), 6 + 1))
matrix[:, 6] = np.sqrt(y)                       # Fonction np.sqrt() pour les paramètre y
matrix[:, 5] = np.sin(x)                        # Fonction np.sin() pour les paramètre x
matrix[:, 4] = y ** 2
matrix[:, 3] = x ** 2 
matrix[:, 2] = y
matrix[:, 1] = x
matrix[:, 0] = 1

reg = np.linalg.lstsq(matrix, fm((x, y)), rcond=None)[0]

# Transformation des résultats de régression en structure de grille
RZ = np.dot(matrix, reg).reshape((20, 20))      

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(projection='3d')

# Tracé de la surface de la fonction originale
surf1 = ax.plot_surface(X, Y, Z, rstride=2, cstride=2, cmap=mpl.cm.coolwarm, linewidth=0.5, antialiased=True)

# Tracé de la surface de régression
surf2 = ax.plot_wireframe(X, Y, RZ, rstride=2, cstride=2, label='Surface de régression dimensions multiples')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.legend()
fig.colorbar(surf1, shrink=0.5, aspect=5)
plt.show()




### Exercice 10 : Interpolation par splines linéaires et cubiques ###

'''
Dans cet exercice, nous allons faire de l'interpolation par splines cubiques, elle ne s'utilise que dans les problèmes à peu de dimensions.

En partant d'un jeu ordonné de points d'observation dans la dimension x, le principe est de faire une régression entre deux points de données voisins,
de manière à ce que les points soient trouvés par la fonction d'interpolation définie et que les points soient différenciable de façon continue.
Pour ce faire, il faut une interpolation au moins de degré 3, donc avec des splines cubiques.
Pour autant, l'approche est applicable avec des splines quadratiques ou même linéaires, mais les résultats sont moins satisfaisants.

Les interpolations splines sont souvent utilisées dans le domaine financier pour générer des estimations de valeurs dépendantes pour des points de données indépendants. 
Ces points de données indépendants ne font pas partie des observations fournies. 

L'inconvénient des splines linéaires est que la fonction ne peut pas être différenciables en continu au niveau des points de données originaux. 
'''

# Interpolation de splines linéaires #

# Import du sous-paquet Scipy pour l'interpolation
import scipy.interpolate as spi

# Valeurs de x allant de -2π à 2π utilisées pour le tracé et les calculs de f(x)
x = np.linspace(-2 * np.pi, 2 * np.pi, 25)

# Fonction f(x) que nous allons utiliser pour l'interpolation
def f(x):
    return np.sin(x) + 0.5 * x

# Implémente une interpolation de splines linéaires
ipo = spi.splrep(x, f(x), k=1)  

# Dérive de la valeur interpolées
iy = spi.splev(x, ipo)

# Vérfication que les valeurs interpolées sont assez proches des valeurs de la fonction
print(np.allclose(f(x), iy))

create_plot([x, x], [f(x), iy], ['b', 'ro'], ['f(x)', 'Interpolation par splines linéaires'], ['x', 'f(x)'])
plt.show()


# Interpolation par splines linéaires sur un sous-ensemble des données #

''' 
Pour l'interpolation, les fonctions portent les noms sci.splrep() et sci.splev(). 

Les principaux paramètres de sci.splrep() sont :
- x : Coordonnées x (ordonnées, valeurs des variables indépendantes)
- y : Coordonnées y (ordonnées en x, valeurs des variables dépendantes) 
- w : Pondération pour les coordonnées y
- xb, xe : Intervalle de l'ajustement; si None, alors [x[0], x[-1]]
- k : Degré de l'ajustement de spline (1 <= k <= 5)
- s : Facteur de lissage (lissage proportionnel à la valeur)
- full_output : Si True, renvoie des données additionnelles
- quiet : Si True, pas d'affichage des messages 

Les principaux paramètres de sci.splev() sont :
- x : Coordonnées x (ordonnées, valeurs des variables indépendantes)
- tck : Séquence de longueur 3 renvoyée par sci.splrep() (noeuds, coefficients, degrés)
- der : Ordre de dérivation (0 pour la fonction, 1 pour la première dérivée)
- ext : Comportement si x n'est pas dans la séquences de noeuds (0 = extrapolation, 1 = renvoi de 0 et 2 = déclenche ValueError)
'''

# Plus petit intervalle avec plus de points
xd = np.linspace(1.0, 3.0, 50)
iyd = spi.splev(xd, ipo)

create_plot([xd, xd], [f(xd), iyd], ['b', 'ro'], ['f(x)', 'Interpolation par splines linéaires sur un sous-ensemble des données'], ['x', 'f(x)'])
plt.show()


# Interpolation par splines cubiques sur un sous-ensemble des données #

'''
Les splines cubiques sont plus adaptées pour l'interpolation et donnent souvent de meilleurs résultats.

Lorsqu'il est possible d'utiliser l'interpolation splines, les résultats sont généralement meilleurs que les régressions MCO.
Il ne faut pas oublier que pour l'interpolation les données doivent être ordonnées, 
c'est-à-dire que les valeurs de x doivent être triées et non bruitées et nous sommes limités à des fonctions à peu de dimensions.
L'opération est également plus lourde en traitement et peut demander beaucoup plus de temps qu'une régression dans certains cas. 
'''

# Interpolation spline cubique sur le jeu de données complet
ipo = spi.splrep(x, f(x), k=3)

# Les résultats sont appliqués au petit intervalle 
iyd = spi.splev(xd, ipo)

# L'interpolation n'est toujours pas parfaite
print(np.allclose(f(xd), iyd))

# Mais elle est meilleure qu'auparavant, l'erreur quadratique moyenne est plus faible
print(np.mean((f(xd) - iyd) ** 2))

create_plot([xd, xd], [f(xd), iyd], ['b', 'ro'], ['f(x)', 'Interpolation par splines cubiques sur un sous-ensemble des données'], ['x', 'f(x)'])
plt.show()



