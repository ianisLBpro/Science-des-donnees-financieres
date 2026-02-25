# Module 0 — Performance de Python

Ce module explore différentes stratégies d'optimisation des performances en Python appliquées à des problèmes financiers et classiques. Chaque exercice compare plusieurs implémentations (boucles Python, vectorisation NumPy, compilation JIT avec Numba) pour mettre en évidence les gains de performance.

---

## Exercices et scripts

| Fichier | Description |
|---|---|
| `Arbres_binomiaux.py` | Construction d'un arbre binomial (Cox-Ross-Rubinstein 1979) selon 6 approches : Python pur, NumPy vectorisé, Numba JIT, Cython (à venir), affichage graphique Matplotlib. Valorisation d'options européennes (Call/Put) par backward induction, comparaison avec Black-Scholes-Merton |
| `Recherche_nb_Pi.py` | Estimation du nombre π par la méthode de Monte Carlo. Visualisation des points aléatoires, version Python pur, version NumPy vectorisée, analyse de performance. |
| `Recherches_nb_premiers.py` | Test de primalité accéléré par Numba JIT pour illustrer les gains de performance sur des boucles Python. |
| `Simulation_monte_carlo_put_euro.py` | Pricing d'un put européen par simulation Monte Carlo de trajectoires de mouvement brownien géométrique (dynamique Black-Scholes). Comparaison : boucles Python vs NumPy vs Numba. |
| `Recherches_suite_fibonacci.py` | Calcul des nombres de Fibonacci selon trois approches : récursion naïve, récursion mémorisée (`lru_cache`) et méthode itérative, avec un générateur pour afficher la suite. |

---

## Détail des exercices

### 1. Arbre binomial (arbres_binomiaux.py)
- Construction par boucles Python, NumPy vectorisé, Numba JIT, Cython (à venir)
- Affichage graphique de l'arbre
- Valorisation d'options européennes (Call/Put) par backward induction
- Comparaison avec Black-Scholes-Merton

### 2. Estimation de π (recherche_nb_Pi.py)
- Méthode de Monte Carlo : points aléatoires dans un carré [-1,1]^2
- Calcul du rapport points dans le cercle / total
- Visualisation graphique
- Version Python pur, version NumPy vectorisée
- Analyse de performance

### 3. Test de primalité (recherches_nb_premiers.py)
- Implémentation classique et accélérée par Numba JIT
- Comparaison des temps d'exécution

### 4. Pricing Monte Carlo (simulation_monte_carlo_put_euro.py)
- Simulation de trajectoires de mouvement brownien géométrique
- Pricing d'un put européen
- Implémentations Python, NumPy, Numba
- Analyse de performance

### 5. Suite de Fibonacci (recherches_suite_fibonacci.py)
- Récursion naïve, récursion mémoïsée, méthode itérative
- Générateur Python pour afficher la suite
- Comparaison des performances

---

## Dépendances principales

- numpy
- scipy
- matplotlib
- numba
- llvmlite
- random

---

## Exécution

### Scripts Python
```bash
python '<nom_du_script>.py'
```

Ou ouvrir directement dans VS Code