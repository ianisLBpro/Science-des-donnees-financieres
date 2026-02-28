"""
module 2 - Series temporelles financières
3_Analyse_de_correlation : 

Dans ce module nous allons aborder un autre exemple de traitement des données temporelles financières avec pandas.
Considérons la corrélation entre l'indice S&P 500 et l'indice de volatilité VIX.
Nous allons constater que lorsque le S&P 500 augmente, le VIX diminue, et inversement.

Il s'agit bien d'une corrélation, et non d'un lien de causalité.
Nous allons donc montrer certaines évidences statistiques qui supporte ce constat de corrélation hautement négative entre les 2 indices.
"""


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import yfinance as yf


plt.style.use('seaborn-v0_8')
mpl.rcParams['font.family'] = 'serif'



# Récupération des données financières via yfinance
print("=== Téléchargement du S&P 500 et du VIX ===")
START = '2010-01-01'
END = '2018-06-29'

# Télécharger les données du S&P 500 et du VIX
raw = yf.download(['^GSPC', '^VIX'], start=START, end=END, auto_adjust=True)
# yfinance retourne un MultiIndex (Price, Ticker) donc on prend la colonne 'Close' pour chaque ticker
data = raw['Close'].copy()
# Renommer les colonnes Yahoo Finance pour correspondre à nos conventions
data.rename(columns={'^GSPC': '.SPX', '^VIX': '.VIX'}, inplace=True)
# Nous ne conserverons que les lignes de données complètes
data.dropna(inplace=True)
# Renommer l'index en 'Date'
data.index.name = 'Date'

# Affichage des 5 dernières lignes du dataset
print("\n=== data.tail() ===")
print(data.tail())

# Affichage graphique des séries temporelles du S&P 500 et du VIX en subplots
data.plot(subplots=True, figsize=(10, 6))
plt.suptitle('Données temporelles S&P 500 et VIX (subplots)')
plt.tight_layout()
plt.savefig('./Module 2 - Series temporelles financières/Figures_series_temporelles_financieres/fig_SPX_VIX_subplots.png', dpi=150, bbox_inches='tight')
plt.show()

# Deux séries S&P 500 et VIX sur le même tracé avec double axe Y
# .loc[:'DATE'] sélectionne les données jusqu'à la date demandée
data.loc[:'2012-12-31'].plot(secondary_y='.VIX', figsize=(10, 6))
plt.title('Données temporelles S&P 500 et VIX (double axe Y)')
plt.tight_layout()
plt.savefig('./Module 2 - Series temporelles financières/Figures_series_temporelles_financieres/fig_SPX_VIX_double_axe_y.png', dpi=150, bbox_inches='tight')
plt.show()




'''
Exercice 1 : Calcul des log returns
Les analyses statistiques cherchent à obtenir des rendements et non des variations absolues, ni des valeurs absolues. 
Nous allons donc calculer les rendements logarithmiques (log returns) avant tout autres analyses.

Nous pouvons constater la forte variabilité du rendement logarithmique sur les prochains graphiques.
Nous voyons également des grappes de volatilité (volatility clustering) pour les deux indices. 

De manière générale, les périodes de forte volatilité d'un indice boursier sont accompagnées par le même phénomène au niveau de l'indice de volatilité VIX.
'''

# Calcul des rendements logarithmiques (log returns)
rets = np.log(data / data.shift(1))

# Affichage des 5 premières lignes des rendements logarithmiques
print("\n=== rets.head() ===")
print(rets.head())

# Nous ne conserverons que les lignes de données complètes pour les rendements logarithmiques
rets.dropna(inplace=True)

# Affichage graphique des rendements logarithmiques du S&P 500 et du VIX en subplots
rets.plot(subplots=True, figsize=(10, 6))
plt.suptitle('Rendements logarithmiques du S&P 500 et du VIX (subplots)')
plt.tight_layout()
plt.savefig('./Module 2 - Series temporelles financières/Figures_series_temporelles_financieres/fig_SPX_VIX_log_returns_subplots.png', dpi=150, bbox_inches='tight')
plt.show()

# Affichage graphique des rendements logarithmiques sous forme de scatter matrix
pd.plotting.scatter_matrix(rets, alpha=0.2, diagonal='hist', hist_kwds={'bins': 35}, figsize=(10, 6))
plt.suptitle('Scatter matrix des rendements logarithmiques du S&P 500 et du VIX')
plt.tight_layout()
plt.savefig('./Module 2 - Series temporelles financières/Figures_series_temporelles_financieres/fig_SPX_VIX_log_returns_scatter_matrix.png', dpi=150, bbox_inches='tight')
plt.show()




'''
Exercice 2 : Régression linéaire OLS et corrélation

'''

# Régression linéaire OLS (Ordinary Least Squares) entre les rendements logarithmiques du S&P 500 et du VIX
reg = np.polyfit(rets['.SPX'], rets['.VIX'], deg=1) 
print(f"\n=== OLS Regression ===")
print(f"Pente : {reg[0]:.4f}, Ordonnée à l'origine : {reg[1]:.4f}")

# Affichage graphique du scatter plot des rendements logarithmiques du S&P 500 et du VIX avec la ligne de régression OLS
ax = rets.plot(kind='scatter', x='.SPX', y='.VIX', figsize=(10, 6))  
ax.plot(rets['.SPX'], np.polyval(reg, rets['.SPX']), 'r', lw=2)      
plt.title('OLS Regression VIX log returns et S&P 500 log returns')
plt.tight_layout()
plt.savefig('./Module 2 - Series temporelles financières/Figures_series_temporelles_financieres/fig_SPX_VIX_log_returns_ols_regression.png', dpi=150, bbox_inches='tight')
plt.show()




'''
Exercice 3 : Corrélation statique et corrélation glissante (rolling correlation)
'''

# Calcul de la corrélation statique entre les rendements logarithmiques du S&P 500 et du VIX
print("\n=== rets.corr() ===")
print(rets.corr())

# Affichage graphique de la corrélation statique et mobile entre les rendements logarithmiques du S&P 500 et du VIX avec une fenêtre de 252 jours (environ 1 an de trading)
ax = rets['.SPX'].rolling(window=252).corr(rets['.VIX']).plot(figsize=(10, 6))    
ax.axhline(rets.corr().iloc[0, 1], c='r')  
plt.title('Corrélation statique et mobile entre les rendements logarithmiques du S&P 500 et du VIX')
plt.ylabel('Correlation')
plt.tight_layout()
plt.savefig('./Module 2 - Series temporelles financières/Figures_series_temporelles_financieres/fig_SPX_VIX_log_returns_rolling_correlation.png', dpi=150, bbox_inches='tight')
plt.show()