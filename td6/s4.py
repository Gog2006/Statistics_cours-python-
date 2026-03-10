import matplotlib.pyplot as plt
import csv
import importlib
import os
import tempfile
from collections import Counter
from pathlib import Path

os.environ["MPLCONFIGDIR"] = str(Path(tempfile.gettempdir()) / "matplotlib")


try:
    from td6.s3 import ecarttype, interquartile
except ModuleNotFoundError:
    from s3 import ecarttype, interquartile


try:
    import numpy as np
except ModuleNotFoundError:
    np = None


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


def _find_csv_path(csv_path=None):
    if csv_path is not None:
        candidate = Path(csv_path)
    else:
        candidate = Path(__file__).with_name("mindfactory_updated.csv")

    if candidate.exists():
        return candidate

    raise FileNotFoundError(
        f"mindfactory_updated.csv introuvable: {candidate}"
    )


def _show_or_save(fig, output_name):
    if plt.get_backend().lower().endswith("agg"):
        output_file = Path(__file__).with_name(output_name)
        fig.savefig(output_file, dpi=150, bbox_inches="tight")
        print(f"Plot saved to: {output_file}")
        plt.close(fig)
    else:
        plt.show()


def listefilteranddisplay(listebrute, seuil, titre):
    compteur = Counter(listebrute)
    liste1 = list(compteur.keys())
    liste2 = list(compteur.values())

    liste1simple = []
    liste2simple = []
    for valeur, effectif in zip(liste1, liste2):
        if effectif > seuil:
            liste1simple.append(valeur)
            liste2simple.append(effectif)

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle(f"Analyse: {titre}")

    axes[0, 0].hist(listebrute)
    axes[0, 0].set_title("Histogramme listebrute")

    axes[0, 1].bar([str(v) for v in liste1simple], liste2simple)
    axes[0, 1].set_title(f"Diagramme en batons (>{seuil})")
    axes[0, 1].tick_params(axis="x", labelrotation=45)

    axes[1, 0].pie(liste2, labels=[str(v) for v in liste1], autopct="%1.1f%%")
    axes[1, 0].set_title("Diagramme circulaire complet")

    if liste2simple:
        axes[1, 1].pie(
            liste2simple,
            labels=[str(v) for v in liste1simple],
            autopct="%1.1f%%",
        )
        axes[1, 1].set_title("Diagramme circulaire filtre")
    else:
        axes[1, 1].text(0.5, 0.5, "Aucune valeur > seuil",
                        ha="center", va="center")
        axes[1, 1].set_title("Diagramme circulaire filtre")

    plt.tight_layout()
    safe_title = titre.lower().replace(" ", "_")
    _show_or_save(fig, f"s4_listefilteranddisplay_{safe_title}.png")

    return liste1simple, liste2simple


def exercice1():
    csv_file = _find_csv_path()

    cpu_list = []
    gpu_list = []
    gpu_list_i = []
    ram_list = []

    with csv_file.open("r", encoding="utf-8", newline="") as fichier:
        reader = csv.DictReader(fichier)
        for row in reader:
            cpu = (row.get("cpu_processor") or "").strip()
            if cpu:
                cpu_list.append(cpu)

            gpu_extra = (row.get("gpu_extra") or "").strip()
            if gpu_extra:
                gpu_list.append(gpu_extra)
            else:
                gpu_list.append("Integrated GPU")

            gpu_integrated = (row.get("gpu_integrated") or "").strip()
            if gpu_integrated:
                gpu_list_i.append(gpu_integrated)

            ram = (row.get("ram_memory") or "").strip()
            try:
                ram_value = float(ram)
            except ValueError:
                continue
            if ram_value <= 128.0:
                ram_list.append(ram_value)

    cpu_l1, cpu_l2 = listefilteranddisplay(cpu_list, 20, "CPU")
    gpu_l1, gpu_l2 = listefilteranddisplay(gpu_list, 10, "GPU")
    gpui_l1, gpui_l2 = listefilteranddisplay(gpu_list_i, 10, "Integrated GPU")
    ram_l1, ram_l2 = listefilteranddisplay(ram_list, 4, "RAM")

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle("Synthese finale exercice1")

    axes[0, 0].pie(cpu_l2, labels=[str(v) for v in cpu_l1], autopct="%1.1f%%")
    axes[0, 0].set_title("CPU")

    axes[0, 1].pie(gpu_l2, labels=[str(v) for v in gpu_l1], autopct="%1.1f%%")
    axes[0, 1].set_title("GPU (extra, vide -> Integrated GPU)")

    axes[1, 0].pie(gpui_l2, labels=[str(v)
                   for v in gpui_l1], autopct="%1.1f%%")
    axes[1, 0].set_title("GPU integre")

    axes[1, 1].pie(ram_l2, labels=[str(v) for v in ram_l1], autopct="%1.1f%%")
    axes[1, 1].set_title("RAM")

    plt.tight_layout()
    _show_or_save(fig, "s4_exercice1_synthese.png")

    return {
        "cpu": (cpu_l1, cpu_l2),
        "gpu": (gpu_l1, gpu_l2),
        "gpu_i": (gpui_l1, gpui_l2),
        "ram": (ram_l1, ram_l2),
    }


