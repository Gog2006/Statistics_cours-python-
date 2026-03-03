def moy_ponderee(values):
    total_effectif = sum(effectif for _, effectif in values)
    if total_effectif == 0:
        raise ValueError(
            "La somme des effectifs doit être strictement positive.")
    somme_ponderee = sum(valeur * effectif for valeur, effectif in values)
    return somme_ponderee / total_effectif
