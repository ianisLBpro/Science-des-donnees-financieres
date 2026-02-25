'''
arbres_binomiaux.py

Voyons ici comment construire un arbre binomial, une méthode très répandue pour l'évaluation des options définie par Cox, Ross et Rubinstein en 1979.
L'objectif est la représentation de l'évolution future d'une valeur au moyen d'un arbre recombinant (binomial). 
Comme dans le modèle de Black-Scholes-Merton de 1973, il y a un actif risqué, qui est un indice ou une action, et un actif sans risque, une obligation. 
La plage temporelle entre aujourd'hui et la maturité de l'option est divisée en intervalles équidistants de longueur Δt.

A partir d'un niveau d'indice au moment s de S(s), le niveau de l'indice au moment t = s + Δt sera S(t) = S(s) * m. 
La valeur de m est choisie au hasard dans l'intervalle {u, d}, avec 0 < d < e^rΔt < u = e^σ√Δt, et u = 1/d. 
Le taux court sans risque est r, et la volatilité de l'indice est σ.

Nous allons montrer comment construire un arbre binomial de différentes manières, en utilisant des outils de plus en plus performants pour accélérer la construction de l'arbre.
Voici différentes manières de construire un arbre binomial : 
- Exercice 1 : Formulation en Python pur de l'arbre binomial, fondée sur quelques paramètres numériques fixes du modèle.
- Exercice 2 : Arbre binomial avec Numpy en utilisant du code totalement vectorisé
- Exercice 3 : Variante de l'arbre binomial avec Numba 
- Exercice 4 : Variante de l'arbre binomial avec Cython (A venir)
- Exercice 5 : Affichage graphique de l'arbre binomial avec Matplotlib
- Exercice 6 : Valorisation d'options européennes, comparaison avec Black-Scholes-Merton
'''



import math
import time
import numpy as np
import matplotlib.pyplot as plt
import numba
from scipy.stats import norm


'''
Exercice 1 : Formulation en Python pur de l'arbre binomial, fondée sur quelques paramètres numériques fixes du modèle. 
Contrairement à ce qui se produit dans un tracé typique d'arbre, le mouvement croissant correspond dans l'objet ndarray à un déplacement latéral.
Cela fait diminuer la taille de ndarray, et rend plus facile la construction de l'arbre.
'''

print("\n" + "="*70)
print("Exercice 1 : CONSTRUCTION D'UN ARBRE BINOMIAL - PYTHON PUR")
print("="*70)

# Valeur initiale de l'actif risqué 
S0 = 36.
# Horizon temporel de la simulation d'arbre binomial
T = 1.0
# Taux constant à court terme 
r = 0.06
# facteur de volatilité constant
sigma = 0.2

# Fonction simulate_tree pur 
def simulate_tree(M):
    # Longueur des intervalles temporels
    dt = T / M
    # Facteur pour les mouvements croissants et décroissants
    u = math.exp(sigma * math.sqrt(dt))
    d = 1 / u
    # Construction de l'arbre binomial
    S = np.zeros((M + 1 , M + 1))
    S[0, 0] = S0
    z = 1
    for t in range(1, M + 1):
        for i in range(z):
            S[i, t] = S[i, t-1] * u
            S[i + 1, t] = S[i, t-1] * d
        z += 1
    return S

# Affichage graphique de l'arbre binomial, set_printoptions pour un affichage plus lisible des prix dans l'arbre
np.set_printoptions(formatter={'float': lambda x: '%6.2f' % x})
# Arbre avec 4 intervalles temporels
print("Arbre binomial avec 4 périodes :")
print(simulate_tree(4))
# Arbre avec 500 intervalles temporels
print("\nArbre binomial avec 500 périodes :")
t0 = time.time()
print(simulate_tree(500))
print(f"Temps d'exécution pour 500 périodes : {time.time() - t0:.5f} secondes")




'''
Exercice 2 : Arbre binomial avec Numpy en utilisant du code totalement vectorisé
'''

print("\n" + "="*70)
print("Exercice 2 : CONSTRUCTION D'UN ARBRE BINOMIAL - CODE VECTORISÉ AVEC NUMPY")
print("="*70)

# Fonction de simulation d'arbre binomial à 4 périodes
M = 4 
# Séquence de 0 à M 
up = np.arange(M + 1) 

# Objet ndarray avec mouvements bruts à la hausse 
up = np.resize(up, (M + 1, M +1))
print("Mouvements bruts à la hausse :")
print(up)

# Objet ndarray avec mouvements bruts à la baisse
down = up.T * 2
print("\nMouvements bruts à la baisse :")
print(down)

