tableau_12_1 = [
    {"fonction": "rand",             "parametres": "d0, d1, ..., dn",       "resultat": "Valeurs aléatoires dans la forme spécifiée"},
    {"fonction": "randn",            "parametres": "d0, d1, ..., dn",       "resultat": "Un ou plusieurs échantillons en distribution normale standard"},
    {"fonction": "randint",          "parametres": "low[, high, size]",     "resultat": "Entiers aléatoires entre low (incluse) et high (exclue)"},
    {"fonction": "random_integers",  "parametres": "low[, high, size]",     "resultat": "Entiers aléatoires entre low (incluse) et high (incluse)"},
    {"fonction": "random_sample",    "parametres": "[size]",                "resultat": "Flottants aléatoires dans l'intervalle semi-ouvert [0.0, 1.0)"},
    {"fonction": "random",           "parametres": "[size]",                "resultat": "Flottants aléatoires dans l'intervalle semi-ouvert [0.0, 1.0)"},
    {"fonction": "ranf",             "parametres": "[size]",                "resultat": "Flottants aléatoires dans l'intervalle semi-ouvert [0.0, 1.0)"},
    {"fonction": "sample",           "parametres": "[size]",                "resultat": "Flottants aléatoires dans l'intervalle semi-ouvert [0.0, 1.0)"},
    {"fonction": "choice",           "parametres": "a[, size, replace, p]", "resultat": "Échantillon aléatoire tiré dans un tableau en 1D"},
    {"fonction": "bytes",            "parametres": "length",                "resultat": "Octets aléatoires"},
]

def afficher_tableau(titre, tableau):
    col_f = max(len(r["fonction"])   for r in tableau)
    col_p = max(len(r["parametres"]) for r in tableau)
    col_r = max(len(r["resultat"])   for r in tableau)

    sep = f"+{'-'*(col_f+2)}+{'-'*(col_p+2)}+{'-'*(col_r+2)}+"
    header = f"| {'Fonction':<{col_f}} | {'Paramètres':<{col_p}} | {'Échantillons renvoyés/Résultat':<{col_r}} |"

    print(f"\n{titre}")
    print(sep)
    print(header)
    print(sep)
    for row in tableau:
        print(f"| {row['fonction']:<{col_f}} | {row['parametres']:<{col_p}} | {row['resultat']:<{col_r}} |")
    print(sep)


if __name__ == "__main__":
    afficher_tableau("Tableau 12.1 : Fonctions du générateur aléatoire simple", tableau_12_1)