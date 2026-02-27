''' 
Module 2 - Financial Time Series
2_Statistiques_mobiles : 

Dans ce module nous allons aborder les statistiques mobiles (rolling statistics) également appelés indicateurs financiers ou études financières. 
Ce sont les outils fondamentaux pour les chartistes et les traders techniques. 
'''


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import yfinance as yf


plt.style.use('seaborn-v0_8')  
mpl.rcParams['font.family'] = 'serif'


# =====================================================================================================
# On réutilise les données financières téléchargées dans le module précédent (1_Donnees_financieres.py)
# =====================================================================================================
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

# ========================================================================================================




'''
Exercice 1 : Aperçu général des données
Dans ces exercices nous n'utiliserons qu'une seule série financière temporelle. 
Nous verrons que produire des statistiques mobiles standard avec pandas est très simple.
'''

# Isoler la série temporelle de l'action Apple (AAPL.O)
sym = 'AAPL.O'
data = pd.DataFrame(data[sym]).dropna()
print("\n=== data.tail() ===")
print(data.tail())

# Définir la fenêtre mobile, c'est-à-dire le nombre de valeurs d'index à utiliser
window = 20 

# Calcule de la valeur minimale mobile 
data['min'] = data[sym].rolling(window=window).min()
# Calcule de la valeur moyenne mobile
data['mean'] = data[sym].rolling(window=window).mean()
# Calcule de l'écart-type mobile
data['std'] = data[sym].rolling(window=window).std()
# Calcule de la médiane mobile
data['median'] = data[sym].rolling(window=window).median()
# Calcule de la valeur maximale mobile
data['max'] = data[sym].rolling(window=window).max()
# Calcule la moyenne mobile pondérée exponentielle avec décroissance en termes de demi-vie de 0.5
data['ewma'] = data[sym].ewm(halflife=0.5, min_periods=window).mean()

# Afficher les 5 premières lignes de la DataFrame avec les statistiques mobiles
print("\n=== data.dropna().head() ===")
print(data.dropna().head())

# Affichage graphique des statistiques mobiles pour les valeurs minimale, moyenne et maximale 
# Visualisation de trois des statistiques mobiles pour les 200 dernières lignes de données
ax = data[['min', 'mean', 'max']].iloc[-200:].plot(figsize=(10, 6), style=['g--', 'r--', 'g--'], lw=0.8) 
# Ajout au tracé les données de la série temporelle d'origine 
data[sym].iloc[-200:].plot(ax=ax, lw=2.0)              
plt.title('Prix de l\'action Apple et statistiques mobiles')
# Ajustement de la mise en page pour éviter les chevauchements
plt.tight_layout()
plt.savefig('./Module 2 - Series temporelles financières/Figures_series_temporelles_financieres/fig_Statistiques_mobiles_Apple.png', dpi=150, bbox_inches='tight')
plt.show()




'''
Exercice 2 : Exemple d'analyse technique
Les statistiques mobiles constituent l'un des outils principaux de l'analyse technique des actions. 
En comparaison l'analyse fondamentale se concentre sur les rapports financiers des entreprises et les positions stratégiques qu'elles adoptent. 

Une des technique utilisée depuis plusieurs décennies en analyse technique se fonde sur deux moyennes mobiles simples 'SMA' (Simple Moving Average).
Le principe consiste pour le trader à prendre une position longue sur une action ou sur un instrument financier en général lorsque la moyenne SMA à court terme est supérieure à celle à long terme. 
Le trader prend un position courte dans le cas inverse. 

Ce concept peut être montré graphiquement au moyen de la librairire pandas et de l'objet DataFrame. 
Ces SMA sont calculées qu'à partir du moment ou nous avons assez de données en tenant compte du paramètre "window". 
Nous verrons que l'affichage de la SMA ne débute que lorsque nous avons suffisamment données. 
'''

# Moyennes mobiles simples (SMA) 
# Calcule de la moyenne à court terme (SMA1) 
data['SMA1'] = data[sym].rolling(window=42).mean() 
# Calcule de la moyenne à long terme (SMA2)
data['SMA2'] = data[sym].rolling(window=252).mean()

# Affichage des 5 dernières lignes de la DataFrame Apple avec les SMA
print("\n=== data[[sym, 'SMA1', 'SMA2']].tail() ===")
print(data[[sym, 'SMA1', 'SMA2']].tail())

# --- In [40] / Figure 8-6 : Prix + 2 SMA ---
data[[sym, 'SMA1', 'SMA2']].plot(figsize=(10, 6))
plt.title('Prix de l\'action Apple et deux moyennes mobiles simples (SMA)')
plt.tight_layout()
plt.savefig('./Module 2 - Series temporelles financières/Figures_series_temporelles_financieres/fig_Apple_&_SMA.png', dpi=150, bbox_inches='tight')
plt.show()

'''
Les SMA servent surtout à trouver des positions à adopter sur les marchés financiers.
Dans l'exemple suivant nous allons faire correspondre une position longue à la valeur 1 et une position courte à la valeur -1.
Le passage d'une position à l'autre correspond à un croisement des deux lignes des séries temporelles SMA. 
'''

# Affichage graphique du prix de l'action Apple et des deux moyennes mobiles simples (SMA1 et SMA2)
# Nous ne conserverons que les lignes de données complètes
data.dropna(inplace=True)

# Calcul des positions à adopter en fonction du croisement des deux SMA
# Si SMA court > SMA long → position longue (1), sinon → short (-1)
data['positions'] = np.where(data['SMA1'] > data['SMA2'], 1, -1)
ax = data[[sym, 'SMA1', 'SMA2', 'positions']].plot(figsize=(10, 6), secondary_y='positions')
# .set_bbox_to_anchor() permet de positionner la légende à un endroit précis du tracé
ax.get_legend().set_bbox_to_anchor((0.25, 0.85))
plt.title('Prix de l\'action Apple, deux SMA et positions longues/courtes')
plt.tight_layout()
plt.savefig('./Module 2 - Series temporelles financières/Figures_series_temporelles_financieres/fig_Apple_&_SMA_positions.png', dpi=150, bbox_inches='tight')
plt.show()