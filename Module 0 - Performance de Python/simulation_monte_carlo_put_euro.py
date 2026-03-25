'''
Simulation_monte_carlo_put_euro

La simulation de Monte Carlo, 
c'est une méthode qui consiste à répéter un calcul des milliers (voire millions) de fois en y injectant du hasard, 
puis à analyser la distribution des résultats pour en tirer des conclusions.

Dans cet exemple, nous allons simuler le prix d'une option de vente européenne (put), 
via la simulation d'un mouvement brownien géométrique, qui est un processus stochastique simple pour modéliser
l'évolution du cours des actions ou des indices. 

La théorie de valorisation des options de Black-Scholes-Merton (1973) se fonde sur ce processus. 
le sous-jacent de l'option à évaluer obéit à l'équation différentielle stochastique EDS,
(SED, stochastic differential equation) comme suit :

- La valeur du sous-jacent à l'instant t, S_t
- Le taux sans risque à court terme constant est r 
- La volatilité instantanée est la constante sigma 
- Le mouvment brownien correspond à Z_t

dS_t = r * S_t * dt + sigma * S_t * dZ_t


Cette équation peut être discrétisée sur une série d'intervalles temporels équidistants,
puis simulée selon l'equation suivante qui correspond à un schéma d'Euler-Maruyama :

- z est la valeur aléatoire en distribution normale standard
- M est le nombre d'intervalles temporels, la longueur de chaque intervalle est dt = T / M
    - T est l'horizon temporel de la simulation, c'est à dire la maturité de l'option

S_t = S_t-dt * exp((r - sigma^2 / 2) * dt + sigma * sqrt(dt) * z)


L'estimateur de Monte Carlo pour une option call européenne est obtenue par l'équation dans laquelle
S_t(i) est la i-ème valeur simulée du sous-jacent à la maturité T pour un nombre total de trajectoires simulées I,
avec i = 1,2,...,I].

- K est le prix d'exercice de l'option

Pour un call européen :
C_0 = e^(-r * T) * 1/I * sum(max(S_t(i) - K, 0))

Pour un put européen :
P_0 = e^(-r * T) * 1/I * sum(max(K - S_t(i), 0))

'''


import matplotlib.pyplot as plt
import numba
import numpy as np
import math
import time



# Paramètres de la simulation
S0 = 36.       # Prix initial du sous-jacent
T = 1.0        # Maturité (en années)
sigma = 0.2    # Volatilité
r = 0.06       # Taux sans risque
M = 100        # Nombre d'intervalles temporels
I = 50000      # Nombre de trajectoires simulées
K = 40         # Prix d'exercice (strike)


# Méthode 1 : Python  #
def mcs_simulation_py(p):
    M, I = p
    dt = T / M
    S = np.zeros((M + 1, I))
    S[0] = S0
    # Valeurs aléatoires générées dans une seule étape vectorisée
    rn = np.random.standard_normal(S.shape)
    # Boucle imbriquée qui concrétise la simulation fondée sur le schéma d'Euler-Maruyama
    for t in range(1, M + 1):
        for i in range(I):
            S[t, i] = S[t-1, i] * math.exp((r - sigma ** 2 / 2) * dt + sigma * math.sqrt(dt) * rn[t, i])
    return S

print('\nMéthode 1 : Python (double boucle)')
start = time.time()
S = mcs_simulation_py((M, I))
# temps écoulé pour la simulation
elapsed = time.time() - start

# Etimateur de Monte Carlo pour le prix du put européen
C0 = math.exp(-r * T) * np.maximum(K - S[-1], 0).mean()
print(f'Valeur moyenne en fin de période fondée sur la simulation : {S[-1].mean():.4f}')
print(f'valeur moyenne en fin de période théoriquement espérée :    {S0 * math.exp(r * T):.4f}')
print(f'Prix du put européen (Monte Carlo) :                        {C0:.4f}')
print(f'Temps de simulation : {elapsed:.4f} s\n')


# Méthode 2 : NumPy vectorisé #
def mcs_simulation_np(p):
    M, I = p
    dt = T / M
    S = np.zeros((M + 1, I))
    S[0] = S0
    rn = np.random.standard_normal(S.shape)
    # La boucle qui progresse parmi les intervalles temporels
    for t in range(1, M + 1):
        # Le schéma de Euler-Maruyama avec le code Numpy vectorisé qui traite toutes les trajectoires en une fois 
        S[t] = S[t-1] * np.exp((r - sigma ** 2 / 2) * dt + sigma * math.sqrt(dt) * rn[t])
    return S

print('Méthode 2 : NumPy vectorisé')
start = time.time()
S = mcs_simulation_np((M, I))
elapsed = time.time() - start

C0 = math.exp(-r * T) * np.maximum(K - S[-1], 0).mean()
print(f'Prix moyen du sous-jacent à maturité : {S[-1].mean():.4f}')
print(f'Prix du put européen (Monte Carlo) :   {C0:.4f}')
print(f'Temps de simulation : {elapsed:.4f} s\n')


# Méthode 3 : Numba JIT #
mcs_simulation_nb = numba.jit(mcs_simulation_py)
mcs_simulation_nb((10, 10))  # Pré-compilation JIT (hors mesure)

print('Méthode 3 : Numba JIT')
start = time.time()
S = mcs_simulation_nb((M, I))
elapsed = time.time() - start

C0 = math.exp(-r * T) * np.maximum(K - S[-1], 0).mean()
print(f'Prix moyen du sous-jacent à maturité : {S[-1].mean():.4f}')
print(f'Prix du put européen (Monte Carlo) :   {C0:.4f}')
print(f'Temps de simulation : {elapsed:.4f} s\n')


# Graphique #
plt.figure(figsize=(10, 6))
plt.hist(S[-1], bins=35, label='Fréquence')
plt.axvline(S[-1].mean(), color='r', label=f'Moyenne = {S[-1].mean():.2f}')
plt.axvline(K, color='g', linestyle='--', label=f'Strike K = {K}')
plt.legend(loc=0)
plt.title('Distribution du prix du sous-jacent à maturité')
plt.xlabel('Prix à maturité')
plt.ylabel('Fréquence')
plt.show()