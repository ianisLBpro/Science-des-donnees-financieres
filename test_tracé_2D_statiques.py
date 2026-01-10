#
#
# Tests tracés 2D statiques avec Matplotlib
#
#
#

### Importation des bibliothèques nécessaires ###
import matplotlib as mpl                                                 # Matplotilib pour les tracés
import matplotlib.pyplot as plt                                          # Module pyplot pour les tracés
import seaborn as sns                                                    # Seaborn pour le style des tracés
import numpy as np                                                       # NumPy pour les calculs numériques



# Configuration du style des tracés
sns.set_style("whitegrid")                                               # Style avec grille blanche
mpl.rcParams['font.family'] = 'serif'                                    # Police avec empattements


### Création de données aléatoires et des axes ###
np.random.seed(1000)                                                     # Ajout d'une graine pour la reproductibilité
y = np.random.standard_normal(20)                                        # Ajout des valeurs y en données aléatoires
x = np.arange(len(y))                                                    # Ajout des valeurs x correspondant aux indices des données y


### Tracés 2D statiques simple ###
plt.figure()                                                             # Création d'une nouvelle figure
plt.plot(x, y)                                                           # Tracé 2D statiquesimple
plt.title('Tracé 2D statique simple')                                    # Titre du graphique 
plt.show()


### Tracé 2D statique somme cumulée ###
plt.figure()                                                             # Création d'une nouvelle figure
plt.plot(y.cumsum())                                                     # Tracé de la somme cumulée des données aléatoires 
plt.title('Tracé 2D statique somme cumulée')                             # Titre du graphique
plt.show()


### Tracé 2D avec style et échelle personnalisé ### 
plt.figure()                                                             # Création d'une nouvelle figure
plt.plot(y.cumsum())                                                     # Tracé avec style personnalisé de la grille et de l'échelle
plt.grid(False)                                                          # Désactive la grille
plt.axis('equal')                                                        # Mêmes échelles pour x et y
plt.title('Tracé 2D avec style et échelle personnalisé')                 # Titre du graphique
plt.show()


### Tracé 2D avec limites d'axes spécifiques ###
plt.figure()                                                             # Création d'une nouvelle figure
plt.plot(y.cumsum())                                                     # Tracé avec style personnalisé avec limites x et y
plt.xlim(-1, 20)                                                         # Limites de l'axe x
plt.ylim(np.min(y.cumsum()) -1, 
         np.max(y.cumsum()) +1)                                          # Limites de l'axe y
plt.title("Tracé 2D avec limites d'axes spécifiques")                    # Titre du graphique
plt.show()


### Tracé 2D avec taille et labels personnalisée ###
plt.figure(figsize=(10, 6))                                              # Taille de la figure
plt.plot(y.cumsum(), 'b', lw=1.5)                                        # Tracé avec taille personnalis
plt.plot(y.cumsum(), 'ro')                                               # Points rouges
plt.xlabel('Index')                                                      # Label axe x
plt.ylabel('Value')                                                      # Label axe y
plt.title('Tracé 2D avec taille et labels personnalisée')                # Titre du graphique
plt.show() 


### Tracé 2D de deux jeux de données ###
y = np.random.standard_normal((20, 2)).cumsum(axis=0)                    # Données aléatoires pour deux séries cumulées
plt.figure(figsize=(10, 6))                                              # Taille de la figure
plt.plot(y, lw=1.5)                                                      # Tracé avec taille personnalisée
plt.plot(y, 'ro')                                                        # Points rouges
plt.xlabel('Index')                                                      # Label axe x
plt.ylabel('Value')                                                      # Label axe y
plt.title('Tracé 2D de deux jeux de donnée')                             # Titre du graphique
plt.show()


### Tracé 2D avec deux jeux de données avec légende ###
plt.figure(figsize=(10, 6))                                              # Taille de la figure
plt.plot(y[:, 0], lw=1.5, label='1st')                                   # Tracé avec taille personnalisée
plt.plot(y[:, 1], lw=1.5, label='2nd')                                   # Tracé avec taille personnalisée
plt.plot(y, 'ro')                                                        # Points rouges
plt.legend(loc=0)                                                        # Légende automatique
plt.xlabel('Index')                                                      # Label axe x
plt.ylabel('Value')                                                      # Label axe y
plt.title('Tracé simple avec deux jeux de données légendés')             # Titre du graphique
plt.show()


