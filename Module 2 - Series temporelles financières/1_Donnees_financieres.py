'''
Module 2 - Financial Time Series
1_Données financières : Importation, génération de statistiques, calcul des changements au cours du temps et rééchantillonnage.

Etape 0 : Importation des données financières avec yfinance
Etape 1 : Inspection et statistiques descriptives
Etape 2 : Calcul des rendements logarithmiques et rééchantillonnage
'''


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import yfinance as yf


plt.style.use('seaborn-v0_8')  
mpl.rcParams['font.family'] = 'serif'



'''
Étape 0 : Importation des données financières avec yfinance
On utilise yfinance pour télécharger les données financières de 12 instruments (actions, indices, matières premières, taux de change) sur une période donnée.
'''

ric_to_yahoo = {
    'AAPL.O': 'AAPL',
    'MSFT.O': 'MSFT',
    'INTC.O': 'INTC',
    'AMZN.O': 'AMZN',
    'GS.N':   'GS',
    'SPY':    'SPY',
    '.SPX':   '^GSPC',
    '.VIX':   '^VIX',
    'EUR=':   'EURUSD=X',
    'XAU=':   'GC=F',
    'GDX':    'GDX',
    'GLD':    'GLD',
}

instruments = ['Apple Stock', 'Microsoft Stock',
               'Intel Stock', 'Amazon Stock', 'Goldman Sachs Stock',
               'SPDR S&P 500 ETF Trust', 'S&P 500 Index',
               'VIX Volatility Index', 'EUR/USD Exchange Rate',
               'Gold Price', 'VanEck Vectors Gold Miners ETF',
               'SPDR Gold Trust']

# Période : 2016-01-01 à 2026-01-01
START = '2016-01-01'
END = '2026-01-01'

print("=== Téléchargement des données via yfinance ===")
yahoo_tickers = list(ric_to_yahoo.values())
raw_yf = yf.download(yahoo_tickers, start=START, end=END, auto_adjust=True)

# yfinance retourne un MultiIndex (Price, Ticker).
# On prend la colonne 'Close' pour chaque ticker
data = raw_yf['Close'].copy()

# Renommer les colonnes Yahoo Finance
yahoo_to_ric = {v: k for k, v in ric_to_yahoo.items()}
data.rename(columns=yahoo_to_ric, inplace=True)

# Réordonner les colonnes selon un ordre cohérent 
ric_order = list(ric_to_yahoo.keys())
data = data[ric_order]
data.index.name = 'Date'

# Supprimer les lignes NaN (première ligne souvent)
# data.dropna(how='all', inplace=True)




'''
Étape 1 : Inspection et statistiques descriptives

Un analyste financier voudra tout d'abord se faire une première idée de la nature des données, par inspection ou par visualisation.

On utilise .info(), .head(), .tail() pour inspecter les données.
On utilise .describe(), .mean(), .aggregate() pour obtenir des statistiques descriptives de base.
On utilise .diff(), .pct_change() pour calculer les changements au cours du temps (différences absolues et rendements simples).

Les tracés de séries temporelles et les statistiques descriptives permettent de mieux comprendre les caractéristiques de chaque série.
Le Bar plot des rendements moyens quotidiens permet de comparer rapidement la performance moyenne de chaque instrument.
Attention à certains comme le VIX qui a une échelle et une nature très différentes des autres.
'''

# Informations sur les données importées
print("\n=== data.info() ===")
data.info()

# Affichage des 5 premières lignes 
print("\n=== data.head() ===")
print(data.head())

# Affichage des 5 dernières lignes
print("\n=== data.tail() ===")
print(data.tail())

# Plot de la série temporelle format tracé multiple en ligne pour les 12 instruments
data.plot(figsize=(10, 12), subplots=True)
plt.suptitle('Séries temporelles financières en tracé multiple en ligne', y=1.01)
plt.tight_layout()
plt.savefig('./Module 2 - Series temporelles financières/Figures_series_temporelles_financieres/fig_Tracé_multiple_en_ligne.png', dpi=150, bbox_inches='tight')
plt.show()

# Liste des instruments et leurs Tickers format tableau
print("\n=== Liste des instruments ===")
for ric, name in zip(data.columns, instruments):
    print('{:8s} | {}'.format(ric, name))

# Descriptions statistiques de base arrondies à 2 décimales
print("\n=== data.describe() ===")
print(data.describe().round(2))

# Moyennes par colonne arrondies à 2 décimales
print("\n=== data.mean() ===")
print(data.mean().round(2))

