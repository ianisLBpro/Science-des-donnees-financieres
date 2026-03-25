# Module 0 — Performance de Python

Ce module explore différentes stratégies d'optimisation des performances en Python appliquées à des problèmes financiers et classiques. Chaque exercice compare plusieurs implémentations (boucles Python, vectorisation NumPy, compilation JIT avec Numba) pour mettre en évidence les gains de performance.

---

## Exercices et scripts

| Fichier | Description |
|---|---|
| `Recherches_nb_premiers.py` | Test de primalité sur un nombre donné et génération de séries de nombres premiers. Comparaison Python pur vs Numba JIT. |
| `Recherches_suite_fibonacci.py` | Calcul du n-ième nombre de Fibonacci selon trois approches : récursion naïve, récursion mémoïsée (`lru_cache`), méthode itérative. Générateur pour afficher la suite complète. |
| `Simulation_monte_carlo_put_euro.py` | Pricing d'un put européen par simulation Monte Carlo de trajectoires GBM (schéma d'Euler-Maruyama, dynamique Black-Scholes). Comparaison : boucles Python vs NumPy vectorisé vs Numba JIT. |
| `Recherche_nb_Pi.py` | Estimation du nombre π par méthode de Monte Carlo (points aléatoires dans un carré inscrit). Visualisation graphique, versions Python pur, NumPy vectorisée et Numba JIT. |
| `Arbres_binomiaux.py` | Construction d'un arbre binomial (Cox-Ross-Rubinstein 1979) : Python pur, NumPy vectorisé, Numba JIT, Cython (WIP). Affichage graphique Matplotlib. Valorisation d'options européennes (Call/Put) par backward induction sous probabilité risque-neutre, comparaison avec la formule fermée de Black-Scholes-Merton. |

---

## Détail des exercices

### 1. Test de primalité (`Recherches_nb_premiers.py`)
- Test interactif : l'utilisateur saisit un nombre, le script vérifie s'il est premier
- Génération d'une série de n premiers nombres premiers
- Chaque opération est chronométrée en Python pur puis en Numba JIT
- Nombre suggéré pour observer l'écart de performance : `100109100129162907`

### 2. Suite de Fibonacci (`Recherches_suite_fibonacci.py`)
- **Récursion naïve** : complexité exponentielle O(2^n), lente au-delà de n=32
- **Récursion mémoïsée** (`functools.lru_cache`) : complexité linéaire, limitée par la profondeur de récursion (~999)
- **Méthode itérative** : complexité linéaire, sans limite de récursion
- **Générateur** : affichage de la suite complète du 1er au n-ième terme
- Chaque méthode est chronométrée indépendamment

### 3. Pricing Monte Carlo d'un put européen (`Simulation_monte_carlo_put_euro.py`)
- Simulation de 50 000 trajectoires GBM sur 100 pas temporels (schéma d'Euler-Maruyama)
- Paramètres : S0=36, K=40, T=1 an, r=6%, σ=20%
- Estimateur Monte Carlo du put : `P₀ = e^{-rT} × (1/I) × Σ max(K - S_T(i), 0)`
- Trois implémentations chronométrées : Python pur (double boucle), NumPy vectorisé, Numba JIT
- Histogramme de la distribution des prix à maturité avec moyenne et strike

### 4. Estimation de π (`Recherche_nb_Pi.py`)
- Méthode de Monte Carlo : ratio points dans le cercle unité / points dans le carré [-1,1]²
- Visualisation graphique des 10 000 points avec cercle et carré inscrits
- Estimation avec 10 000 000 de points en Python pur, NumPy vectorisé et Numba JIT
- Comparaison des temps d'exécution

### 5. Arbre binomial (`Arbres_binomiaux.py`)
- **Exercice 1** : Construction par boucles Python (schéma CRR avec facteurs u et d)
- **Exercice 2** : Construction par NumPy vectorisé (mouvements nets hausse/baisse)
- **Exercice 3** : Compilation Numba JIT de la version Python
- **Exercice 4** : Cython (WIP — nécessite une image Docker)
- **Exercice 5** : Affichage graphique de l'arbre avec Matplotlib (nœuds, connexions, prix)
- **Exercice 6** : Valorisation d'options européennes Call/Put par backward induction sous probabilité risque-neutre q, benchmark avec la formule fermée de Black-Scholes-Merton

---

## Dépendances

- `numpy`
- `scipy`
- `matplotlib`
- `numba`
- `llvmlite`

---

## Exécution
```bash
python '<nom_du_script>.py'
```

Ou ouvrir directement dans VS Code.