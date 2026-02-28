# Science des Données Financières

Ce projet regroupe l'ensemble de mes travaux réalisés dans le cadre de l'étude de la science des données appliquée à la finance. Il couvre un large spectre de sujets allant de l'optimisation des performances Python jusqu'à l'apprentissage machine, en passant par la visualisation de données, les outils mathématiques et la modélisation stochastique.

## Technologies utilisées

| Catégorie | Librairies |
|---|---|
| Calcul scientifique | `numpy`, `scipy`, `pandas` |
| Visualisation | `matplotlib`, `seaborn`, `plotly` |
| Finance | `yfinance` |
| Performance | `numba`, `llvmlite`, `Cython` (WIP) |
| Big Data | `pyspark` |
| Notebooks | `jupyter`, `ipykernel`, `ipywidgets` |

> ⚠️ `cufflinks` est installé mais **incompatible avec `plotly >= 6` et `numpy >= 2`** — remplacé par Plotly pur dans tous les scripts.

> **Python 3.14.0** — Voir le fichier [INSTALLATION.md](INSTALLATION.md) pour la mise en place de l'environnement virtuel.

---

## Structure du projet

### Module 0 — Performance de Python

Ce module explore différentes stratégies d'optimisation des performances en Python appliquées à des problèmes financiers et classiques. Chaque exercice compare plusieurs implémentations (boucles Python, vectorisation NumPy, compilation JIT avec Numba) pour mettre en évidence les gains de performance.

| Fichier | Description |
|---|---|
| `Arbres_binomiaux.py` | Construction d'un arbre binomial (Cox-Ross-Rubinstein 1979) selon 6 approches : Python pur, NumPy vectorisé, Numba JIT, Cython (WIP - nécessite une image Docker), affichage graphique Matplotlib. Valorisation d'options européennes (Call/Put) par backward induction, comparaison avec Black-Scholes-Merton. |
| `Recherche_nb_pi.py` | Estimation du nombre π par la méthode de Monte Carlo. Visualisation des points aléatoires, version Python pur, version NumPy vectorisée, analyse de performance. |
| `Recherches_nb_premiers.py` | Test de primalité accéléré par Numba JIT pour illustrer les gains de performance sur des boucles Python. |
| `Simulation_monte_carlo_put_euro.py` | Pricing d'un put européen par simulation Monte Carlo de trajectoires de mouvement brownien géométrique (dynamique Black-Scholes). Comparaison : boucles Python vs NumPy vs Numba. |
| `Recherches_suite_fibonacci.py` | Calcul des nombres de Fibonacci selon trois approches : récursion naïve, récursion mémoïsée (`lru_cache`) et méthode itérative, avec un générateur pour afficher la suite. |

---

### Module 1 — Visualisation des données

Ce module est dédié à la visualisation graphique des données financières au moyen de **Matplotlib** (tracés statiques) et **Plotly** (tracés interactifs).

| Fichier | Description |
|---|---|
| `1_Traces_2D_statiques.py` | Tour complet des tracés 2D statiques avec Matplotlib : lignes, sommes cumulées, double axe Y, sous-tracés, scatter plots, histogrammes, boîtes à moustaches et intégrale sous une courbe avec annotations LaTeX. |
| `2_Traces_3D_statiques.py` | Tracés 3D statiques : surface de volatilité implicite (strike × maturité) et nuage de points 3D avec angles de vue personnalisés. |
| `3_Traces_2D_interactifs.py` | Tracés interactifs avec Plotly : séries temporelles, histogrammes de rendements, boxplots et graphique en chandelier (candlestick) à partir de données OHLC simulées. Exportés en HTML dans `Test_trace_2D_interactifs/`.|
| `4_Traces-2D_interactifs_TESTS.py` | Tracés interactifs avancés avec Plotly pur : line plots personnalisés, histogrammes par colonne, OHLC, Bandes de Bollinger et RSI (avec sous-graphiques). Exportés en HTML dans `Test_trace_2D_interactifs/`. |
| `Financial_plots_2D_interactifs.ipynb` | Notebook Jupyter téléchargeant des données de marché réelles via `yfinance` et produisant des graphiques financiers interactifs Plotly : volatilité, donut/pie charts, jauge, chandelier, OHLC, lignes, et sous-tracés prix/volume. |

