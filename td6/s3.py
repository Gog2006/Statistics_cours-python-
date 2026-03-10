import math


def ecarttype(liste_simple=None, liste_avec_effectifs=None, classes=None, values=None):
    if liste_simple is None:
        raise ValueError("liste_simple est requis pour cette version.")
    if len(liste_simple) == 0:
        raise ValueError("liste_simple ne peut pas etre vide.")

    moyenne = sum(liste_simple) / len(liste_simple)
    variance = sum((x - moyenne) ** 2 for x in liste_simple) / \
        len(liste_simple)
    return float(math.sqrt(variance)), float(moyenne)


def interquartile(liste_simple=None, liste_avec_effectifs=None, classes=None, values=None):
    if liste_simple is None:
        raise ValueError("liste_simple est requis pour cette version.")
    if len(liste_simple) == 0:
        raise ValueError("liste_simple ne peut pas etre vide.")

    data = sorted(float(x) for x in liste_simple)
    n = len(data)

    def quantile_weibull(p):
        pos = p * (n + 1)
        if pos <= 1:
            return data[0]
        if pos >= n:
            return data[-1]

        low = int(pos) - 1
        high = low + 1
        frac = pos - int(pos)
        return data[low] + frac * (data[high] - data[low])

    q1 = quantile_weibull(0.25)
    med = quantile_weibull(0.5)
    q3 = quantile_weibull(0.75)
    return float(q3 - q1), float(med)
