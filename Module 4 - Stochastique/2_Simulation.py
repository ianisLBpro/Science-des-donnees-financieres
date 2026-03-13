'''
2_Simulation

La simulation de Monte Carlo (MCS) est une technique de modélisation qui utilise des méthodes statistiques 
pour simuler le comportement d'un système ou d'un processus complexe.
Elle fait partie des techniques numériques fondamentales en finance et c'est peut-être la plus utilisée. 

C'est la plus souple lorsqu'il s'agit d'évaluer des expressions mathématiques telles que des intégrales, 
notamment pour évaluer des produits dérivés financiers. 

Le problème est que la charge de traitement est importante, il faut réaliser des centaines de milliers 
ou des millions de calculs complexes pour aboutir à une seule valeur estimée. 
'''

import math 
import numpy as np 
import numpy.random as npr
from pylab import plt, mpl

plt.style.use('seaborn-v0_8')
mpl.rcParams['font.family'] = 'serif'
npr.seed(100)
np.set_printoptions(precision=4)


'''
Exercice 1 : Simulation statique d'une mouvement brownien géometrique (GBM) avec npr.standard_normal()
Partons de la configuration d'évaluation d'option Black-Scholes-Merton (BSM). 

La valeur d'un indice d'action St à une date future T en partant d'un niveau d'indice actuel S0 
est obtenue avec l'équation suivante :

    S_T = S0 * exp((r - 0.5 * sigma**2) * T + sigma * sqrt(T) * z)

où :
S_T    : Niveau d'indice à la date T
S0     : Niveau actuel de l'indice
r      : Taux court sans risque constant
sigma  : Volatilité constante de S (écart-type de rentabilité)
T      : Horizon temporel
z      : Variable aléatoire en distribution standard normale

Dans cet exercice, nous verrons que la distribution aléatoire de la variable définie suit la loi log-normale. 
'''

# Le niveau initial de l'indice
S0 = 100
# Le taux sans risque court constant
r = 0.05
# Le facteur de volatilité constant 
sigma = 0.25
# L'horizon en fraction d'années 
T = 2.0
# Le nombre de simulations 
I = 10000  
# La simulation en tant qu'expression vectorisée. La discrétisation utilise la fonction npr.standard_normal() 
ST1 = S0 * np.exp((r - 0.5 * sigma**2) * T +
                   sigma * math.sqrt(T) * npr.standard_normal(I))

plt.figure(figsize=(10, 6))
plt.hist(ST1, bins=50)
plt.title("Simulation statique d'un GBM avec npr.standard_normal()")
plt.xlabel("Index Level")
plt.ylabel("Frequency")
plt.show()




'''
Exercice 2 : Simulation statique d'une mouvement brownien géometrique (GBM) avec npr.lognormal()
Comme nous l'avons vu dans le chapitre précédent, la variable aléatoire définie par l'équation du GBM suit une distribution log-normale.
Nous pouvons donc recourir à la fonction npr.lognormal() pour obtenir directement les valeurs de la variable. 
Il faut fournir la moyenne et l'écart-type de la distribution 
normale sous-jacente, soit (r - 0.5 * sigma**2) * T et sigma * sqrt(T).
'''

# Simulation par expression vectorisée, la discrétisation utilise la fonction npr.lognormal()
ST2 = S0 * npr.lognormal((r - 0.5 * sigma ** 2) * T, sigma * math.sqrt(T), size=I)

plt.figure(figsize=(10, 6))
plt.hist(ST2, bins=50)
plt.title("Simulation statique d'un GBM avec npr.lognormal()")
plt.xlabel("Index Level")
plt.ylabel("Frequency")
plt.show()




'''
Exercice 3 : Vérification par comparaison des deux méthodes de simulation
Dans cet exercice nous allons comparer les résultats obtenus par les deux méthodes de simulation.
Nous utiliserons pour cela le sous-paquetage stats de SciPy et 
d'une fonction de support print_statistics() que nous allons définir. 

Les statistiques des deux simulations sont très proches, elles se distinguent par ce que 
l'on appelle <<l'erreur d'échantillonnage>> ou de <<tirage>>.

Une autre erreur peut apparaître lorsqu'on cherche à simuler de façon discrète des processus stochastiques continus, 
c'est l'erreur de discrétisation.

Elle ne joue aucun rôle ici parce que l'approche de simulation est ici statique. 
'''

import scipy.stats as scs

def print_statistics(a1, a2):
    '''
    Affiche des statistiques choisies.

    Paramètres
    ==========
    a1, a2 : objets ndarray
        produits de la simulation
    '''

# La fonction scs.describe() renvoie des statistiques très utiles à propos d'un jeu de données. 
    sta1 = scs.describe(a1)
    sta2 = scs.describe(a2)
    print('%14s %14s %14s' % ('statistiques', 'data set 1', 'data set 2'))
    print(45 * '-')
    print('%14s %14.3f %14.3f' % ('size',     sta1[0],              sta2[0]))
    print('%14s %14.3f %14.3f' % ('min',      sta1[1][0],           sta2[1][0]))
    print('%14s %14.3f %14.3f' % ('max',      sta1[1][1],           sta2[1][1]))
    print('%14s %14.3f %14.3f' % ('mean',     sta1[2],              sta2[2]))
    print('%14s %14.3f %14.3f' % ('std',      np.sqrt(sta1[3]),     np.sqrt(sta2[3])))
    print('%14s %14.3f %14.3f' % ('skew',     sta1[4],              sta2[4]))
    print('%14s %14.3f %14.3f' % ('kurtosis', sta1[5],              sta2[5]))

# Appel
print_statistics(ST1, ST2)




'''
Exercice 4 : Simulation de processus stochastiques

'''