Les graphiques interactifs générés sont disponibles dans les dossiers `Financial_plot_2D_interactifs/` et `Test_trace_2D_interactifs/`.

---

### Module 2 — Séries temporelles financières

Ce module est consacré à l'importation, l'analyse et la visualisation des séries temporelles financières avec `pandas`, `matplotlib` et `yfinance`.

| Fichier | Description |
|---|---|
| `1_Donnees_financieres.py` | Importation de 12 instruments financiers (actions, indices, ETF, taux de change, matières premières) via `yfinance` sur 2016–2026. **Étape 0** : téléchargement et mise en forme des données (MultiIndex `yfinance` → colonnes RIC). **Étape 1** : inspection et statistiques descriptives (`info`, `describe`, `aggregate`, `diff`, `pct_change`), tracé multiple en ligne et bar plot des rendements moyens. **Étape 2** : calcul des rendements logarithmiques vectorisés, évolution cumulative normalisée, rééchantillonnage hebdomadaire (`'W'`) et mensuel (`'ME'`). |
| `2_Statistiques_mobiles.py` | Statistiques et indicateurs mobiles sur l'action Apple (AAPL) avec fenêtre de 20 jours : min, mean, std, médiane, max et EWMA (`halflife=0.5`). Analyse technique par croisement de deux SMA (42 j et 252 j) avec génération d'un signal de position longue/courte (+1 / −1) tracé sur axe secondaire. |
| `3_Analyse_de_correlation.py` | Analyse de la corrélation négative entre S&P 500 et VIX (2010–2018). **Exercice 1** : calcul des rendements logarithmiques, visualisation des grappes de volatilité et scatter matrix. **Exercice 2** : régression linéaire OLS (`np.polyfit`) — pente négative confirmant la corrélation inverse. **Exercice 3** : corrélation statique (`rets.corr()`) et corrélation glissante sur 252 jours. |
| `4_Donnees_a_haute_frequence.py` | Données intraday EUR/USD à 1 minute via `yfinance`. Simulation Bid/Ask à partir du prix `Close` (demi-spread = 0.5 pip). Calcul du prix Mid et rééchantillonnage toutes les 5 minutes (`resample('5min').last()`). |

---

### Module 3 — Outils mathématiques

Ce module couvre les outils mathématiques fondamentaux utilisés en finance quantitative.

| Fichier | Description |
|---|---|
| `1_Approximation_Regression_Interpolation.py` | 10 exercices progressifs : régression polynomiale (`polyfit`/`polyval`), fonctions de base personnalisées par moindres carrés (`linalg.lstsq`), bases sinusoïdales, données bruitées, régression multidimensionnelle (surface 3D), et interpolation par splines (linéaire et cubique). |
| `2_Optimisation_convexe.py` | 4 exercices progressifs sur l'optimisation convexe avec `scipy.optimize` : visualisation 3D de la fonction objectif, minimisation globale par force brute (`sco.brute`) avec grille grossière puis fine (résultat : x = y ≈ −1.4, min ≈ −1.8), affinement par optimisation locale (`sco.fmin`) et illustration du piège du minimum local relatif selon le point de départ, et enfin optimisation contrainte (`sco.minimize`, méthode SLSQP) pour maximiser l'utilité espérée d'un portefeuille de deux actifs risqués sous contrainte budgétaire et d'absence de vente à découvert. |
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
python '.\Module 'X' - Nom du module\<nom_du_script>.py'
```

### Notebooks Jupyter
```bash
jupyter nbconvert --execute --to html "<nom_du_notebook>.ipynb"
```

Ou ouvrir directement dans VS Code / Jupyter Lab.
