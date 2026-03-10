try:
    from td6.s3 import ecarttype
    from td6.s4 import statresume
except ModuleNotFoundError:
    from s3 import ecarttype
    from s4 import statresume


def statfiltre(liste_simple, liste_a_modifier=None):
    donnees = list(liste_simple)
    donnees_modifiees = None if liste_a_modifier is None else list(
        liste_a_modifier)

    if donnees_modifiees is not None and len(donnees_modifiees) != len(donnees):
        raise ValueError(
            "liste_a_modifier doit avoir la meme longueur que liste_simple.")

    while len(donnees) >= 3:
        a_valeurs_aberrantes, _, _ = statresume(liste_simple=donnees)
        if not a_valeurs_aberrantes:
            break

        ecart_type, moyenne = ecarttype(liste_simple=donnees)
        borne_inf = moyenne - 0.7 * ecart_type
        borne_sup = moyenne + 0.7 * ecart_type

        indices_gardes = [
            i for i, valeur in enumerate(donnees)
            if borne_inf <= valeur <= borne_sup
        ]

        if len(indices_gardes) == len(donnees):
            break

        donnees = [donnees[i] for i in indices_gardes]
        if donnees_modifiees is not None:
            donnees_modifiees = [donnees_modifiees[i] for i in indices_gardes]

    return donnees, donnees_modifiees