# Objet ndarray avec mouvements nets à la hausse (positif) et à la baisse (négatif)
net = up - down
print("\nMouvements nets à la hausse et à la baisse :")
print(net)

# Calcul de la longueur de chaque intervalle temporel 
dt = T / M 
# Arbre pour quatre intervalles temporels (triangle de valeurs du coin supérieur droit)
S0 * np.exp(sigma * math.sqrt(dt) * (up - down))

# Code format compact pour générer un arbre binomial avec Numpy
def simulate_tree_np(M):
    dt = T / M 
    up = np.arange(M + 1)
    up = np.resize(up, (M + 1, M +1))
    down = up.transpose() * 2
    S = S0 * np.exp(sigma * math.sqrt(dt) * (up - down))
    return S

print("\nArbre binomial avec Numpy vectorisé 4 périodes :")
print(simulate_tree_np(4))
print("\nArbre binomial avec Numpy vectorisé 500 périodes :")
t0 = time.time()
print(simulate_tree_np(500))
print(f"Temps d'exécution pour 500 périodes : {time.time() - t0:.5f} secondes")




'''
Exercice 3 : Variante de l'arbre binomial avec Numba
L'algorithme de simulation d'arbre binomial devrait être optimisable grâce à la compilation dynamique de Numba.
'''

print("\n" + "="*70)
print("Exercice 3 : CONSTRUCTION D'UN ARBRE BINOMIAL - CODE OPTIMISÉ AVEC NUMBA")
print("="*70)
# Version optimisée de la fonction de simulation d'arbre binomial avec Numba
simulate_tree_nb = numba.jit(simulate_tree)

print("\nArbre binomial avec Numba optimisé 4 périodes :")
print(simulate_tree_nb(4))
print("\nArbre binomial avec Numba optimisé 500 périodes :")
t0 = time.time()
print(simulate_tree_nb(500))
print(f"Temps d'exécution pour 500 périodes : {time.time() - t0:.5f} secondes")




'''
Exercice 4 : Variante de l'arbre binomial avec Cython (WIP - Necessite une image Docker)
'''
print("\n" + "="*70)
print("Exercice 4 : CONSTRUCTION D'UN ARBRE BINOMIAL - CODE OPTIMISÉ AVEC CYTHON (WIP - Necessite une image Docker)")
print("="*70)







'''
Exercice 5 : Affichage graphique de l'arbre binomial avec Matplotlib
'''

print("\n" + "="*70)
print("Exercice 5 : CONSTRUCTION D'UN ARBRE BINOMIAL - AFFICHAGE GRAPHIQUE AVEC MATPLOTLIB")
print("="*70)

S0 = 36.
T = 1.0
r = 0.06 
sigma = 0.2 

def simulate_tree(M):
    dt = T / M 
    u = math.exp(sigma * math.sqrt(dt))
    d = 1 / u 
    S = np.zeros((M + 1 , M + 1))
    S[0, 0] = S0
    z = 1
    for t in range(1, M + 1):
        for i in range(z):
            S[i, t] = S[i, t-1] * u
            S[i + 1, t] = S[i, t-1] * d
        z += 1
    return S

def plot_tree(S):
    M = S.shape[1] - 1 
    fig, ax = plt.subplots(figsize=(14, 8)) 
    
    # Tracer les noeuds et les connexions
    for t in range(M + 1):
        for i in range(t + 1):
            x = t  # Position horizontale (temps)
            y = i  # Position verticale (prix)
            
            # Afficher le noeud (prix)
            ax.plot(x, y, 'o', markersize=8, color='blue')
            ax.text(x, y - 0.3, f'{S[i, t]:.1f}', ha='center', fontsize=9)
            
            # Tracer les lignes vers les noeuds suivants
            if t < M:
                ax.plot([x, x + 1], [y, y], 'k-', alpha=0.3, linewidth=1)      # Hausse
                ax.plot([x, x + 1], [y, y + 1], 'k-', alpha=0.3, linewidth=1)  # Baisse
    
    ax.set_xlabel('Périodes (temps)', fontsize=12)
    ax.set_ylabel('Prix de l\'action', fontsize=12)
    ax.set_title('Arbre Binomial - Évolution du Prix de l\'Action', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-0.5, M + 0.5)
    ax.set_ylim(-1, M + 1)
    plt.tight_layout()
    plt.show()

