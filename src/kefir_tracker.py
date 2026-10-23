from src.storage import load_history, save_fermentation, delete_fermentation
from src.calculations import milk_needed, calculate_average_ratio


class KefirTracker:
    def __init__(self):
        self.history = load_history()

    def register_fermentation(self, fermentation):
        save_fermentation(fermentation)
        self.history.append(fermentation)

    def remove_fermentation(self, index):
        if 0 <= index < len(self.history):
            delete_fermentation(index)
            self.history.pop(index)

    def get_history(self):
        return self.history

    def get_statistics(self):
        total = len(self.history)

        return {
            "total": total,
            "good": sum(1 for f in self.history if f.result == "Buena"),
            "overfermented": sum(1 for f in self.history if f.result == "Sobrefermentada"),
            "insufficient": sum(1 for f in self.history if f.result == "Insuficiente"),
            "damaged": sum(1 for f in self.history if f.result == "Dañado")
        }
        
    def has_enough_good_fermentations(self):
        successful = [
            fermentation for fermentation in self.history
            if fermentation.result == "Buena"
        ]
        return len(successful) >= 3

    def calculate_milk(self, grains_weight):
        successful = [
            fermentation for fermentation in self.history if fermentation.result == "Buena"
        ]
        
        if len(successful) < 3:
            raise ValueError(
                "Necesitas al menos 3 fermentaciones buenas para hacer la recomendación."
            )

        recent_fermentations = successful[-3:]

        ratios = [
            fermentation.milk_ml / fermentation.grains_weight
            for fermentation in recent_fermentations
        ]

        ratio = calculate_average_ratio(ratios)
        return milk_needed(grains_weight, ratio)
