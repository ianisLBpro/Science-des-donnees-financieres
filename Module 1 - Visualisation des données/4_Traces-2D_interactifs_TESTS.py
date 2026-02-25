#
#
# Tracés 2D interactifs avec Plotly
#
#
#


import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as plyo
from plotly.subplots import make_subplots


# ============================================================
# SECTION 1 : Basic Plots - Données pseudo-aléatoires
# ============================================================

# Génération des données
a = np.random.standard_normal((250, 5)).cumsum(axis=0)                  # Nombres pseudo-aléatoires

index = pd.date_range('2019-1-1',                                       # Date de début
                       freq='B',                                        # Fréquence "business daily"
                       periods=len(a))                                  # Nombre de périodes

df = pd.DataFrame(100 + 5 * a,                                          # Transformation linéaire
                  columns=list('abcde'),                                # En-têtes de colonnes
                  index=index)                                          # DatetimeIndex

print("=== df.head() ===")
print(df.head())
print()

# Tracé en ligne d'une série temporelle
fig1 = go.Figure()
for col in df.columns:
    fig1.add_trace(go.Scatter(x=df.index, y=df[col], mode='lines', name=col))
fig1.update_layout(title="Figure 7-22 : Line plot (toutes les colonnes)")
plyo.plot(fig1, filename='./Module 1 - Visualisation des données/Test_trace_2D_interactifs/ply_01.html', auto_open=True)

# Tracé en ligne avec personnalisations
fig2 = go.Figure()
fig2.add_trace(go.Scatter(
    x=df.index, y=df['a'], mode='markers',                             # Mode marqueurs
    name='a',
    marker=dict(symbol='circle', size=3.5, color='blue'),              # Symboles et couleur
))
fig2.add_trace(go.Scatter(
    x=df.index, y=df['b'], mode='lines+markers',                       # Mode lignes + marqueurs
    name='b',
    marker=dict(symbol='diamond', size=3.5, color='magenta'),          # Symboles et couleur
    line=dict(color='magenta'),
))
fig2.update_layout(
    title='A Time Series Plot',                                        # Titre
    xaxis_title='date',                                                # Label axe x
    yaxis_title='value',                                               # Label axe y
    template='plotly_white',                                           # Thème clair (≈ polar)
)
plyo.plot(fig2, filename='./Module 1 - Visualisation des données/Test_trace_2D_interactifs/ply_02.html', auto_open=True)

# Tracé d'histogrammes par colonne
fig3 = make_subplots(rows=len(df.columns), cols=1,
                     shared_xaxes=False,
                     subplot_titles=list(df.columns))
for i, col in enumerate(df.columns, start=1):
    fig3.add_trace(
        go.Histogram(x=df[col], nbinsx=15, name=col),                 # Histogramme par colonne
        row=i, col=1,
    )
fig3.update_layout(title="Figure 7-24 : Histograms per column",
                   height=250 * len(df.columns), showlegend=False)
plyo.plot(fig3, filename='./Module 1 - Visualisation des données/Test_trace_2D_interactifs/ply_03.html', auto_open=True)


# =================================================================
# SECTION 2 : Financial Plots - Données OHLC synthétiques (EUR/USD)
# =================================================================

# Ici, on génère des données OHLC synthétiques
print("=== Génération de données OHLC synthétiques (EUR/USD) ===")

np.random.seed(42)
dates = pd.date_range('2017-10-20', periods=60, freq='B')
close_prices = 1.16 + np.random.standard_normal(60).cumsum() * 0.005

quotes = pd.DataFrame({
    'AskOpen':  close_prices + np.random.uniform(-0.002, 0.002, 60),
    'AskHigh':  close_prices + np.abs(np.random.normal(0, 0.003, 60)),
    'AskLow':   close_prices - np.abs(np.random.normal(0, 0.003, 60)),
    'AskClose': close_prices,
}, index=dates)

print(quotes.tail())
print()

# Tracé OHLC (Open-High-Low-Close)
fig4 = go.Figure(data=go.Ohlc(
    x=quotes.index,
    open=quotes['AskOpen'],                                            # Prix d'ouverture
    high=quotes['AskHigh'],                                            # Prix haut
    low=quotes['AskLow'],                                              # Prix bas
    close=quotes['AskClose'],                                          # Prix de clôture
    name='EUR/USD',
))
fig4.update_layout(title='EUR/USD Exchange Rate', legend=dict(yanchor='top'))
plyo.plot(fig4, filename='./Module 1 - Visualisation des données/Test_trace_2D_interactifs/qf_01.html', auto_open=True)

