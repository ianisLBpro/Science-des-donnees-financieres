# Simulation de Monte Carlo pour le prix d'une option européenne de type put sur un actif dont le prix suit une dynamique Black-Scholes.

import matplotlib.pyplot as plt
import numba
import numpy as np
import math

S0 = 36.
T = 1.0
sigma = 0.2
r = 0.06
M = 100
I = 50000
K = 40

def mcs_simulation_py(p):
    M, I = p
    dt = T / M 
    S = np.zeros((M + 1, I))
    S[0] = S0
    rn = np.random.standard_normal(S.shape)
    for t in range(1, M + 1):
        for i in range(I):
            S[t, i] = S[t-1, i] * math.exp((r - sigma ** 2 / 2) * dt + sigma * math.sqrt(dt) *rn[t, i])
    return S

S = mcs_simulation_py((M, I))
print(S)
print(S[-1].mean())
print(S0 * math.exp(r * T))

C0 = math.exp(-r * T) * np.maximum(K - S[-1], 0).mean()
print(C0)


# Graphiques des trajectoires simulées
plt.figure(figsize=(10, 6))
plt.hist(S[-1], bins=35, label='frequency')
plt.axvline(S[-1].mean(), color='r', label='mean value')
plt.legend(loc=0)
plt.title('Histogram of the simulated asset prices at maturity')
plt.xlabel('Asset price at maturity')
plt.ylabel('Frequency')
plt.show()


# Variante avec NUMPY vectorisé
def mcs_simulation_np(p):
    M, I = p
    dt = T / M 
    S = np.zeros((M + 1, I))
    S[0] = S0
    rn = np.random.standard_normal(S.shape)
    for t in range(1, M + 1):
        S[t] = S[t-1] * np.exp((r - sigma ** 2 / 2) * dt + sigma * math.sqrt(dt) * rn[t])
    return S

S = mcs_simulation_np((M, I))
print(S)
print(S[-1].mean())


# Variante avec NUMBA JIT
mcs_simulation_nb = numba.jit(mcs_simulation_py)
S = mcs_simulation_nb((M, I))
print(S)
print(S[-1].mean())
C0 = math.exp(-r * T) * np.maximum(K - S[-1], 0).mean()
print(C0)