class Fermentation:
    def __init__(self, grains_weight, milk_ml, duration_hours, result):
        self.grains_weight = grains_weight
        self.milk_ml = milk_ml
        self.duration_hours = duration_hours
        self.result = result
        
    def describe_result(self):
        return f"Resultado: {self.result}"

class GoodFermentation(Fermentation):
    def __init__(self, grains_weight, milk_ml, duration_hours):
        super().__init__(
            grains_weight,
            milk_ml,
            duration_hours,
            "Buena"
        )
    def describe_result(self):
        return "\n¡Disfruta tu kéfir!\n"

class DamagedFermentation(Fermentation):
    def __init__(self, grains_weight, milk_ml, duration_hours):
        super().__init__(
            grains_weight,
            milk_ml,
            duration_hours,
            "Dañado"
        )
    def describe_result(self):
        return "\n¡Nunca dejes tu kéfir fermentar más de 48h en invierno o 24h en verano! Vigila la contaminación cruzada. Desecha los gránulos, no pueden volver a reutilizarse.\n"

class InsufficientFermentation(Fermentation):
    def __init__(self, grains_weight, milk_ml, duration_hours):
        super().__init__(
            grains_weight,
            milk_ml,
            duration_hours,
            "Insuficiente"
        )
    def describe_result(self):
        return "\nPoco tiempo, demasiada proporción de leche o temperaturas muy bajas pueden provocar fermentación insuficiente.\n"
        
class OverfermentedFermentation(Fermentation):
    def __init__(self, grains_weight, milk_ml, duration_hours):
        super().__init__(
            grains_weight,
            milk_ml,
            duration_hours,
            "Sobrefermentada"
        )
    def describe_result(self):
        return "\nDemasiado tiempo, poca leche o temperatura elevada pueden provocar la sobrefermentación.\n"