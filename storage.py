import json
from pathlib import Path

HISTORY_FILE = Path(__file__).parent / "data" / "history.json"

#Cargar el historial
def load_history():
    if not HISTORY_FILE.exists():
        return[]
    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

#Guardar la fermentación
def save_fermentation(fermentation):
    history = load_history()
    history.append(fermentation)

    HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=4)

#Eliminar fermentaciones
def delete_fermentation(index):
    history = load_history()
    if 0 <= index < len(history):
        history.pop(index)
        with open(HISTORY_FILE, "w", encoding="utf-8") as file:
            json.dump(history, file, ensure_ascii=False, indent=4)
    