### Tracé 2D avec plusieurs série avec légende et échelle différente ###
y[:, 0] = y[:, 0] * 100                                                  # Redimensionnement de la première série pour créer un problème d'échelle
plt.figure(figsize=(10, 6))                                              # Taille de la figure
plt.plot(y[:, 0], lw=1.5, label='1st')                                   # label de sous jeu de données
plt.plot(y[:, 1], lw=1.5, label='2nd')                                   # label de sous jeu de données
plt.plot(y, 'ro')                                                        # Points rouges
plt.legend(loc=0)                                                        # Légende automatique
plt.xlabel('Index')                                                      # Label axe x
plt.ylabel('Value')                                                      # Label axe y
plt.title('Tracé 2D avec deux jeux de données et problèmes d\'échelle')  # Titre du graphique
plt.show()
# Pour résoudre le problème d'échelle, on utilise un second axe y #
fig, ax1 = plt.subplots(figsize=(10, 6))                                 # Taille de la figure
plt.plot(y[:, 0], 'b', lw=1.5, label='1st')                              # Tracé avec taille personnalisée
plt.plot(y[:, 0], 'ro')                                                  # Points rouges
plt.legend(loc=8)                                                        # Légende automatique
plt.xlabel('Index')                                                      # Label axe x
plt.ylabel('Value 1st')                                                  # Label axe y
plt.title('Tracé 2D avec deux jeux de données et résolution d\'échelle') # Titre du graphique
ax2 = ax1.twinx()                                                        # Création d'un second axe y
plt.plot(y[:, 1], 'g', lw=1.5, label='2nd')                              # Tracé avec taille personnalisée
plt.plot(y[:, 1], 'ro')                                                  # Points rouges
plt.legend(loc=0)                                                        # Légende automatique
plt.ylabel('Value 2nd')                                                  # Label axe y
plt.show()


### Tracé 2D avec 2 sous-tracés séparés ###
plt.figure(figsize=(10, 6))
plt.subplot(211)                                                         # Création du premier sous-tracé
plt.plot(y[:, 0], lw=1.5, label='1st')                                   # Tracé avec taille personnalisée
plt.plot(y[:, 0], 'ro')                                                  # Points rouges
plt.legend(loc=0)                                                        # Légende automatique
plt.ylabel('Value')                                                      # Label axe y
plt.title('Tracé 2D avec 2 sous-tracés séparés')                         # Titre du graphique
plt.subplot(212)                                                         # Création du second sous-tracé
plt.plot(y[:, 1], lw=1.5, label='2nd')                                   # Tracé avec taille personnalisée
plt.plot(y[:, 1], 'ro')                                                  # Points rouges 
plt.legend(loc=0)                                                        # Légende automatique
plt.xlabel('Index')                                                      # Label axe x
plt.ylabel('Value')                                                      # Label axe y
plt.show()


### Tracé combinant des lignes et des barres d'histogramme ###
plt.subplot(121)                                                         # Création du premier sous-tracé
plt.plot(y[:, 0], 'b', lw=1.5, label='1st')                              # Tracé avec taille personnalisée
plt.plot(y[:, 0], 'ro')                                                  # Points rouges
plt.legend(loc=0)                                                        # Légende automatique
plt.xlabel('Index')                                                      # Label axe x  
plt.ylabel('Value')                                                      # Label axe y
plt.title('1st data set')                                                # Titre du graphique
plt.subplot(122)                                                         # Création du second sous-tracé
plt.bar(np.arange(len(y)), y[:, 1], color='g', label='2nd')              # Création d'un sous-tracé type histogramme
plt.legend(loc=0)                                                        # Légende automatique
plt.xlabel('Index')                                                      # Label axe x
plt.title('2nd data set')                                                # Titre du graphique
plt.suptitle('Tracé combiné : Lignes et Barres')                         # Titre global de la figure
plt.show()


### Scatter plot 2D statique (nuage de points) avec plt.plot ###
y = np.random.standard_normal((1000, 2))                                 # Données aléatoires pour le scatter plot
plt.figure(figsize=(10, 6))                                              # Taille de la figure
plt.plot(y[:, 0], y[:, 1], 'ro')                                         # Tracé du scatter plot avec points rouges et transparence
plt.xlabel('1st')                                                        # Label axe x
plt.ylabel('2nd')                                                        # Label axe y
plt.title('Scatter plot type plt.plot')                                  # Titre du graphique
plt.show()


### Scatter plot 2D statique (nuage de points) avec plt.scatter ###
plt.figure(figsize=(10, 6))                                              # Taille de la figure
plt.scatter(y[:, 0], y[:, 1], marker='o')                                # Tracé du scatter plot avec points bleus et transparence
plt.xlabel('1st')                                                        # Label axe x
plt.ylabel('2nd')                                                        # Label axe y
plt.title('Scatter plot type plt.scatter')                               # Titre du graphique
plt.show()


### Scatter plot 2D statique (nuage de points) avec une troisième dimension ###
c = np.random.randint(0, 10, len(y))                                     # Création d'une troisième dimension pour la couleur des points
plt.figure(figsize=(10, 6))                                              # Taille de la figure
plt.scatter(y[:, 0], y[:, 1],
            c=c,
            cmap='coolwarm',
            marker='o')                                                  # Tracé du scatter plot avec points colorés selon une échelle
plt.colorbar()                                                           # Ajout de la barre de couleur
plt.xlabel('1st')                                                        # Label axe x
plt.ylabel('2nd')                                                        # Label axe y
plt.title('Scatter plot avec échelle de couleur')                        # Titre du graphique
plt.show()


### Histogramme 2D statique avec deux séries de données ###
plt.figure(figsize=(10, 6))                                              # Taille de la figure
plt.hist(y, label=['1st', '2nd'], bins=25)                               # Tracé de l'histogramme avec deux séries de données
plt.legend(loc=0)                                                        # Légende automatique
plt.xlabel('Value')                                                      # Label axe x
plt.ylabel('Frequency')                                                  # Label axe y
plt.title('Histogramme 2D statique avec deux séries de données')         # Titre du graphique
plt.show()