# Set_printoptions pour un affichage plus lisible des prix dans l'arbre
np.set_printoptions(formatter={'float': lambda x: '%6.2f' % x})
# Créer l'arbre binomial
M = 20               # Nombre de périodes (intervalles temporels)
S = simulate_tree(M) # Générer l'arbre binomial avec M périodes
print(f"Arbre binomial créé avec {M} périodes")
print(f"Prix initial : {S[0,0]:.2f}€")
print(f"Prix final min : {np.min(S[S > 0]):.5f}€")
print(f"Prix final max : {np.max(S):.5f}€")
plot_tree(S)




'''
Exercice 6 : Valorisation d'options européennes et analyse par l'arbre binomial (En cours de rédaction)
On utilise l'arbre binomial de Cox-Ross-Rubinstein pour valoriser des options européennes Call et Put,
puis on vérifie la cohérence du modèle par benchmark avec la formule fermée de Black-Scholes-Merton.
- Valorisation par backward induction en probabilité risque-neutre
- Comparaison avec la formule fermée de Black-Scholes-Merton
'''

print("\n" + "="*70)
print("Exercice 6 : VALORISATION D'OPTIONS EUROPÉENNES PAR ARBRE BINOMIAL")
print("="*70)

# Paramètres 
S0 = 36.              # Prix spot du sous-jacent
K = 40.               # Strike (prix d'exercice)
T = 1.0               # Maturité (en années)
r = 0.06              # Taux sans risque continu
sigma = 0.2           # Volatilité annualisée
M = 500               # Nombre de pas temporels

# Construction de l'arbre et valorisation par backward induction sous la probabilité risque-neutre q
def binomial_option_price(S0, K, T, r, sigma, M, option_type="CALL"):
    '''
    Valorisation d'une option européenne par le modèle binomial de CRR.
    Backward induction sous la probabilité risque-neutre q.
    Retourne le prix de l'option, l'arbre des prix du sous-jacent et l'arbre des valeurs de l'option.
    '''
    dt = T / M                              # Longueur de chaque intervalle temporel
    u = math.exp(sigma * math.sqrt(dt))     # Facteur de mouvement à la hausse
    d = 1 / u                               # Facteur de mouvement à la baisse
    q = (math.exp(r * dt) - d) / (u - d)    # Probabilité risque-neutre de hausse
    discount = math.exp(-r * dt)            # Facteur d'actualisation par pas

    # Construction de l'arbre des prix du sous-jacent
    S = np.zeros((M + 1, M + 1))
    S[0, 0] = S0
    for t in range(1, M + 1):
        for i in range(t + 1):
            S[i, t] = S0 * (u ** (t - i)) * (d ** i)

    # Payoff à maturité
    C = np.zeros((M + 1, M + 1))
    for i in range(M + 1):
        if option_type == "CALL":
            C[i, M] = max(S[i, M] - K, 0)
        else:
            C[i, M] = max(K - S[i, M], 0)

    # Backward induction : on remonte l'arbre de t = M-1 à t = 0
    for t in range(M - 1, -1, -1):
        for i in range(t + 1):
            C[i, t] = discount * (q * C[i, t + 1] + (1 - q) * C[i + 1, t + 1])

    return C[0, 0], S, C

# Calcul du Call et du Put
call_price, S_tree, C_tree = binomial_option_price(S0, K, T, r, sigma, M, "CALL")
put_price, _, P_tree = binomial_option_price(S0, K, T, r, sigma, M, "PUT")

print(f"\nParamètres : S0={S0}, K={K}, T={T}, r={r}, σ={sigma}, M={M}")
print(f"Prix du CALL européen (binomial) : {call_price:.4f}€")
print(f"Prix du PUT européen (binomial)  : {put_price:.4f}€")

# Formule fermée de Black-Scholes-Merton (benchmark analytique)

def black_scholes(S0, K, T, r, sigma, option_type="CALL"):
    '''
    Formule fermée de Black-Scholes-Merton pour une option européenne.
    C = S0 * N(d1) - K * e^{-rT} * N(d2)  pour un Call
    P = K * e^{-rT} * N(-d2) - S0 * N(-d1)  pour un Put
    '''
    d1 = (math.log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == "CALL":
        price = S0 * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    else:
        price = K * math.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
    return price, d1, d2

call_bs, d1, d2 = black_scholes(S0, K, T, r, sigma, "CALL")
put_bs, _, _ = black_scholes(S0, K, T, r, sigma, "PUT")

print(f"\nPrix du CALL européen (Black-Scholes) : {call_bs:.4f}€")
print(f"Prix du PUT européen (Black-Scholes)  : {put_bs:.4f}€")
print(f"Écart CALL (binomial vs BS) : {abs(call_price - call_bs):.6f}€")
print(f"Écart PUT  (binomial vs BS) : {abs(put_price - put_bs):.6f}€")



