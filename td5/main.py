from td5.s1 import moy_ponderee
from td5.s3 import arrondir_liste, ecarttype, exercice1, exercice2, exercice3, interquartile
from td5.s4 import exercice4, statresume
from td5.s5 import exercice5, statfiltre


if __name__ == "__main__":
    ls = [8, 11, 12, 13, 15, 17, 56, 78, 109]
    le = [[175, 1], [180, 1], [185, 2], [190, 2], [195, 4], [200, 5], [205, 5], [210, 4], [215, 3],
          [220, 1], [225, 1], [230, 1]]
    lclasses = [[0, 150], [150, 160], [160, 170], [170, 180], [180, 200]]
    lvalues = [0, 3, 11, 8, 3]

    print("Exemple - moyenne pondérée:", round(moy_ponderee(le), 2))

    print("Exercice 1:", exercice1())
    print("Exercice 2:", arrondir_liste(exercice2(), 2))
    print("Exercice 3:", arrondir_liste(exercice3(), 2))

    print("Exercice 4:", [(r[0], round(r[1], 2), round(r[2], 2))
          for r in exercice4()])

    ls_filtree, _ = statfiltre(ls)
    print("Exercice 5 - liste filtrée:", ls_filtree)
    print("Exercice 5 - statresume après filtrage:",
          (lambda r: (r[0], round(r[1], 2), round(r[2], 2)))(statresume(liste_simple=ls_filtree)))

    print("Contrôle direct ecarttype (méthode 1):", tuple(round(v, 2)
          for v in ecarttype(liste_simple=ls)))
    print("Contrôle direct interquartile (méthode 3):", tuple(round(v, 2)
          for v in interquartile(classes=lclasses, values=lvalues)))
    print("Exercice 5 (fonction dédiée):", exercice5())
