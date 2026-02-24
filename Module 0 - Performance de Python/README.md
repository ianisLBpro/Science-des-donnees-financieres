# Module 0 — Performance de Python

Ce module explore les différentes stratégies d'optimisation des performances en Python à travers des problèmes classiques et financiers. Chaque exercice compare plusieurs implémentations (boucles Python, vectorisation NumPy, compilation JIT avec Numba) pour mettre en évidence les gains de performance.

---

## Fichiers

| Fichier | Description |
|---|---|
| `arbres_binomiaux.py` | Construction et valorisation d'un arbre binomial (Cox-Ross-Rubinstein). 6 exercices progressifs détaillés ci-dessous. |
| `nb_pi_test.py` | Estimation de π par Monte Carlo. Comparaison Python pur, NumPy et visualisation graphique. |
| `nb_premiers_test.py` | Test de primalité accéléré par Numba JIT. |
| `simulation_monte_carlo_put_euro.py` | Pricing d'un put européen par Monte Carlo (mouvement brownien géométrique). Comparaison Python, NumPy, Numba. |
| `suite_de_Fibonacci.py` | Calcul de la suite de Fibonacci : récursion naïve, récursion mémoïsée (`lru_cache`), méthode itérative et générateur. |

---

## arbres_binomiaux.py — Détail des exercices

### Paramètres du modèle

| Paramètre | Valeur | Description |
|---|---|---|
| `S0` | 36.0 | Prix spot initial du sous-jacent |
| `K` | 40.0 | Strike (prix d'exercice) |
| `T` | 1.0 | Maturité (en années) |
| `r` | 0.06 | Taux sans risque continu |
| `σ` | 0.20 | Volatilité annualisée |
| `M` | 4 / 500 | Nombre de pas temporels |

### Exercice 1 — Python pur

Construction de l'arbre par double boucle Python. Les nœuds sont stockés dans un `ndarray` triangulaire : un mouvement haussier correspond à un déplacement latéral, ce qui réduit la taille de la matrice.

```
u = e^(σ√Δt)    d = 1/u    Δt = T/M
```

Temps mesuré pour M = 4 et M = 500 avec `time.time()`.

### Exercice 2 — NumPy vectorisé

Construction sans boucle Python en exploitant la formule analytique :

$$S_{i,t} = S_0 \cdot u^{t-i} \cdot d^i$$

Une seule opération NumPy génère l'arbre entier via deux matrices `up` et `down` représentant les mouvements nets.

### Exercice 3 — Numba JIT

Compilation dynamique de la fonction Python pur avec `numba.jit`. Le premier appel déclenche la compilation JIT (non mesuré) ; les appels suivants bénéficient de la vitesse du code compilé.

```python
simulate_tree_nb = numba.jit(simulate_tree)
```

### Exercice 4 — Cython *(à venir)*

Variante compilée en C via Cython pour une performance maximale. Nécessite un compilateur C et une étape de compilation séparée.

### Exercice 5 — Affichage graphique (Matplotlib)

Représentation visuelle de l'arbre binomial avec M = 20 périodes. Chaque nœud affiche le prix du sous-jacent, avec des arêtes représentant les mouvements haussiers et baissiers.

### Exercice 6 — Valorisation d'options européennes

Application financière complète de l'arbre binomial incluant :

1. **Backward induction** — Calcul du prix Call/Put par remontée de l'arbre sous probabilité risque-neutre `q` :

$$q = \frac{e^{r\Delta t} - d}{u - d}$$

2. **Black-Scholes-Merton** — Formule fermée utilisée comme benchmark analytique :

$$C = S_0 N(d_1) - K e^{-rT} N(d_2)$$

3. **Parité Call-Put** — Vérification de la relation fondamentale :

$$C - P = S_0 - K e^{-rT}$$

4. **Greeks** — Calcul par différences finies depuis l'arbre (Delta, Gamma, Theta) comparés aux formules analytiques BS.

5. **Convergence** — Graphique montrant la convergence oscillante du prix binomial vers le prix Black-Scholes quand M → ∞.

---

## Comparatif de performance (M = 500)

| Implémentation | Temps (ordre de grandeur) |
|---|---|
| Python pur (boucles) | ~1 s |
| NumPy vectorisé | ~4 ms |
| Numba JIT | ~1 ms |

> Les temps exacts dépendent de la machine. Le premier appel Numba inclut la compilation JIT et ne doit pas être mesuré.

---

## Dépendances

```
numpy
scipy
matplotlib
numba
llvmlite
```
