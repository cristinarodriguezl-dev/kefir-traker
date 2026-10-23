import json
from pathlib import Path
from src.models import Fermentation, GoodFermentation, DamagedFermentation, InsufficientFermentation, OverfermentedFermentation

HISTORY_FILE = Path(__file__).parent.parent / "data" / "history.json"

def load_history():
    if not HISTORY_FILE.exists():
        return []

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    fermentation_classes = {
        "Buena": GoodFermentation,
        "Dañado": DamagedFermentation,
        "Insuficiente": InsufficientFermentation,
        "Sobrefermentada": OverfermentedFermentation
    }

    history = []

    for fermentation in data:
        fermentation_class = fermentation_classes.get(
            fermentation["result"],
            Fermentation
        )

        history.append(
            fermentation_class(
                fermentation["grains_weight"],
                fermentation["milk_ml"],
                fermentation["duration_hours"]
            )
            if fermentation_class != Fermentation
            else Fermentation(
                fermentation["grains_weight"],
                fermentation["milk_ml"],
                fermentation["duration_hours"],
                fermentation["result"]
            )
        )

    return history

def save_fermentation(fermentation):
    history = load_history()
    history.append(fermentation)

    HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(
            [fermentation.__dict__ for fermentation in history],
            file,
            ensure_ascii=False,
            indent=4
        )

def delete_fermentation(index):
    history = load_history()

    if 0 <= index < len(history):
        history.pop(index)

        with open(HISTORY_FILE, "w", encoding="utf-8") as file:
            json.dump(
                [fermentation.__dict__ for fermentation in history],
                file,
                ensure_ascii=False,
                indent=4
            )