# Statistiques agrégées personnalisées (min, mean, std, median, max) arrondies à 2 décimales
print("\n=== data.aggregate(['min', 'mean', 'std', 'median', 'max']) ===")
print(data.aggregate(['min', 'mean', 'std', 'median', 'max']).round(2))

# Différences absolues
print("\n=== data.diff().head() ===")
print(data.diff().head())

# Moyenne des différences absolues arrondie à 3 décimales
print("\n=== data.diff().mean() ===")
print(data.diff().mean().round(3))

# Variations en pourcentage (rendements simples) arrondies à 3 décimales
print("\n=== data.pct_change().head() ===")
print(data.pct_change().round(3).head())

# Affichage de la moyenne des variations en pourcentage par colonne (Bar plot)
data.pct_change().mean().plot(kind='bar', figsize=(10, 6))
plt.title('Bar plot des rendements moyens quotidiens')
plt.tight_layout()
plt.savefig('./Module 2 - Series temporelles financières/Figures_series_temporelles_financieres/fig_Barplot_rendements_moyens_quotidiens.png', dpi=150, bbox_inches='tight')
plt.show()



'''
Étape 2 : Calcul des rendements logarithmiques et rééchantillonnage

Les rendements logarithmiques (log returns) sont calculés avec np.log(data / data.shift(1)).
Le calcul des rendements logarithmiques est vectorisé, ce qui est plus rapide que l'utilisation de .apply() ou de boucles.
Il permet de mesurer les changements relatifs de manière plus symétrique et est souvent préféré en finance.

L'évolution cumulative des rendements logarithmiques est tracée avec rets.cumsum().apply(np.exp).plot().
Cela permet de visualiser la croissance d'une unité de capital investie dans chaque instrument au fil du temps, en tenant compte des rendements composés.

Le rééchantillonnage hebdomadaire et mensuel est effectué avec data.resample('W', label='right').last() et data.resample('ME', label='right').last() respectivement.
Cela permet d'obtenir des séries temporelles à des fréquences plus basses, ce qui peut être utile pour certaines analyses ou visualisations.
'''

# Calcul des rendements logarithmiques (log returns) 
rets = np.log(data / data.shift(1))  # Calcul vectorisé des log returns

# Affichage des 5 premières lignes des rendements logarithmiques arrondies à 3 décimales
print("\n=== rets.head() ===")
print(rets.head().round(3))

# Tracé de l'évolution cumulative des rendements logarithmiques (cumulative log returns) 
rets.cumsum().apply(np.exp).plot(figsize=(10, 6))
plt.title('Évolution cumulative des rendements logarithmiques')
plt.ylabel('Prix normalisé')
plt.tight_layout()
plt.savefig('./Module 2 - Series temporelles financières/Figures_series_temporelles_financieres/fig_Evolution_cumulative_rendements_logarithmiques.png', dpi=150, bbox_inches='tight')
plt.show()

# Rééchantillonnage hebdomadaire (weekly) 
# EOD (End of Day) data rééchantillonnée en intervalles hebdomadaires
# .last() → on garde la dernière valeur de chaque semaine
print("\n=== Rééchantillonnage hebdomadaire ===")
print(data.resample('W', label='right').last().head()) # label='right' → on prend la date de fin de semaine (évite le foresight bias)

# Rééchantillonnage mensuel (monthly)
# EOD (End of Day) data rééchantillonnée en intervalles mensuels
# .last() → on garde la dernière valeur de chaque mois
print("\n=== Rééchantillonnage mensuel ===")
print(data.resample('ME', label='right').last().head()) # label='right' → on prend la date de fin de mois (évite le foresight bias)

# Tracé de l'évolution cumulative des rendements logarithmiques rééchantillonnés mensuellement
# cumsum() sur les log returns → apply(np.exp) → rééchantillonnage mensuel → plot
rets.cumsum().apply(np.exp).resample('ME', label='right').last().plot(figsize=(10, 6))
plt.title('Évolution cumulative des rendements logarithmiques (rééchantillonnés mensuellement)')
plt.ylabel('Prix normalisé')
plt.tight_layout()
plt.savefig('./Module 2 - Series temporelles financières/Figures_series_temporelles_financieres/fig_Evolution_cumulative_rendements_logarithmiques_mensuel.png', dpi=150, bbox_inches='tight')
plt.show()

'''
NOTE IMPORTANTE SUR LE RÉÉCHANTILLONNAGE :
Lors du rééchantillonnage, pandas prend par défaut le label gauche de l'intervalle. 
Pour être cohérent financièrement, il faut utiliser label='right' et .last() pour prendre la dernière valeur disponible dans l'intervalle. 
Sinon, on introduit un biais de prévision (foresight bias) dans l'analyse.
'''