def prepare_data_mindfactory():
    try:
        from td6.s5 import statfiltre
    except ModuleNotFoundError:
        from s5 import statfiltre

    csv_file = _find_csv_path()
    x = []
    y = []

    with csv_file.open("r", encoding="utf-8", newline="") as fichier:
        reader = csv.DictReader(fichier)
        for row in reader:
            display_cm = (row.get("display_cm") or "").strip()
            price = (row.get("price_eur") or "").strip()
            try:
                display_value = float(display_cm)
                price_value = float(price)
            except ValueError:
                continue
            x.append(display_value)
            y.append(price_value)

    xpf, ypf = statfiltre(x, y)
    return x, y, xpf, ypf


def _compute_linregress(x, y):
    try:
        stats = importlib.import_module("scipy.stats")
        res = stats.linregress(x, y)
        return float(res.slope), float(res.intercept)
    except ModuleNotFoundError:
        pass

    if np is None:
        raise ModuleNotFoundError(
            "scipy ou numpy est requis pour la regression.")

    slope, intercept = np.polyfit(np.array(x), np.array(y), 1)
    return float(slope), float(intercept)


def exercice2():
    x, y, xpf, ypf = prepare_data_mindfactory()

    slope1, intercept1 = _compute_linregress(x, y)
    slope2, intercept2 = _compute_linregress(xpf, ypf)

    x_sorted = sorted(x)
    y_reg_1 = [slope1 * xi + intercept1 for xi in x_sorted]

    xpf_sorted = sorted(xpf)
    y_reg_2 = [slope2 * xi + intercept2 for xi in xpf_sorted]

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    axes[0].scatter(x, y, s=12, alpha=0.6, label="Donnees brutes")
    axes[0].plot(x_sorted, y_reg_1, color="red", label="Regression")
    axes[0].set_title("Prix en fonction de display_cm (brut)")
    axes[0].set_xlabel("display_cm")
    axes[0].set_ylabel("price_eur")
    axes[0].legend()

    axes[1].scatter(xpf, ypf, s=12, alpha=0.6, label="Donnees filtrees")
    axes[1].plot(xpf_sorted, y_reg_2, color="green", label="Regression")
    axes[1].set_title("Prix en fonction de display_cm (filtre)")
    axes[1].set_xlabel("display_cm")
    axes[1].set_ylabel("price_eur")
    axes[1].legend()

    plt.tight_layout()
    _show_or_save(fig, "s4_exercice2_regression.png")

    prediction_70_brut = slope1 * 70 + intercept1
    prediction_70_filtre = slope2 * 70 + intercept2

    return {
        "modele_brut": {
            "slope": slope1,
            "intercept": intercept1,
            "prediction_70": prediction_70_brut,
        },
        "modele_filtre": {
            "slope": slope2,
            "intercept": intercept2,
            "prediction_70": prediction_70_filtre,
        },
    }


def _plot_clusters(ax, x, y, model, title):
    colors = ["b", "g", "r", "c", "m", "y", "k"]
    for point in zip(x, y):
        cluster_id = int(model.predict([point])[0])
        ax.scatter(point[0], point[1],
                   c=colors[cluster_id % len(colors)], s=14)

    centers = model.cluster_centers_
    ax.scatter(centers[:, 0], centers[:, 1], c="black",
               marker="x", s=80, label="Centres")
    ax.set_title(title)
    ax.set_xlabel("display_cm")
    ax.set_ylabel("price_eur")
    ax.legend()


def exercice3():
    try:
        KMeans = importlib.import_module("sklearn.cluster").KMeans
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            "sklearn est requis pour l'exercice 3.") from exc

    x, y, xpf, ypf = prepare_data_mindfactory()

    if np is not None:
        data1 = np.column_stack((x, y))
        data2 = np.column_stack((xpf, ypf))
    else:
        data1 = list(zip(x, y))
        data2 = list(zip(xpf, ypf))

    model1 = KMeans(n_clusters=3, random_state=42, n_init=10).fit(data1)
    model2 = KMeans(n_clusters=2, random_state=42, n_init=10).fit(data2)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    _plot_clusters(axes[0], x, y, model1, "Clusters KMeans (x,y) - 3 groupes")
    _plot_clusters(axes[1], xpf, ypf, model2,
                   "Clusters KMeans (xpf,ypf) - 2 groupes")
    plt.tight_layout()
    _show_or_save(fig, "s4_exercice3_kmeans.png")

    return {
        "centres_modele1": model1.cluster_centers_.tolist(),
        "centres_modele2": model2.cluster_centers_.tolist(),
    }


if __name__ == "__main__":
    print("Exercice 1")
    print(exercice1())
    print("Exercice 2")
    print(exercice2())
    print("Exercice 3")
    try:
        print(exercice3())
    except ModuleNotFoundError:
        print("Exercice 3 saute: sklearn non installe")
