"""
module_2 - Series temporelles financières
4_Donnees_a_haute_frequence : 

Ce module est dédié aux analyses de séries temporelles avec pandas. 
Les jeux de données en continu par tick ne constituent qu'un cas particulier de série temporelle. 
Elles peuvent être gérées à peu près de la même manière que les données de clôture EOD que nous venons de voir dans les derniers modules de série temporelle.

En général, l'importation de tels jeux de données est assez rapide avec pandas.
Problème que nous rencontrons : 
Les données Bid/Ask sont souvent fournies dans des fichiers séparés (CSV et autres), dans tous nos modules nous n'utilisons que la bibliothèque Yfinance pour télécharger les données, 
ce qui nous oblige à simuler les données Bid/Ask à partir des données de clôture (Close) fournies par Yfinance.
Nous verrons dans d'autres modules comment travailler avec des données de tick plus réalistes, notamment en utilisant des bibliothèques spécialisées comme FXCM, Interactive Brokers, 
qui peuvent gérer des données de tick plus complexes et fournir des fonctionnalités avancées pour l'analyse et le backtesting.
"""


import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import yfinance as yf


plt.style.use('seaborn-v0_8')
mpl.rcParams['font.family'] = 'serif'



print("=== Téléchargement données intraday EUR/USD ===")
print("yfinance : intervalle 1 minute, derniers jours disponibles\n")
tick_raw = yf.download('EURUSD=X', period='1d', interval='1m', auto_adjust=True)

# Simulation Bid/Ask à partir des données OHLC
# Le spread EUR/USD est typiquement ~ 0.00010 (1 pip) → demi-spread = 0.00005
half_spread = 0.00005
close = tick_raw['Close'].squeeze()  # Assure une Series 1D (compatibilité yfinance récent)
tick = pd.DataFrame({
    'Bid': close - half_spread,
    'Ask': close + half_spread,
}, index=tick_raw.index)
tick.index.name = 'Date'

# Aperçu des tick 
print("=== tick.info() ===")
tick.info()
print()

# Calcule des prix Mid pour chaque ligne (moyenne entre Bid et Ask)
tick['Mid'] = tick.mean(axis=1)  

# Affichage graphique des données de tick pour le taux de change EUR/USD
tick['Mid'].plot(figsize=(10, 6))
plt.title('Données de tick pour le taux de change EUR/USD')
plt.ylabel('Mid Price')
plt.tight_layout()
plt.savefig('./Module 2 - Series temporelles financières/Figures_series_temporelles_financieres/fig_tick_mid_EURUSD.png', dpi=150, bbox_inches='tight')
plt.show()




'''
Lorsqu'on travaille avec des données de cote ou de tick, il est nécessaire de réaliser un rééchantillonnage. 
C'est ce que nous faisons dans l'exemple suivant en simplifiant les donénes pour les aligner sur une période de cinq minutes. 
Les données peuvent ensuite être utilisées, par exemple, pour lancer un rétroset de stratégie de trading algorithmique ou pour effectuer une analyse technique.
'''

# Rééchantillonnage des données de tick à une fréquence de 5 minutes en prenant le dernier prix de chaque intervalle de 5 minutes
tick_resam = tick.resample(rule='5min', label='right').last()

# Aperçu des données rééchantillonnées
print("=== tick_resam.head() ===")
print(tick_resam.head())

# Affichage graphique des données rééchantillonnées pour le taux de change EUR/USD
tick_resam['Mid'].plot(figsize=(10, 6))
plt.title('Données rééchantillonnées toutes les 5 minutes pour le taux de change EUR/USD')
plt.ylabel('Mid Price')
plt.tight_layout()
plt.savefig('./Module 2 - Series temporelles financières/Figures_series_temporelles_financieres/fig_tick_resam_5min_EURUSD.png', dpi=150, bbox_inches='tight')
plt.show()


