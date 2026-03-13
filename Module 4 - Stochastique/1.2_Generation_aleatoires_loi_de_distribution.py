tableau_12_2 = [
    {"fonction": "beta",                "parametres": "a, b[, size]",                  "resultat": "Distribution bêta sur [0, 1]"},
    {"fonction": "binomial",            "parametres": "n, p[, size]",                  "resultat": "Distribution binomiale"},
    {"fonction": "chisquare",           "parametres": "df[, size]",                    "resultat": "Distribution khi carré"},
    {"fonction": "dirichlet",           "parametres": "alpha[, size]",                 "resultat": "Distribution de Dirichlet"},
    {"fonction": "exponential",         "parametres": "[scale, size]",                 "resultat": "Distribution exponentielle"},
    {"fonction": "f",                   "parametres": "dfnum, dfden[, size]",          "resultat": "Distribution F"},
    {"fonction": "gamma",               "parametres": "shape[, scale, size]",          "resultat": "Distribution gamma"},
    {"fonction": "geometric",           "parametres": "p[, size]",                     "resultat": "Distribution géométrique"},
    {"fonction": "gumbel",              "parametres": "[loc, scale, size]",            "resultat": "Distribution de Gumbel"},
    {"fonction": "hypergeometric",      "parametres": "ngood, nbad, nsample[, size]",  "resultat": "Distribution hypergéométrique"},
    {"fonction": "laplace",             "parametres": "[loc, scale, size]",            "resultat": "Distribution de Laplace ou double exponentielle"},
    {"fonction": "logistic",            "parametres": "[loc, scale, size]",            "resultat": "Distribution logistique"},
    {"fonction": "lognormal",           "parametres": "[mean, sigma, size]",           "resultat": "Distribution log-normale"},
    {"fonction": "logseries",           "parametres": "p[, size]",                     "resultat": "Distribution de séries logarithmiques"},
    {"fonction": "multinomial",         "parametres": "n, pvals[, size]",              "resultat": "Distribution multinomiale"},
    {"fonction": "multivariate_normal", "parametres": "mean, cov[, size]",             "resultat": "Distribution multivariée normale"},
    {"fonction": "negative_binomial",   "parametres": "n, p[, size]",                  "resultat": "Distribution binomiale négative"},
    {"fonction": "noncentral_chisquare","parametres": "df, nonc[, size]",              "resultat": "Distribution khi carré non centrale"},
    {"fonction": "noncentral_f",        "parametres": "dfnum, dfden, nonc[, size]",    "resultat": "Distribution-F non centrale"},
    {"fonction": "normal",              "parametres": "[loc, scale, size]",            "resultat": "Distribution normale (gaussienne)"},
    {"fonction": "pareto",              "parametres": "a[, size]",                     "resultat": "Distribution de Pareto II ou Lomax dans la forme spécifiée"},
    {"fonction": "poisson",             "parametres": "[lam, size]",                   "resultat": "Distribution de Poisson"},
    {"fonction": "power",               "parametres": "a[, size]",                     "resultat": "Distribution de puissance dans l'intervalle [0, 1] avec exposant positif a - 1"},
    {"fonction": "rayleigh",            "parametres": "[scale, size]",                 "resultat": "Distribution de Rayleigh"},
    {"fonction": "standard_cauchy",     "parametres": "[size]",                        "resultat": "Distribution de Cauchy standard avec mode = 0"},
    {"fonction": "standard_exponential","parametres": "[size]",                        "resultat": "Distribution standard exponentielle"},
    {"fonction": "standard_gamma",      "parametres": "shape[, size]",                 "resultat": "Distribution standard gamma"},
    {"fonction": "standard_normal",     "parametres": "[size]",                        "resultat": "Distribution standard normale (mean=0, stdev=1)"},
    {"fonction": "standard_t",          "parametres": "df[, size]",                    "resultat": "Distribution t-Student avec df degrés de liberté"},
    {"fonction": "triangular",          "parametres": "left, mode, right[, size]",     "resultat": "Distribution triangulaire sur l'intervalle [left, right]"},
    {"fonction": "uniform",             "parametres": "[low, high, size]",             "resultat": "Distribution uniforme"},
    {"fonction": "vonmises",            "parametres": "mu, kappa[, size]",             "resultat": "Distribution de von Mises"},
    {"fonction": "wald",                "parametres": "mean, scale[, size]",           "resultat": "Distribution de Wald ou gaussienne inverse"},
    {"fonction": "weibull",             "parametres": "a[, size]",                     "resultat": "Distribution de Weibull"},
    {"fonction": "zipf",                "parametres": "a[, size]",                     "resultat": "Distribution de Zipf"},
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
    afficher_tableau("Tableau 12.2 : Fonctions de générations aléatoires selon la loi de distribution", tableau_12_2)