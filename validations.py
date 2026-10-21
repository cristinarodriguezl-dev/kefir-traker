#Validación del cálculo de la leche
def validate_milk_needed(grains_weight, ratio):
    if not isinstance(grains_weight, (float, int)) or not isinstance(ratio, (float, int)):
        raise ValueError("La cantidad debe ser un número")
    elif grains_weight <= 0:
        raise ValueError("La cantidad debe ser mayor a 0")
    elif ratio <= 0:
        raise ValueError("La proporción debe ser mayor a 0")
    
    return True