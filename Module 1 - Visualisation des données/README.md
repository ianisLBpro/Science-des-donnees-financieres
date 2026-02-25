# Module 1 — Visualisation des données 📊

Ce module est dédié à la visualisation graphique des données financières au moyen de deux librairies complémentaires :

- **Matplotlib / Seaborn** — tracés statiques (2D et 3D)
- **Plotly** — tracés interactifs exportés en HTML

---

## Description des fichiers

### 1. `1_Traces_2D_statiques.py`

Tour complet des tracés 2D statiques avec Matplotlib :

| # | Tracé |
|---|---|
| 1 | Tracé 2D statique simple |
| 2 | Tracé 2D statique — somme cumulée |
| 3 | Tracé 2D avec style et échelle personnalisés |
| 4 | Tracé 2D avec limites d'axes spécifiques |
| 5 | Tracé 2D avec taille et labels personnalisés |
| 6 | Tracé 2D de deux jeux de données |
| 7 | Tracé 2D avec deux jeux de données légendés |
| 8 | Tracé 2D avec deux jeux de données — problèmes d'échelle |
| 9 | Tracé 2D avec deux jeux de données — résolution d'échelle (`twinx`) |
| 10 | Tracé 2D avec 2 sous-tracés séparés |
| 11 | Tracé combiné : lignes et barres |
| 12 | Scatter plot — `plt.plot` |
| 13 | Scatter plot — `plt.scatter` |
| 14 | Scatter plot avec échelle de couleur |
| 15 | Histogramme 2D avec deux séries de données |
| 16 | Histogramme 2D empilant deux jeux de données |
| 17 | Boîte à moustaches pour deux jeux de données |
| 18 | Tracé d'une fonction exponentielle avec intégrale |

### 2. `2_Traces_3D_statiques.py`

Tracés 3D statiques avec Matplotlib (`mpl_toolkits.mplot3d`) :

| # | Tracé |
|---|---|
| 1 | Surface de volatilité implicite en 3D (strike × maturité) |
| 2 | Nuage de points 3D avec les volatilités induites |

### 3. `3_Traces_2D_interactifs.py`

Tracés interactifs avec Plotly, exportés en fichiers HTML dans `Test_trace_2D_interactifs/` :

| # | Tracé |
|---|---|
| 1 | Tracé en ligne — séries temporelles |
| 2 | Histogramme des rendements quotidiens |
| 3 | Box plot des rendements quotidiens |
| 4 | Graphique en chandelier (*candlestick*) |

### 4. `4_Traces-2D_interactifs_TESTS.py`

Tracés interactifs avancés avec Plotly pur (remplacement de cufflinks, incompatible avec plotly >= 6 et numpy >= 2), exportés en HTML dans `Test_trace_2D_interactifs/` :

| Section | Tracé | Fichier |
|---|---|---|
| 1 | Tracé en ligne — toutes les colonnes | `ply_01.html` |
| 1 | Tracé en ligne avec personnalisations (mode, symboles, couleurs) | `ply_02.html` |
| 1 | Histogrammes par colonne (sous-graphiques) | `ply_03.html` |
| 2 | Graphique OHLC — EUR/USD | `qf_01.html` |
| 2 | OHLC + Bandes de Bollinger (SMA, upper/lower) | `qf_02.html` |
| 2 | OHLC + Bandes de Bollinger + RSI (sous-graphiques) | `qf_03.html` |

### 5. `Financial_plots_2D_interactifs.ipynb`

Notebook Jupyter téléchargeant des données de marché réelles via `yfinance` et produisant des graphiques financiers interactifs, exportés en HTML dans `Financial_plot_2D_interactifs/` :

| Graphique | Description |
|---|---|
| `volatility_plot` | Tracé de la volatilité historique |
| `donut_plot` | Répartition en anneau |
| `pie_plot` | Répartition en camembert |
| `gauge_plot` | Indicateur à jauge |
| `candlestick_plot` | Graphique en chandelier |
| `ohlc_plot` | Graphique OHLC |
| `line_plot` | Tracé en ligne |
| `sub_plot` | Sous-tracés prix / volume |

---

## Exécution

> **Prérequis :** environnement virtuel activé (voir [INSTALLATION.md](../INSTALLATION.md))

**Script Python :**
```bash
python '.\Module 1 - Visualisation des données\<nom_du_script>.py'
```

**Notebook Jupyter :**
```bash
jupyter nbconvert --execute --to html "Module 1 - Visualisation des données\<nom_du_notebook>.ipynb"
```

Ou ouvrir directement le `.ipynb` dans **VS Code** / **Jupyter Lab**.