# Tracé OHLC + Bandes de Bollinger
# Calcul des bandes de Bollinger
bb_period = 15                                                         # Périodes pour les bandes
bb_std = 2                                                             # Écarts-types pour la largeur
sma = quotes['AskClose'].rolling(window=bb_period).mean()
std = quotes['AskClose'].rolling(window=bb_period).std()
upper_band = sma + bb_std * std
lower_band = sma - bb_std * std

fig5 = go.Figure()
fig5.add_trace(go.Ohlc(
    x=quotes.index, open=quotes['AskOpen'], high=quotes['AskHigh'],
    low=quotes['AskLow'], close=quotes['AskClose'], name='EUR/USD',
))
fig5.add_trace(go.Scatter(
    x=quotes.index, y=upper_band, mode='lines',
    name=f'BB supérieure ({bb_period}, {bb_std}σ)',
    line=dict(color='rgba(31,119,180,0.5)', width=1),
))
fig5.add_trace(go.Scatter(
    x=quotes.index, y=sma, mode='lines',
    name=f'SMA({bb_period})',
    line=dict(color='rgba(31,119,180,0.8)', width=1, dash='dash'),
))
fig5.add_trace(go.Scatter(
    x=quotes.index, y=lower_band, mode='lines',
    name=f'BB inférieure ({bb_period}, {bb_std}σ)',
    line=dict(color='rgba(31,119,180,0.5)', width=1),
    fill='tonexty', fillcolor='rgba(31,119,180,0.1)',                   # Remplissage entre bandes
))
fig5.update_layout(title='EUR/USD + Bollinger Bands', legend=dict(yanchor='top'))
plyo.plot(fig5, filename='./Module 1 - Visualisation des données/Test_trace_2D_interactifs/qf_02.html', auto_open=True)

# Tracé OHLC + bandes de Bollinger + RSI
# Calcul du RSI
rsi_period = 14                                                         # Période RSI
delta = quotes['AskClose'].diff()
gain = delta.where(delta > 0, 0.0)
loss = (-delta).where(delta < 0, 0.0)
avg_gain = gain.rolling(window=rsi_period).mean()
avg_loss = loss.rolling(window=rsi_period).mean()
rs = avg_gain / avg_loss
rsi = 100 - (100 / (1 + rs))

fig6 = make_subplots(rows=2, cols=1, shared_xaxes=True,
                     vertical_spacing=0.03,
                     row_heights=[0.7, 0.3],
                     subplot_titles=['EUR/USD + Bollinger Bands', 'RSI'])

# Sous-graphique 1 : OHLC + Bollinger
fig6.add_trace(go.Ohlc(
    x=quotes.index, open=quotes['AskOpen'], high=quotes['AskHigh'],
    low=quotes['AskLow'], close=quotes['AskClose'], name='EUR/USD',
), row=1, col=1)
fig6.add_trace(go.Scatter(
    x=quotes.index, y=upper_band, mode='lines',
    name='BB sup.', line=dict(color='rgba(31,119,180,0.5)', width=1),
    showlegend=False,
), row=1, col=1)
fig6.add_trace(go.Scatter(
    x=quotes.index, y=sma, mode='lines',                                # SMA — même cohérence que fig5
    name=f'SMA({bb_period})',
    line=dict(color='rgba(31,119,180,0.8)', width=1, dash='dash'),
    showlegend=False,
), row=1, col=1)
fig6.add_trace(go.Scatter(
    x=quotes.index, y=lower_band, mode='lines',
    name='BB inf.', line=dict(color='rgba(31,119,180,0.5)', width=1),
    fill='tonexty', fillcolor='rgba(31,119,180,0.1)', showlegend=False, # Remplissage entre SMA et bande basse
), row=1, col=1)

# Sous-graphique 2 : RSI
fig6.add_trace(go.Scatter(
    x=quotes.index, y=rsi, mode='lines', name='RSI',
    line=dict(color='purple', width=1.5),
), row=2, col=1)
fig6.add_hline(y=70, line_dash='dash', line_color='red',
               annotation_text='Suracheté (70)', row=2, col=1)          # Seuil suracheté
fig6.add_hline(y=30, line_dash='dash', line_color='green',
               annotation_text='Survendu (30)', row=2, col=1)           # Seuil survendu
fig6.update_yaxes(range=[0, 100], row=2, col=1)

fig6.update_layout(height=700, title='EUR/USD + Bollinger Bands + RSI',
                   legend=dict(yanchor='top'))
plyo.plot(fig6, filename='./Module 1 - Visualisation des données/Test_trace_2D_interactifs/qf_03.html', auto_open=True)

