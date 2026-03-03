from td5.s3 import ecarttype, interquartile


def statresume(liste_simple=None, liste_avec_effectifs=None, classes=None, values=None):
    ecart_type, moyenne = ecarttype(
        liste_simple=liste_simple,
        liste_avec_effectifs=liste_avec_effectifs,
        classes=classes,
        values=values,
    )
    ecart_iq, mediane = interquartile(
        liste_simple=liste_simple,
        liste_avec_effectifs=liste_avec_effectifs,
        classes=classes,
        values=values,
    )

    if moyenne == 0:
        difference_relative = abs(moyenne - mediane)
    else:
        difference_relative = abs(moyenne - mediane) / abs(moyenne)

    a_valeurs_aberrantes = difference_relative > 0.05
    if a_valeurs_aberrantes:
        return True, mediane, ecart_iq
    return False, moyenne, ecart_type


def exercice4():
    ls = [8, 11, 12, 13, 15, 17, 56, 78, 109]
    le = [[175, 1], [180, 1], [185, 2], [190, 2], [195, 4], [200, 5], [205, 5], [210, 4], [215, 3],
          [220, 1], [225, 1], [230, 1]]
    lclasses = [[0, 150], [150, 160], [160, 170], [170, 180], [180, 200]]
    lvalues = [0, 3, 11, 8, 3]

    r1 = statresume(liste_simple=ls)
    r2 = statresume(liste_avec_effectifs=le)
    r3 = statresume(classes=lclasses, values=lvalues)
    return [r1, r2, r3]


if __name__ == "__main__":
    print("Exercice 4:", [(r[0], round(r[1], 2), round(r[2], 2))
          for r in exercice4()])
