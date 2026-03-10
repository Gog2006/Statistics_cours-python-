import matplotlib.pyplot as plt
import os
import tempfile
from pathlib import Path

os.environ["MPLCONFIGDIR"] = str(Path(tempfile.gettempdir()) / "matplotlib")


def battongrosse(valeurs):
    plt.figure()
    plt.hist(valeurs)

    if plt.get_backend().lower().endswith("agg"):
        output_file = Path(__file__).with_name("battonfinne.png")
        plt.savefig(output_file, dpi=150,   bbox_inches="tight")
        print(f"Plot saved to: {output_file}")
    else:
        plt.show()


def battonfinne(valeurs, effectifs):
    plt.figure()
    plt.bar(valeurs, effectifs)

    if plt.get_backend().lower().endswith("agg"):
        output_file = Path(__file__).with_name("battongrosse.png")
        plt.savefig(output_file, dpi=150, bbox_inches="tight")
        print(f"Plot saved to: {output_file}")
    else:
        plt.show()


def circul(listedesvaleurs, listedeffectif):
    plt.figure()
    plt.pie(listedeffectif, labels=listedesvaleurs, autopct="%1.1f%%")

    if plt.get_backend().lower().endswith("agg"):
        output_file = Path(__file__).with_name("circul.png")
        plt.savefig(output_file, dpi=150, bbox_inches="tight")
        print(f"Plot saved to: {output_file}")
    else:
        plt.show()


if __name__ == "__main__":
    listedesvaleurs = ["A", "B", "C"]
    listedeffectif = [160, 110, 330]
    battongrosse(listedesvaleurs)
    battonfinne(listedesvaleurs, listedeffectif)
    circul(listedesvaleurs, listedeffectif)
