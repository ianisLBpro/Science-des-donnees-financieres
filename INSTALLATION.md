# Guide d'installation de l'environnement virtuel

## Prérequis

- **Python 3.14** (ou version compatible) installé sur votre machine
  - Téléchargement : https://www.python.org/downloads/
  - Vérifier l'installation : `python --version`

---

## Installation pas à pas

### 1. Cloner le dépôt

```bash
git clone <url-du-depot>
cd Science-des-donnees-financieres
```

### 2. Créer l'environnement virtuel

#### Windows (PowerShell / CMD)
```powershell
python -m venv .venv
```

#### macOS / Linux
```bash
python3 -m venv .venv
```

### 3. Activer l'environnement virtuel

#### Windows — PowerShell
```powershell
.\.venv\Scripts\Activate.ps1
```

> **Note :** Si vous obtenez une erreur liée à la politique d'exécution, exécutez d'abord :
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

#### Windows — CMD
```cmd
.\.venv\Scripts\activate.bat
```

#### macOS / Linux
```bash
source .venv/bin/activate
```

Une fois activé, votre invite de commande affichera le préfixe `(.venv)`.

### 4. Mettre à jour pip (recommandé)

```bash
python -m pip install --upgrade pip
```

### 5. Installer les dépendances

```bash
pip install -r requirements.txt
```

Cela installera tous les packages nécessaires avec les versions exactes :

| Package principal | Description |
|---|---|
| `numpy` | Calcul numérique |
| `pandas` | Manipulation de données |
| `matplotlib` | Graphiques 2D/3D statiques |
| `seaborn` | Graphiques statistiques |
| `plotly` | Graphiques interactifs |
| `cufflinks` | Lien Pandas ↔ Plotly |
| `scipy` | Calcul scientifique |
| `yfinance` | Données financières Yahoo Finance |
| `requests` | Requêtes HTTP |
| `beautifulsoup4` | Web scraping |
| `ipykernel` | Noyau Jupyter pour notebooks |
| `ipywidgets` | Widgets interactifs Jupyter |

### 6. Vérifier l'installation

```bash
python -c "import numpy, pandas, matplotlib, plotly, scipy, yfinance; print('Toutes les dépendances sont installées !')"
```

---

## Désactivation de l'environnement

```bash
deactivate
```

---

## Résolution de problèmes

| Problème | Solution |
|---|---|
| `python` non reconnu | Ajoutez Python au `PATH` système ou utilisez le chemin complet |
| Erreur de permission PowerShell | `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| Conflit de version Python | Utilisez `py -3.14` (Windows) ou `python3.14` (Linux/macOS) pour cibler la bonne version |
| Échec d'installation d'un package | Essayez `pip install --upgrade pip` puis relancez l'installation |
| Erreur de compilation (cffi, etc.) | Installez les outils de build : **Windows** → [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) / **Linux** → `sudo apt install build-essential python3-dev` |
