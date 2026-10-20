"""Calcula la cantidad de leche que hay que añadir por la cantidad de gramos de gránulos de kéfir"""

def milk_needed(grains_weight, ratio):
    milk_needed = grains_weight * ratio
    
    if milk_needed <=0:
        raise ValueError("La cantidad de leche debe ser mayor a 0")

    return milk_needed
        
        