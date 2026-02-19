# La Science des Données Financières

Ce projet regroupe l'ensemble de mes travaux réalisés dans le cadre de l'étude de la science des données appliquée à la finance. Il couvre un large spectre de sujets allant de l'optimisation des performances Python jusqu'à l'apprentissage machine, en passant par la visualisation de données, les outils mathématiques et la modélisation stochastique.

## Technologies utilisées

| Catégorie | Librairies |
|---|---|
| Calcul scientifique | `numpy`, `scipy`, `pandas` |
| Visualisation | `matplotlib`, `seaborn`, `plotly`, `cufflinks` |
| Finance | `yfinance` |
| Performance | `numba` |
| Notebooks | `jupyter`, `ipykernel`, `ipywidgets` |

> **Python 3.14** — Voir le fichier [INSTALLATION.md](INSTALLATION.md) pour la mise en place de l'environnement virtuel.

---

## Structure du projet

### Module 0 — Performance de Python

Ce module explore les différentes stratégies d'optimisation des performances en Python à travers des problèmes classiques et financiers. Chaque exercice compare plusieurs implémentations (boucles Python, vectorisation NumPy, compilation JIT avec Numba) pour mettre en évidence les gains de performance.

| Fichier | Description |
|---|---|
| `arbres_binomiaux.py` | Construction d'un arbre binomial pour modéliser l'évolution d'un cours d'action et valoriser une option européenne (call/put) par induction rétrograde en probabilité risque-neutre. Inclut une analyse de scénarios (perte/gain max, ratio risque/rendement). |
| `nb_pi_test.py` | Estimation du nombre π par la méthode de Monte Carlo (points aléatoires dans un cercle unité). Comparaison de trois implémentations : boucle Python, vectorisation NumPy et visualisation graphique. |
| `nb_premiers_test.py` | Test de primalité accéléré par le compilateur JIT de Numba pour illustrer les gains de performance. |
| `simulation_monte_carlo_put_euro.py` | Pricing d'un put européen par simulation Monte Carlo de trajectoires de mouvement brownien géométrique (dynamique Black-Scholes). Comparaison : boucles Python vs NumPy vs Numba. |
| `suite_de_Fibonacci.py` | Calcul des nombres de Fibonacci selon trois approches : récursion naïve, récursion mémoïsée (`lru_cache`) et méthode itérative, avec un générateur pour afficher la suite. |

---

### Module 1 — Visualisation des données

Ce module est dédié à la visualisation graphique des données financières au moyen de **Matplotlib** (tracés statiques) et **Plotly** (tracés interactifs).

| Fichier | Description |
|---|---|
| `1_traces_2D_statiques.py` | Tour complet des tracés 2D statiques avec Matplotlib : lignes, sommes cumulées, double axe Y, sous-tracés, scatter plots, histogrammes, boîtes à moustaches et intégrale sous une courbe avec annotations LaTeX. |
| `2_traces_3D_statiques.py` | Tracés 3D statiques : surface de volatilité implicite (strike × maturité) et nuage de points 3D avec angles de vue personnalisés. |
| `3_traces_2D_interactifs.py` | Tracés interactifs avec Plotly exportés en HTML : séries temporelles, histogrammes de rendements, boxplots et graphique en chandelier (candlestick) à partir de données OHLC simulées. |
| `4_financial_plots_2D_interactifs.ipynb` | Notebook Jupyter téléchargeant des données de marché réelles via `yfinance` et produisant des graphiques financiers interactifs Plotly : volatilité, donut/pie charts, jauge, chandelier, OHLC, lignes, et sous-tracés prix/volume. |

Les graphiques interactifs générés sont disponibles dans les dossiers `Financial_plot_2D_interactifs/` et `Test_trace_2D_interactifs/`.

---

### Module 2 — Séries temporelles financières

Ce module est consacré à l'analyse des séries temporelles financières.

| Fichier | Description |
|---|---|
| `Donnees_financieres.py` | *À venir* — Récupération et manipulation de données financières. |

---

### Module 3 — Outils mathématiques

Ce module couvre les outils mathématiques fondamentaux utilisés en finance quantitative.

| Fichier | Description |
|---|---|
| `1_Approximation_Regression_Interpolation.py` | 10 exercices progressifs : régression polynomiale (`polyfit`/`polyval`), fonctions de base personnalisées par moindres carrés (`linalg.lstsq`), bases sinusoïdales, données bruitées, régression multidimensionnelle (surface 3D), et interpolation par splines (linéaire et cubique). |
| `2_Optimisation_convexe.py` | *À venir* — Optimisation convexe. |
| `3_Integration.py` | *À venir* — Intégration numérique. |
| `4_Calcul_formel_ou_symbolique.py` | *À venir* — Calcul formel et symbolique. |

---

### Module 4 — Stochastique

Ce module traite de la modélisation stochastique appliquée à la finance.

| Fichier | Description |
|---|---|
| `1_Nombres_aleatoires.py` | *À venir* — Génération de nombres aléatoires. |
| `2_Simulation.py` | *À venir* — Simulation de processus stochastiques. |
| `3_Evaluation.py` | *À venir* — Évaluation et pricing stochastique. |
| `4_Mesure_du_risque.py` | *À venir* — Mesures de risque (VaR, CVaR, etc.). |

---

### Module 5 — Statistiques

Ce module aborde les méthodes statistiques appliquées à la finance et à la gestion de portefeuille.

| Fichier | Description |
|---|---|
| `1_Tests_de_normalite.py` | *À venir* — Tests de normalité des rendements financiers. |
| `2_Optimisation_de_portefeuille.py` | *À venir* — Optimisation de portefeuille (Markowitz, frontière efficiente). |
| `3_Statistiques_bayésiennes.py` | *À venir* — Inférence bayésienne appliquée à la finance. |
| `4_Apprentissage_machine.py` | *À venir* — Apprentissage machine pour la prédiction financière. |

---

## Exécution

### Scripts Python
```bash
python '.\Module X - Nom du module\<nom_du_script>.py'
```

### Notebooks Jupyter
```bash
jupyter nbconvert --execute --to html "<nom_du_notebook>.ipynb"
```

Ou ouvrir directement dans VS Code / Jupyter Lab.
