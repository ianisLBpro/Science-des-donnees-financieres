



import numpy as np 
from pylab import plt, mpl 

plt.style.use('seaborn-v0_8')
mpl.rcParams['font.family'] = 'serif'


### Exercice 1 : Approximation de fonctions ###

# La fonction f(x) que nous allons utiliser comporte un terme trigonométrique et un terme linéaire.
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


# Valeurs de x allant de -2π à 2π utilisées pour le tracé et les calculs de f(x).
x = np.linspace(-2 * np.pi, 2 * np.pi, 50) 

# Tracé de la fonction f(x) sur l'intervalle défini.
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

# La régression suivante est linéaire.
# Elle ne permettra pas de tenir compte de la partie trigonométrique sin de la fonction f(x).

# Nous allons utiliser un polynôme de degré 1 pour l'ajustement linéaire.
res = np.polyfit(x, f(x), deg=1, full=True)

# Résultats : paramètres, résidus, rang effectif, valeur singulière et valeurs de condition relatives.
print(res)

# Evaluation de la régression linéaire à partir des paramètres obtenus.
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
create_plot([x, x], [f(x), ry], ['b', 'r'], ['f(x)', 'Régression polynomiale de degré 5'], ['x', 'f(x)'])
plt.show()


# Polynôme de degré 7
reg = np.polyfit(x, f(x), deg=7)   
ry = np.polyval(reg, x)

# Vérification de l'approximation
print(np.allclose(f(x), ry))

# Calcul de l'erreur quadratique moyenne entre f(x) et l'approximation ry.
print(np.mean((f(x) - ry) ** 2))

create_plot([x, x], [f(x), ry], ['b', 'r'], ['f(x)', 'Régression polynomiale de degré 7'], ['x', 'f(x)'])
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

# Résolution du problème de moindres carrés pour trouver les paramètres de la régression.
reg = np.linalg.lstsq(matrix.T, f(x), rcond=None)[0]

# Paramètres de de régression optimale 
print(reg.round(4))                         

# Estimation de régression pour les valeurs de la fonction 
ry = np.dot(reg, matrix)
create_plot([x, x], [f(x), ry], ['b', 'r'], ['f(x)', 'Régression avec des monômes de degré 3'], ['x', 'f(x)'])
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

# Paramètres de régression optimaux afin qu'il recouvre la fonction. 
reg.round(4)
ry = np.dot(reg, matrix)
print(np.allclose(f(x), ry))

# Régression produit un ajustement parfait, l'erreur quadratique moyenne est donc nulle.
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





