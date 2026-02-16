# Ce code sert à modéliser le prix d'une action dans le temps et c'est très utile en finance.

# À quoi ça sert :
# Évaluer des options (appel/vente) : Si vous avez une option sur une action, vous devez savoir combien elle vaut. 
# L'arbre binomial montre tous les prix possibles → vous calculez le prix de l'option à chaque scénario.
# Prédire les prix futurs : L'arbre montre que le prix peut monter (u) ou baisser (d) à chaque période. 
# C'est un modèle réaliste du marché.

# Analyse de risque : Vous voyez tous les scénarios possibles (prix bas, moyen, haut) pour prendre de meilleures décisions.

# Exemple concret :
# Prix actuel S0 : 36€
# Dans 1 an, le prix peut être 43€ (hausse) ou 30€ (baisse)
# Vous avez une option d'achat à 40€ : vous savez exactement quand c'est rentable
# Résumé : C'est un outil pour les traders/analystes financiers pour valoriser les contrats futurs et gérer les risques en Bourse. 
# Sans cet arbre, impossible de savoir à quel prix vendre une option !

import math 
import numpy as np
import matplotlib.pyplot as plt

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
    """Affiche graphiquement l'arbre binomial"""
    M = S.shape[1] - 1
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Tracer les nœuds et les connexions
    for t in range(M + 1):
        for i in range(t + 1):
            x = t  # Position horizontale (temps)
            y = i  # Position verticale (prix)
            
            # Afficher le nœud (prix)
            ax.plot(x, y, 'o', markersize=8, color='blue')
            ax.text(x, y - 0.3, f'{S[i, t]:.1f}', ha='center', fontsize=9)
            
            # Tracer les lignes vers les nœuds suivants
            if t < M:
                ax.plot([x, x + 1], [y, y], 'k-', alpha=0.3, linewidth=1)  # Hausse
                ax.plot([x, x + 1], [y, y + 1], 'k-', alpha=0.3, linewidth=1)  # Baisse
    
    ax.set_xlabel('Périodes (temps)', fontsize=12)
    ax.set_ylabel('États du monde', fontsize=12)
    ax.set_title('Arbre Binomial - Évolution du Prix de l\'Action', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-0.5, M + 0.5)
    ax.set_ylim(-1, M + 1)
    plt.tight_layout()
    plt.show()

np.set_printoptions(formatter={'float':
                               lambda x: '%6.2f' % x})

# Créer l'arbre binomial
M = 15
S = simulate_tree(M)
print(f"Arbre binomial créé avec {M} périodes")
print(f"Prix initial : {S[0,0]:.2f}€")
print(f"Prix final min : {np.min(S[S > 0]):.2f}€")
print(f"Prix final max : {np.max(S):.2f}€")
plot_tree(S)


### ===== OUTIL DE TRADER PROFESSIONNEL ===== ###

# Paramètres d'option
K = 40  # Strike (prix d'exercice)
option_type = "CALL"  # ou "PUT"

# Calcul des paramètres du modèle
dt = T / M
u = math.exp(sigma * math.sqrt(dt))
d = 1 / u
q = (math.exp(r * dt) - d) / (u - d)  # Probabilité risque-neutre

# VALUATION DE L'OPTION
def value_option(S_tree, K, q, r, dt, option_type="CALL"):
    """Calcule la valeur de l'option par backtracking"""
    M = S_tree.shape[1] - 1
    C = np.zeros((M + 1, M + 1))
    
    # Valeur à maturité
    for i in range(M + 1):
        if option_type == "CALL":
            C[i, M] = max(S_tree[i, M] - K, 0)
        else:  # PUT
            C[i, M] = max(K - S_tree[i, M], 0)
    
    # Backtracking
    for t in range(M - 1, -1, -1):
        for i in range(t + 1):
            C[i, t] = math.exp(-r * dt) * (q * C[i, t + 1] + (1 - q) * C[i + 1, t + 1])
    
    return C

# Calculer la valeur de l'option
C = value_option(S, K, q, r, dt, option_type)
option_price = C[0, 0]

print("\n" + "="*70)
print(f"VALUATION D'OPTION {option_type}")
print("="*70)
print(f"Strike (K) : {K:.2f}€")
print(f"Prix théorique de l'option {option_type} : {option_price:.2f}€")
print(f"(Ce prix reflète toutes les probabilités de rendement futurs)")

# ANALYSE DE RISQUE
print("\n" + "="*70)
print("ANALYSE DE RISQUE - SCÉNARIOS EXTRÊMES")
print("="*70)

prix_finaux = S[:M+1, M]
prix_finaux = prix_finaux[prix_finaux > 0]
prix_min = np.min(prix_finaux)
prix_max = np.max(prix_finaux)

# Perte/gain max
if option_type == "CALL":
    max_loss = option_price  # Prime payée
    max_gain = prix_max - K - option_price
else:  # PUT
    max_loss = option_price
    max_gain = K - prix_min - option_price

print(f"Perte maximale : {max_loss:.2f}€")
print(f"Gain maximal possible : {max_gain:.2f}€")
print(f"Ratio risque/récompense : {abs(max_gain/max_loss) if max_loss != 0 else float('inf'):.2f}")

# Probabilité de profit
if option_type == "CALL":
    payoff_final = np.maximum(prix_finaux - K, 0)
else:
    payoff_final = np.maximum(K - prix_finaux, 0)

profit_prob = np.sum(payoff_final > option_price) / len(prix_finaux) * 100
print(f"Probabilité de profit : {profit_prob:.1f}%")

# PRÉVISION AVEC 4 SCÉNARIOS
print("\n" + "="*70)
print("PRÉVISION DU PRIX DANS 1 AN (4 SCÉNARIOS)")
print("="*70)
print(f"Prix actuel : {S0:.2f}€")
print(f"Prix min possible : {prix_min:.2f}€")
print(f"Prix max possible : {prix_max:.2f}€\n")

tres_baissier = np.sum(prix_finaux < S0 * 0.80)
baissier = np.sum((prix_finaux >= S0 * 0.80) & (prix_finaux < S0))
haussier = np.sum((prix_finaux >= S0) & (prix_finaux <= S0 * 1.20))
tres_haussier = np.sum(prix_finaux > S0 * 1.20)

proba_tres_baissier = (tres_baissier / len(prix_finaux)) * 100
proba_baissier = (baissier / len(prix_finaux)) * 100
proba_haussier = (haussier / len(prix_finaux)) * 100
proba_tres_haussier = (tres_haussier / len(prix_finaux)) * 100

print(f"📉 TRÈS BAISSIER (< {S0*0.80:.2f}€)  : {proba_tres_baissier:.1f}%")
print(f"📉 BAISSIER ({S0*0.80:.2f}€ - {S0:.2f}€) : {proba_baissier:.1f}%")
print(f"📈 HAUSSIER ({S0:.2f}€ - {S0*1.20:.2f}€) : {proba_haussier:.1f}%")
print(f"📈 TRÈS HAUSSIER (> {S0*1.20:.2f}€)  : {proba_tres_haussier:.1f}%")

print("\n" + "="*70)









