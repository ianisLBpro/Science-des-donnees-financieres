#
# Test du tracé 2D statiques avec Matplotlib
#
#
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

print(mpl.__version__)

### Tracé 2D simple ###
sns.set_style("whitegrid")              # Style avec grille blanche
mpl.rcParams['font.family'] = 'serif'   # Police avec empattements

np.random.seed(1000)                    # Pour la reproductibilité
y = np.random.standard_normal(20)       # Données aléatoires
x = np.arange(len(y))                   # Abscisses
plt.plot(x, y)                          # Tracé simple
plt.show()

plt.plot(y.cumsum())                    # Tracé de la somme cumulée
plt.show()

plt.plot(y.cumsum())                    # Tracé avec style personnalisé de la grille et de l'échelle
plt.grid(False)                         # Désactive la grille
plt.axis('equal')                       # Mêmes échelles pour x et y
plt.show()

plt.plot(y.cumsum())                    # Tracé avec style personnalisé avec limites x et y
plt.xlim(-1, 20)                        # Limites de l'axe x
plt.ylim(np.min(y.cumsum()) -1, 
         np.max(y.cumsum()) +1)         # Limites de l'axe y
plt.show()

plt.figure(figsize=(10, 6))             # Taille de la figure
plt.plot(y.cumsum(), 'b', lw=1.5)       # Tracé avec taille personnalisée
plt.plot(y.cumsum(), 'ro')              # Points rouges
plt.xlabel('Index')                     # Label axe x
plt.ylabel('Value')                     # Label axe y
plt.title('Tracé simple')               # Titre du graphique
plt.show()


### Tracé 2D avec plusieurs séries ###
y = np.random.standard_normal((20, 2)).cumsum(axis=0) # Données aléatoires à 2D cumulées
plt.figure(figsize=(10, 6))             # Taille de la figure
plt.plot(y, lw=1.5)                     # Tracé avec taille personnalisée
plt.plot(y, 'ro')                       # Points rouges
plt.xlabel('Index')                     # Label axe x
plt.ylabel('Value')                     # Label axe y
plt.title('Tracé simple plusieurs séries') # Titre du graphique
plt.show()

### Tracé 2D avec plusieurs série avec légende ###
plt.figure(figsize=(10, 6))             # Taille de la figure
plt.plot(y[:, 0], lw=1.5, label='1st')  # Tracé avec taille personnalisée
plt.plot(y[:, 1], lw=1.5, label='2nd')  # Tracé avec taille personnalisée
plt.plot(y, 'ro')                       # Points rouges
plt.legend(loc=0)                       # Légende automatique
plt.xlabel('Index')                     # Label axe x
plt.ylabel('Value')                     # Label axe y
plt.title('Tracé simple plusieurs séries') # Titre du graphique
plt.show()


### Tracé 2D avec plusieurs série avec légende et échelle différente ###
# Modification de l'échelle de la première série
y[:, 0] = y[:, 0] * 100

plt.figure(figsize=(10, 6))             # Taille de la figure
plt.plot(y[:, 0], lw=1.5, label='1st')  # Tracé avec taille personnalisée
plt.plot(y[:, 1], lw=1.5, label='2nd')  # Tracé avec taille personnalisée
plt.plot(y, 'ro')                       # Points rouges
plt.legend(loc=0)                       # Légende automatique
plt.xlabel('Index')                     # Label axe x
plt.ylabel('Value')                     # Label axe y
plt.title('Tracé simple plusieurs séries') # Titre du graphique
plt.show()

### Pour résoudre le problème d'échelle, on utilise un second axe y ###
fig, ax1 = plt.subplots()
plt.plot(y[:, 0], 'b', lw=1.5, label='1st')  # Tracé avec taille personnalisée
plt.plot(y[:, 0], 'ro')                      # Points rouges
plt.legend(loc=8)                            # Légende automatique
plt.xlabel('Index')                          # Label axe x
plt.ylabel('Value 1st')                      # Label axe y
plt.title('Tracé simple plusieurs séries')   # Titre du graphique

