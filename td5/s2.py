def mediane_quartiles_avec_effectifs2(values):
    expanded_values = []
    for valeur, effectif in values:
        expanded_values.extend([valeur] * effectif)

    if not expanded_values:
        raise ValueError("La série développée est vide.")

    expanded_values.sort()
    n = len(expanded_values)

    q1_pos = (n + 1) / 4
    median_pos = (n + 1) / 2
    q3_pos = 3 * (n + 1) / 4

    def get_value_at_position(pos, sorted_values):
        if pos <= 1:
            return float(sorted_values[0])
        if pos >= len(sorted_values):
            return float(sorted_values[-1])

        lower_idx = int(pos) - 1
        upper_idx = lower_idx + 1
        fraction = pos - (lower_idx + 1)

        if upper_idx >= len(sorted_values):
            return float(sorted_values[-1])

        lower_val = sorted_values[lower_idx]
        upper_val = sorted_values[upper_idx]
        return float(lower_val + fraction * (upper_val - lower_val))

    q1 = get_value_at_position(q1_pos, expanded_values)
    median = get_value_at_position(median_pos, expanded_values)
    q3 = get_value_at_position(q3_pos, expanded_values)

    return [q1, median, q3]


def mediane_quartiles_avec_classes(classes, values):
    if len(classes) != len(values):
        raise ValueError("classes et values doivent avoir la même longueur.")

    total_freq = sum(values)
    if total_freq <= 0:
        raise ValueError(
            "La somme des effectifs doit être strictement positive.")

    cumulative = []
    running = 0
    for value in values:
        running += value
        cumulative.append(running)

    def quartile_interpole(position):
        index = 0
        while index < len(cumulative) and cumulative[index] < position:
            index += 1
        if index >= len(classes):
            index = len(classes) - 1

        borne_inf, borne_sup = classes[index]
        largeur = borne_sup - borne_inf
        fi = values[index]
        f_prev = 0 if index == 0 else cumulative[index - 1]

        if fi == 0:
            return float(borne_inf)

        return float(borne_inf + ((position - f_prev) / fi) * largeur)

    q1 = quartile_interpole((total_freq + 1) / 4)
    median = quartile_interpole((total_freq + 1) / 2)
    q3 = quartile_interpole(3 * (total_freq + 1) / 4)

    return [q1, median, q3]
