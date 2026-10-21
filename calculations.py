from validations import validate_milk_needed

"""Calcula la cantidad de leche que hay que añadir por la cantidad de gramos de gránulos de kéfir"""

#Cálculo de la leche necesaria.
def milk_needed(grains_weight, ratio):
    validate_milk_needed(grains_weight, ratio)
    milk_needed = grains_weight * ratio

    return milk_needed

#Cálculo de las mejores fermentaciones.        
def calculate_average_ratio(ratios):
    if not ratios:
        raise ValueError("No hay fermentaciones.")
        
    average_ratio = sum(ratios) / len(ratios)

    return average_ratio