ax2 = ax1.twinx()                            # Second axe y
plt.plot(y[:, 1], 'g', lw=1.5, label='2nd')  # Tracé avec taille personnalisée
plt.plot(y[:, 1], 'ro')                      # Points rouges
plt.legend(loc=0)                            # Légende automatique
plt.ylabel('Value 2nd')                      # Label axe y
plt.show()


### Tracé 2D avec 2 sous-tracés séparés ###
plt.figure(figsize=(10, 6))

plt.subplot(211)
plt.plot(y[:, 0], lw=1.5, label='1st')      # Tracé avec taille personnalisée
plt.plot(y[:, 0], 'ro')                     # Points rouges
plt.legend(loc=0)                           # Légende automatique
plt.ylabel('Value')                         # Label axe y
plt.title('Tracé simple')                   # Titre du graphique

plt.subplot(212)
plt.plot(y[:, 1], lw=1.5, label='2nd')      # Tracé avec taille personnalisée
plt.plot(y[:, 1], 'ro')                     # Points rouges 
plt.legend(loc=0)                           # Légende automatique
plt.xlabel('Index')                        # Label axe x
plt.ylabel('Value')                        # Label axe y
plt.show()


### Tracé combinant des lignes et des barres d'histogramme ###
plt.figure(figsize=(10, 6))

plt.subplot(121)
plt.plot(y[:, 0], 'b', lw=1.5, label='1st')  # Tracé avec taille personnalisée
plt.plot(y[:, 0], 'ro')                      # Points rouges
plt.legend(loc=0)                            # Légende automatique
plt.xlabel('Index')                          # Label axe x  
plt.ylabel('Value')                         # Label axe y
plt.title('1st data set')                   # Titre du graphique

plt.subplot(122)
plt.bar(np.arange(len(y)), y[:, 1], color='g', label='2nd') # Histogramme
plt.legend(loc=0)                            # Légende automatique
plt.xlabel('Index')                          # Label axe x
plt.title('2nd data set')                   # Titre du graphique
plt.show()










####################################### Exercice Final ############################################

### Tracé d'une fonction exponentielle ave la zone d'intégrale et les labels LaTeX ###

# Définition de la fonction exponentielle et des limites de l'intégrale
def func(x):
    return 0.5 * np.exp(x) + 1                    # Fonction exponentielle
a, b = 0.5, 1.5                                   # Limites de l'intégrale
x = np.linspace(0, 2)                             # Valeur x du tracé 
y = func(x)                                       # Valeur y du tracé
Ix = np.linspace(a, b)                            # Valeur de x pour les limites de l'intégrale
Iy = func(Ix)                                     # Valeur de y pour les limmites de l'intégrale
verts = [(a, 0)] + list(zip(Ix,Iy)) + [(b, 0)]    # Objet de type liste contenant plusieurs tuples (x,y) pour les coordonées du polygone


#Tracé de la fonction exponentielle
from matplotlib.patches import Polygon

fig, ax = plt.subplots(figsize=(10, 6))

plt.plot(x, y, 'b', linewidth=2)                        # Tracé des valeurs de la fonction par un trait bleu
plt.ylim(bottom=0)                                      # Définition de la valeur y minimale pour l'axe des ordonnées
poly = Polygon(verts, facecolor='0.7', edgecolor='0.5') # Tracé en gris du polygone de la zone d'intégrale
ax.add_patch(poly)                                      # Ajout du polygone au tracé
plt.text(0.5 * (a+b), 1, r'$\int_a^b f(x)\mathrm{d}x$', 
         horizontalalignment='center', fontsize=20)     # Ajout de la formule d'intégrale en LaTeX dans le tracé 
plt.figtext(0.9, 0.075, '$x$')                          # Ajout des labels d'axes 
plt.figtext(0.075, 0.9, '$f(x)$')                       # Ajout des labels d'axes 
ax.set_xticks((a, b))                                   # Ajout des lables x 
ax.set_xticklabels(('$a$', '$b$'))                      # Ajout des lables x 
ax.set_yticks([func(a), func(b)])                       # Ajout des lables y
ax.set_yticklabels(('$f(a)$', '$f(b)$'))                # Ajout des lables y
plt.title('Tracé d\'une fonction exponentielle avec intégrale')
plt.show()
