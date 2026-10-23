from src.validations import validate_milk_needed

"""Calcula la cantidad de leche que hay que añadir por la cantidad de gramos de gránulos de kéfir"""

#Cálculo de la leche necesaria.
def milk_needed(grains_weight, ratio):
    validate_milk_needed(grains_weight, ratio)

    return grains_weight * ratio

#Cálculo de las mejores fermentaciones.        
def calculate_average_ratio(ratios):
    if not ratios:
        raise ValueError("No hay fermentaciones.")

    return sum(ratios) / len(ratios)
