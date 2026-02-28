# Module 2 — Séries temporelles financières

Ce module est dédié à l'analyse de séries temporelles financières avec **pandas** et **yfinance**. Il couvre l'importation et l'inspection de données de marché, le calcul de statistiques descriptives et de rendements, les statistiques mobiles (indicateurs techniques), l'analyse de corrélation entre indices, et le traitement de données intraday à haute fréquence.

---

## Description des fichiers

### 1. `1_Donnees_financieres.py`

Importation, statistiques descriptives, rendements logarithmiques et rééchantillonnage sur 12 instruments financiers (2016–2026).

| Étape | Description |
|---|---|
| 0 | Téléchargement via yfinance de 12 instruments (actions, indices, matières premières, forex) |
| 1 | Inspection avec `.info()`, `.head()`, `.tail()`, `.describe()`, `.aggregate()` |
| 1 | Calcul des différences absolues (`.diff()`) et des rendements simples (`.pct_change()`) |
| 1 | Tracé multiple des séries temporelles et bar plot des rendements moyens quotidiens |
| 2 | Calcul des rendements logarithmiques (`np.log`) |
| 2 | Tracé de l'évolution cumulative des rendements (`cumsum` + `exp`) |
| 2 | Rééchantillonnage hebdomadaire (`'W'`) et mensuel (`'ME'`) avec `.resample().last()` |

### 2. `2_Statistiques_mobiles.py`

Statistiques et moyennes mobiles sur la série Apple (AAPL), avec application à une stratégie d'analyse technique simple.

| Exercice | Description |
|---|---|
| 1 | Calcul des statistiques mobiles sur fenêtre de 20 jours : min, mean, std, median, max, EWMA (`halflife=0.5`) |
| 1 | Visualisation des bandes min/max/moyenne sur les 200 dernières observations |
| 2 | Moyennes mobiles simples SMA court terme (42 j) et long terme (252 j) |
| 2 | Signal de position longue/courte (+1 / −1) basé sur le croisement des deux SMA |
| 2 | Tracé du prix, des deux SMA et des positions sur axe secondaire |

### 3. `3_Analyse_de_correlation.py`

Analyse de la corrélation négative entre l'indice S&P 500 et l'indice de volatilité VIX (2010–2018).

| Exercice | Description |
|---|---|
| — | Téléchargement et visualisation des séries S&P 500 / VIX (subplots et double axe Y) |
| 1 | Calcul des rendements logarithmiques, visualisation des grappes de volatilité |
| 1 | Scatter matrix (`pd.plotting.scatter_matrix`) des log returns |
| 2 | Régression linéaire OLS (`np.polyfit`) entre les log returns VIX et S&P 500 |
| 2 | Scatter plot avec droite de régression (pente négative → corrélation négative) |
| 3 | Corrélation statique (`rets.corr()`) et corrélation glissante sur 252 jours |
| 3 | Visualisation de la corrélation mobile autour de la corrélation statique de référence |

### 4. `4_Donnees_a_haute_frequence.py`

Traitement de données intraday tick-by-tick EUR/USD au pas de 1 minute, avec simulation Bid/Ask et rééchantillonnage.

| Étape | Description |
|---|---|
| — | Téléchargement intraday EUR/USD à 1 minute via yfinance (`period='1d'`, `interval='1m'`) |
| — | Simulation Bid/Ask à partir du prix `Close` : `Bid = Close − half_spread`, `Ask = Close + half_spread` (spread EUR/USD ≈ 1 pip) |
| — | Calcul du prix Mid (moyenne Bid/Ask) et tracé de la série tick |
| — | Rééchantillonnage à 5 minutes (`resample('5min').last()`) et tracé de la série rééchantillonnée |

> **Note :** Les données Bid/Ask réelles sont normalement fournies par des plateformes spécialisées (FXCM, Interactive Brokers, etc.). Ici elles sont simulées à partir des données `Close` de yfinance.

---

## Figures générées

Tous les graphiques sont sauvegardés dans `Figures_series_temporelles_financieres/` :

| Fichier | Description |
|---|---|
| `fig_Tracé_multiple_en_ligne.png` | Séries temporelles des 12 instruments en subplots |
| `fig_Barplot_rendements_moyens_quotidiens.png` | Bar plot des rendements moyens quotidiens par instrument |
| `fig_Evolution_cumulative_rendements_logarithmiques.png` | Évolution cumulative des log returns (journalier) |
| `fig_Evolution_cumulative_rendements_logarithmiques_mensuel.png` | Évolution cumulative des log returns (mensuel) |
| `fig_Statistiques_mobiles_Apple.png` | Bandes min/mean/max mobiles sur AAPL |
| `fig_Apple_&_SMA.png` | Prix AAPL + SMA 42 j et SMA 252 j |
| `fig_Apple_&_SMA_positions.png` | Prix AAPL + SMA + signal de position long/short |
| `fig_SPX_VIX_subplots.png` | Séries S&P 500 et VIX en subplots |
| `fig_SPX_VIX_double_axe_y.png` | S&P 500 et VIX sur double axe Y |
| `fig_SPX_VIX_log_returns_subplots.png` | Log returns S&P 500 et VIX en subplots |
| `fig_SPX_VIX_log_returns_scatter_matrix.png` | Scatter matrix des log returns |
| `fig_SPX_VIX_log_returns_ols_regression.png` | Scatter plot + droite de régression OLS |
| `fig_SPX_VIX_log_returns_rolling_correlation.png` | Corrélation glissante 252 j S&P 500 / VIX |
| `fig_tick_mid_EURUSD.png` | Données de tick Mid EUR/USD (1 min) |
| `fig_tick_resam_5min_EURUSD.png` | Données tick Mid EUR/USD rééchantillonnées à 5 min |

---

## Dépendances principales

- numpy
- pandas
- matplotlib
- yfinance

---

## Exécution

> **Prérequis :** environnement virtuel activé (voir [INSTALLATION.md](../INSTALLATION.md))

```bash
python '.\Module 2 - Series temporelles financières\<nom_du_script>.py'
```

Ou ouvrir directement dans **VS Code**.
