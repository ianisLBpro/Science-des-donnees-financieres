#
# Test du tracé 3D statiques avec Matplotlib
#
#
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D # Import 3D

# Affiche la version de Matplotlib
print(mpl.__version__)

# Mise en place du fond et des axes #
sns.set_style("whitegrid")              # Style avec grille blanche
mpl.rcParams['font.family'] = 'serif'   # Police avec empattements

np.random.seed(1000)                    # Pour la reproductibilité
y = np.random.standard_normal(20)       # Données aléatoires
x = np.arange(len(y))                   # Abscisses



# Tracé 3D de surface #
strike = np.linspace(50, 150, 24)                   # Strike de 50 à 150
ttm = np.linspace(0.5, 2.5, 24)                     # Maturité de 0.5 à 2.5 ans
strike, ttm = np.meshgrid(strike, ttm)              # Grilles de strike et ttm
print(strike[:2].round(1))                          # Affiche un extrait de la grille strike

iv = (strike - 100) ** 2 / (100 * strike) / ttm     # Calcul de la volatilité implicite
print(iv[:5, :3])                                   # Affiche un extrait de la matrice iv

fig = plt.figure(figsize=(10, 6))                   # Taille de la figure
ax = fig.add_subplot(111, projection='3d')          # Ajout d'un subplot 3D
surf = ax.plot_surface(strike, 
                       ttm, 
                       iv, 
                       rstride=2, 
                       cstride=2, 
                       cmap=plt.cm.coolwarm, 
                       linewidth=0.5, 
                       antialiased=True)            # Tracé de la surface

ax.set_xlabel('strike')                             # Label axe x
ax.set_ylabel('time to maturity')                   # Label axe y
ax.set_zlabel('implied volatility')                 # Label axe z
fig.colorbar(surf, shrink=0.5, aspect=5)            # Barre de couleur
plt.title('Volatilité implicite en 3D')             # Titre du graphique
plt.show()                                          # Affiche le graphique


# Tracé 3D avec un autre angle de vue #

