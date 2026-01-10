#
#
# Test du tracé 2D interactifs avec Plotly
#
#
#

### Importation des bibliothèques nécessaires ###
import numpy as np                                                       # NumPy pour les calculs numériques
import pandas as pd                                                      # Pandas pour la manipulation des données
import plotly.graph_objects as go                                        # Graphiques avec Plotly
from plotly.offline import plot                                          # Plotly pour les tracés interactifs



### Création des données aléatoires et du DataFrame ###
a = np.random.standard_normal((250, 5)).cumsum(axis=0)                   # Données aléatoires cumulées 
index = pd.date_range('2019-1-1',                                        # Date de début
                      freq='B',                                          # Fréquence des jours ouvrés
                      periods=len(a))                                    # Index de dates
df = pd.DataFrame(100 + 5 * a,                                           # Création du DataFrame et calcul des données
                  columns=list('abcde'),                                 # Colonnes du DataFrame
                  index=index)                                           # Index du DataFrame
print(df.head())                                                         # Affiche les premières lignes du DataFrame


### Base 100 pour les séries temporelles ###
df100 = df.apply(lambda x: (x / x.iloc[0])*100)                          # Mise à l'échelle en base 100


### Calcul des rendements quotidiens ###
# On calcule les rendements logarithmiques pour une meilleure précision et pour éviter les problèmes liés aux rendements négatifs
# 2 manières de le faire :

# returns = df.pct_change().dropna()                                     # Calcul des rendements quotidiens en %
daily_returns = np.log(df/ df.shift(1)).dropna()                         # Calcul des rendements quotidiens log en %


### Création d'une figure type tracé en ligne d'une série temporelle avec Plotly ###
fig = go.Figure(layout=go.Layout(                                        # Layout personnalisé
    title='Tracé en ligne séries temporelles',                           # Titre du graphique
    xaxis_title='Date',                                                  # Titre de l'axe x
    yaxis_title='Valeur',                                                # Titre de l'axe y
    hovermode='x unified'                                                # Permet d'afficher les valeurs de toutes les courbes au survol
))
### Ajouter les courbes ###
for col in df.columns:                                                   # Boucle sur les colonnes du DataFrame
    fig.add_scatter(x=df.index, y=df[col], name=col)                     # Ajout des courbes au graphique
### Sauvegarder dans un fichier HTML ###
plot(fig, filename='ply_01.html', auto_open=True)                        # Sauvegarde et ouverture automatique


### Création d'une figure type histogramme avec Plotly ###
fig = go.Figure(layout=go.Layout(                                        # Layout personnalisé
    title='Histogramme des rendements quotidiens',                       # Titre du graphique
    xaxis_title='Rendement quotidien',                                   # Titre de l'axe x
    yaxis_title='Fréquence'                                              # Titre de l'axe y
))
# Ajouter les histogrammes #
for col in daily_returns.columns:                                        # Boucle sur les colonnes des rendements
    fig.add_histogram(x=daily_returns[col],                              # Données des rendements 
                      name=col,                                          # Nom de la colonne
                      nbinsx=50,                                         # Nombre de bines
                      opacity=0.75)                                      # Ajout des histogrammes au graphique
### Sauvegarder dans un fichier HTML ###
plot(fig, filename='ply_02.html', auto_open=True)                        # Sauvegarde et ouverture automatique


# Création d'une figure type boxplot avec Plotly ###
fig = go.Figure(layout=go.Layout(                                        # Layout personnalisé
    title='Box plot des rendements quotidiens',                          # Titre du graphique
    xaxis_title='Actifs',                                                # Titre de l'axe x
    yaxis_title='Rendement quotidien'                                    # Titre de l'axe y
))
# Ajouter les boîtes à moustaches #
for col in daily_returns.columns:                                        # Boucle sur les colonnes des rendements
    fig.add_box(y=daily_returns[col],                                    # Données des rendements
                name=col)                                                # Ajout des boîtes à moustaches au graphique
### Sauvegarder dans un fichier HTML ###
plot(fig, filename='ply_03.html', auto_open=True)                        # Sauvegarde et ouverture automatique


### Création d'une figure type candlestick avec Plotly ###
# Pour le candlestick, on crée un DataFrame avec des données d'ouverture, haut, bas et fermeture
df_ohlc = pd.DataFrame({                                                 # Création du DataFrame OHLC
    'open': df['a'],                                                     # Données d'ouverture
    'high': df['a'] + np.random.uniform(0, 2, size=len(df)),             # Données haut
    'low': df['a'] - np.random.uniform(0, 2, size=len(df)),              # Données bas
    'close': df['a'] + np.random.uniform(-1, 1, size=len(df))            # Données de fermeture
}, index=df.index)                                                       # Index du DataFrame
# Création de la figure candlestick #
fig = go.Figure(layout=go.Layout(                                        # Layout personnalisé
    title='Graphique en chandelier (candlestick) pour a',                       # Titre du graphique
    xaxis_title='Date',                                                  # Titre de l'axe x
    yaxis_title='Prix'                                                   # Titre de l'axe y
))
# Ajouter le candlestick #
fig.add_candlestick(x=df_ohlc.index,                                     # Dates
                    open=df_ohlc['open'],                                # Données d'ouverture
                    high=df_ohlc['high'],                                # Données haut
                    low=df_ohlc['low'],                                  # Données bas
                    close=df_ohlc['close'],                              # Données de fermeture
                    name='a')                                            # Ajout du candlestick au graphique
### Sauvegarder dans un fichier HTML ###
plot(fig, filename='ply_04.html', auto_open=True)                        # Sauvegarde et ouverture automatique