# liste des paramètres que plt.hist peut prendre :
# plt.hist(x,                                                            # Données à tracer
#          bins=10,                                                      # Nombre de bacs
#          range=None,                                                   # Plage des valeurs 
#          density=False,                                                # Normalisation de l'histogramme
#          weights=None,                                                 # Poids pour chaque valeur
#          cumulative=False,                                             # Histogramme cumulatif
#          bottom=None,                                                  # Position de base des barres
#          histtype='bar',                                               # Type d'histogramme : 'bar', 'barstacked', 'step', 'stepfilled'
#          align='mid',                                                  # Alignement des barres : 'left', 'center', 'right'
#          orientation='vertical',                                       # Orientation des barres : 'vertical', 'horizontal'
#          rwidth=None,                                                  # Largeur relative des barres
#          log=False,                                                    # Échelle logarithmique
#          color=None,                                                   # Couleur des barres
#          label=None,                                                   # Labels pour la légende
#          stacked=False,                                                # Histogramme empilé
#          hold=None,                                                    # Maintien du tracé précédent (déprécié)
#          **kwargs)                                                     # Autres arguments optionnels


### Histogramme 2D statique empilant deux jeux de données ###
plt.figure(figsize=(10, 6))                                              # Taille de la figure
plt.hist(y, 
         label=['1st', '2nd'], 
         color=['b', 'g'], 
         stacked=True, 
         bins=20, 
         alpha=0.5)                                                      # Tracé de l'histogramme empilé avec deux séries de données
plt.legend(loc=0)                                                        # Légende automatique
plt.xlabel('Value')                                                      # Label axe x
plt.ylabel('Frequency')                                                  # Label axe y
plt.title('Histogramme 2D statique empilant deux jeux de données')       # Titre du graphique
plt.show()


### Boîte à moustache (boxplot) pour deux jeux de données ###
fig, ax = plt.subplots(figsize=(10, 6))                                  # Taille de la figure
plt.boxplot(y)                                                           # Tracé de la boîte à moustache
plt.setp(ax, xticklabels=['1st', '2nd'])                                 # Labels des axes x
plt.xlabel('Data set')                                                   # Label axe x
plt.ylabel('Value')                                                      # Label axe y
plt.title('Boîte à moustache pour deux jeux de données')                 # Titre du graphique
plt.show()
# Les ronds indiquent les valeurs aberrantes (outliers) dans le boxplot. 


### Tracé d'une fonction exponentielle ave la zone d'intégrale et les labels LaTeX ###

# Définition de la fonction exponentielle et des limites de l'intégrale #
def func(x):                                                             # Définition de la fonction exponentielle
    return 0.5 * np.exp(x) + 1                                           # Fonction exponentielle
a, b = 0.5, 1.5                                                          # Limites de l'intégrale
x = np.linspace(0, 2)                                                    # Valeur x du tracé 
y = func(x)                                                              # Valeur y du tracé
Ix = np.linspace(a, b)                                                   # Valeur de x pour les limites de l'intégrale
Iy = func(Ix)                                                            # Valeur de y pour les limmites de l'intégrale
verts = [(a, 0)] + list(zip(Ix,Iy)) + [(b, 0)]                           # Objet de type liste contenant plusieurs tuples (x,y) pour les coordonées du polygone


# Tracé de la fonction exponentielle #
from matplotlib.patches import Polygon                                   # Importation de l'objet Polygon pour le tracé de la zone d'intégrale

# Création de la figure et du tracé #
fig, ax = plt.subplots(figsize=(10, 6))                                  # Création de la figure et des axes
plt.plot(x, y, 'b', linewidth=2)                                         # Tracé des valeurs de la fonction par un trait bleu
plt.ylim(bottom=0)                                                       # Définition de la valeur y minimale pour l'axe des ordonnées
poly = Polygon(verts, facecolor='0.7', edgecolor='0.5')                  # Tracé en gris du polygone de la zone d'intégrale
ax.add_patch(poly)                                                       # Ajout du polygone au tracé
plt.text(0.5 * (a+b), 1, r'$\int_a^b f(x)\mathrm{d}x$', 
         horizontalalignment='center', fontsize=20)                      # Ajout de la formule d'intégrale en LaTeX dans le tracé 
plt.figtext(0.9, 0.075, '$x$')                                           # Ajout des labels d'axes 
plt.figtext(0.075, 0.9, '$f(x)$')                                        # Ajout des labels d'axes  
ax.set_xticks((a, b))                                                    # Ajout des lables x 
ax.set_xticklabels(('$a$', '$b$'))                                       # Ajout des lables x 
ax.set_yticks([func(a), func(b)])                                        # Ajout des lables y
ax.set_yticklabels(('$f(a)$', '$f(b)$'))                                 # Ajout des lables y
plt.title('Tracé d\'une fonction exponentielle avec intégrale')          # Titre du graphique
plt.show()
