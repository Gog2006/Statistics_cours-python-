import math

try:
    import numpy as np
except ModuleNotFoundError:
    np = None

from td5.s1 import moy_ponderee
from td5.s2 import mediane_quartiles_avec_classes, mediane_quartiles_avec_effectifs2


def _mean(values):
    if np is not None:
        return float(np.mean(values))
    return float(sum(values) / len(values))


def _sqrt(value):
    if np is not None:
        return float(np.sqrt(value))
    return float(math.sqrt(value))


def _quantiles_weibull(values):
    if np is not None:
        q1, mediane, q3 = np.quantile(
            values, [0.25, 0.5, 0.75], method="weibull")
        return float(q1), float(mediane), float(q3)

    sorted_values = sorted(values)
    n = len(sorted_values)

    def get_value_at_position(pos):
        if pos <= 1:
            return float(sorted_values[0])
        if pos >= n:
            return float(sorted_values[-1])

        lower_idx = int(pos) - 1
        upper_idx = lower_idx + 1
        fraction = pos - (lower_idx + 1)
        lower_val = sorted_values[lower_idx]
        upper_val = sorted_values[upper_idx]
        return float(lower_val + fraction * (upper_val - lower_val))

    q1 = get_value_at_position((n + 1) / 4)
    mediane = get_value_at_position((n + 1) / 2)
    q3 = get_value_at_position(3 * (n + 1) / 4)
    return q1, mediane, q3


def etendue(donnees, effectifs=None):
    if effectifs is None:
        if donnees and isinstance(donnees[0], (list, tuple)) and len(donnees[0]) == 2:
            modalites_non_vides = [
                modalite for modalite, eff in donnees if eff > 0]
            return max(modalites_non_vides) - min(modalites_non_vides)
        return max(donnees) - min(donnees)

    intervalles_non_vides = [intervalle for intervalle,
                             eff in zip(donnees, effectifs) if eff > 0]
    borne_inf_min = intervalles_non_vides[0][0]
    borne_sup_max = intervalles_non_vides[-1][1]
    return borne_sup_max - borne_inf_min


def moy_classes(classes, values):
    if len(classes) != len(values):
        raise ValueError("classes et values doivent avoir la même longueur.")

    total_effectifs = sum(values)
    if total_effectifs <= 0:
        raise ValueError(
            "La somme des effectifs doit être strictement positive.")

    milieux = [((borne_inf + borne_sup) / 2)
               for borne_inf, borne_sup in classes]
    somme_ponderee = sum(mi * fi for mi, fi in zip(milieux, values))
    return somme_ponderee / total_effectifs


def ecarttype(liste_simple=None, liste_avec_effectifs=None, classes=None, values=None):
    if liste_simple is not None:
        moyenne = _mean(liste_simple)
        variance = _mean([(x - moyenne) ** 2 for x in liste_simple])
        return _sqrt(variance), moyenne

    if liste_avec_effectifs is not None:
        moyenne = float(moy_ponderee(liste_avec_effectifs))
        total_effectifs = sum(effectif for _, effectif in liste_avec_effectifs)
        if total_effectifs <= 0:
            raise ValueError(
                "La somme des effectifs doit être strictement positive.")
        variance = sum(effectif * (valeur - moyenne) ** 2 for valeur,
                       effectif in liste_avec_effectifs) / total_effectifs
        return _sqrt(variance), moyenne

    if classes is not None and values is not None:
        moyenne = float(moy_classes(classes, values))
        total_effectifs = sum(values)
        if total_effectifs <= 0:
            raise ValueError(
                "La somme des effectifs doit être strictement positive.")
        milieux = [((borne_inf + borne_sup) / 2)
                   for borne_inf, borne_sup in classes]
        variance = sum(fi * (mi - moyenne) ** 2 for mi,
                       fi in zip(milieux, values)) / total_effectifs
        return _sqrt(variance), moyenne

    raise ValueError(
        "Fournir soit liste_simple, soit liste_avec_effectifs, soit classes et values.")


def interquartile(liste_simple=None, liste_avec_effectifs=None, classes=None, values=None):
    if liste_simple is not None:
        q1, mediane, q3 = _quantiles_weibull(liste_simple)
        return float(q3 - q1), float(mediane)

    if liste_avec_effectifs is not None:
        q1, mediane, q3 = mediane_quartiles_avec_effectifs2(
            liste_avec_effectifs)
        return float(q3 - q1), float(mediane)

    if classes is not None and values is not None:
        q1, mediane, q3 = mediane_quartiles_avec_classes(classes, values)
        return float(q3 - q1), float(mediane)

    raise ValueError(
        "Fournir soit liste_simple, soit liste_avec_effectifs, soit classes et values.")


def exercice1():
    ls = [8, 11, 12, 13, 15, 17, 56, 78, 109]
    le = [[175, 1], [180, 1], [185, 2], [190, 2], [195, 4], [200, 5], [205, 5], [210, 4], [215, 3],
          [220, 1], [225, 1], [230, 1]]
    lclasses = [[0, 150], [150, 160], [160, 170], [170, 180], [180, 200]]
    lvalues = [0, 3, 11, 8, 3]

    return [etendue(ls), etendue(le), etendue(lclasses, lvalues)]


def exercice2():
    ls = [8, 11, 12, 13, 15, 17, 56, 78, 109]
    le = [[175, 1], [180, 1], [185, 2], [190, 2], [195, 4], [200, 5], [205, 5], [210, 4], [215, 3],
          [220, 1], [225, 1], [230, 1]]
    lclasses = [[0, 150], [150, 160], [160, 170], [170, 180], [180, 200]]
    lvalues = [0, 3, 11, 8, 3]

    e1, m1 = ecarttype(liste_simple=ls)
    e2, m2 = ecarttype(liste_avec_effectifs=le)
    e3, m3 = ecarttype(classes=lclasses, values=lvalues)
    return [e1, e2, e3, m1, m2, m3]


def exercice3():
    ls = [8, 11, 12, 13, 15, 17, 56, 78, 109]
    le = [[175, 1], [180, 1], [185, 2], [190, 2], [195, 4], [200, 5], [205, 5], [210, 4], [215, 3],
          [220, 1], [225, 1], [230, 1]]
    lclasses = [[0, 150], [150, 160], [160, 170], [170, 180], [180, 200]]
    lvalues = [0, 3, 11, 8, 3]

    iq1, med1 = interquartile(liste_simple=ls)
    iq2, med2 = interquartile(liste_avec_effectifs=le)
    iq3, med3 = interquartile(classes=lclasses, values=lvalues)
    return [iq1, iq2, iq3, med1, med2, med3]


def arrondir_liste(resultats, nb_decimales=2):
    return [round(valeur, nb_decimales) if isinstance(valeur, float) else valeur for valeur in resultats]


if __name__ == "__main__":
    print("**Exercice 1**")
    print(exercice1())
    print("**Exercice 2**")
    print(arrondir_liste(exercice2(), 2))
    print("**Exercice 3**")
    print(arrondir_liste(exercice3(), 2))
