'''
1_Nombres_aleatoires 

Dans ce chapitre nous allons voir comment générer des valeurs aléatoires¹  en Python. 
Nous allons utiliser les fonctions proposées par le sous-paquetage numpy.random. 

Par exemple, la fonction la plus simple rand(), renvoie des valeurs aléatoires situées dans l'intervalle ouvert [0, 1), 
selon la forme fournie en paramètre et stocke le résultat dans un objet de type ndarray. 
On peut facilement transformer ces valeurs pour les adapter à d'autres intervalles.

Autres exemples, pour couvrir l'intervalle [a, b) = [5, 10), il suffit de transformer les valeurs générées par npr.rand() comme suit :
- npr.rand() * (b - a) + a
Notons que cela fonctionne dans plusieurs dimensions grâce au comportement de diffusion de numpy.

Le tableau dans le fichier 1.1_Generateur_aleatoire_simple.py nous dresse la liste 
de toutes les fonctions disponibles pour générer des valeurs pseudo-aléatoires. 


¹ Pour simplifier nous employons l'expression "valeurs aléatoires" alors que ce sont des valeurs pseudo-aléatoires.
'''

import math 
import numpy as np 
import numpy.random as npr
from pylab import plt, mpl

plt.style.use('seaborn-v0_8')
mpl.rcParams['font.family'] = 'serif'


# Fixe la valeur du germe (seed) afin de reproduire toujours la même série de valeurs aléatoires
npr.seed(100) 
# set_printoptions() est une fonction de numpy qui permet de définir le nombre de chiffres à afficher 
np.set_printoptions(precision=4)
# Production de valeurs aléatoires pour un objet ndarray à une dimension
print("Génération de 10 nombres aléatoires :")
print(npr.rand(10))
# Production de valeurs aléatoires pour un objet ndarray à deux dimensions
print("\nGénération d'une matrice 5x5 de nombres aléatoires :")
print(npr.rand(5,5))

a = 5   # borne inférieure de l'intervalle
b = 10  # borne supérieure de l'intervalle
# Transformation des valeurs générées par npr.rand() pour les adapter à l'intervalle [a, b)
print(f"\nGénération de 10 nombres aléatoires dans l'intervalle [{a}, {b}) :")
print(npr.rand(10) * (b - a) + a)
# Transformation des valeurs générées par npr.rand() pour les adapter à l'intervalle [a, b) dans plusieurs dimensions
print(f"\nGénération d'une matrice 5x5 de nombres aléatoires dans l'intervalle [{a}, {b}) :")
print(npr.rand(5,5) * (b - a) + a)




''' 
Exercice 1 : Visualisation d'histogramme de quelques générations aléatoires
Nous allons visualiser les résultats pour deux distributions continues et deux distributions discrètes, discontinues. 

L'utilisation de distributions en loi normale ou standard fait l'objet de nombreuses critiques,
mais cela reste une approche indispensable et elle est toujours la plus utilisée aussi bien en analyse que dans les applications numériques.

Une des raisons principales est la dépendance de nombreux modèles financiers d'une distribution normale ou log-normale
Les modèles qui ne dépendent pas directement de cette hypothèse peuvent être discrétisés 
et donc produire une approximation de simulation en s'appuyant sur une distribution normale. 

Le tableau dans le fichier 1.2_Generation_aleatoires_loi_de_distribution.py nous dresse la liste 
de toutes les fonctions disponibles pour générer les valeurs aléatoires en fonction de différentes distributions.
'''

sample_size = 500
# Valeurs aléatoires en distribution uniforme
rn1 = npr.rand(sample_size, 3)
# Valeurs entières pour un intervalle spécifié 
rn2 = npr.randint(0, 10, sample_size)
# Valeurs aléatoires en distribution uniforme
rn3 = npr.sample(size=sample_size)
# Sélection aléatoire de valeurs depuis un objet fini de type list
a = [0, 25, 50, 75, 100]
rn4 = npr.choice(a, size=sample_size)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows = 2, ncols = 2, figsize=(10, 8))
plt.suptitle("Histogrammes de générations aléatoires", fontsize=16)
ax1.hist(rn1, bins=25, stacked=True)
ax1.set_title("rand")
ax1.set_ylabel("Frequency")
ax2.hist(rn2, bins=25)
ax2.set_title("randint")
ax3.hist(rn3, bins=25)
ax3.set_title("sample")
ax3.set_ylabel("Frequency")
ax4.hist(rn4, bins=25)
ax4.set_title("choice")

plt.tight_layout()
plt.show()




'''
Exercice 2 : Histogramme pour quatre distributions différentes
Nous allons montrer ce que produisent trois distributions continues et la distribution discrète de Poisson. 

La distribution de Poisson est un modèle de comptage qui décrit la probabilité d'un nombre donné d'événements 
se produisant dans un intervalle de temps ou d'espace fixe, si ces événements se produisent avec une moyenne 
constante et indépendamment du temps écoulé depuis le dernier événement.

Elle permet de simuler la survenue d'un événement externe rare tel qu'un saut brutal dans le prix d'un instrument financier,
ou un choc extérieur. 
'''

sample_size = 500
# Standard normale (gaussienne centrée réduite) avec une moyenne de 0 et un écart type de 1
rn1 = npr.standard_normal(sample_size)
# Normale avec une moyenne de 100 et un écart type de 20
rn2 = npr.normal(100 , 20, sample_size)
# Khi carré avec 0.5 degrés de liberté
rn3 = npr.chisquare(df=0.5, size=sample_size)
# Poisson avec un lambda de 1.0
rn4 = npr.poisson(lam=1.0, size=sample_size)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows = 2, ncols = 2, figsize=(10, 8))
plt.suptitle("Histogrammes pour 4 distributions différentes", fontsize=16)
ax1.hist(rn1, bins=25)
ax1.set_title("standard normal")
ax1.set_ylabel("Fréquence")
ax2.hist(rn2, bins=25)
ax2.set_title("normal(100, 20)")
ax3.hist(rn3, bins=25)
ax3.set_title("chi-square")
ax3.set_ylabel("Frequency")
ax4.hist(rn4, bins=25)
ax4.set_title("Poisson")

plt.tight_layout()
plt.show()



'''
Numpy et valeurs aléatoires :
Ce chapitre nous a montré que NumPy constituait un outil puissant et indispensable pour générer des valeurs pseudo-aléatoires en Python.
Ce paquetage permet de générer de très grands objets ndarray contenant de telles valeurs. 
'''