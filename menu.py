import questionary
from calculations import milk_needed

def main_menu ():
    while True:
        option = questionary.select(
            "Menú principal",
            choices=[
                "Calcular cantidad de leche necesaria",
                "Registrar fermentación",
                "Consultar historial",
                "Ver estadísticas",
                "Salir"
            ]
        ).ask()

        if option =="Salir" or option is None:
            print("¡Hasta pronto!")
            break
        elif option =="Registrar fermentación":
            print("Registro pendiente")
        
        elif option =="Calcular cantidad de leche necesaria":
            grains_weight = float(questionary.text("Ingrese la cantidad de gramos de gránulos de kéfir:").ask())
            ratio = float(questionary.text("Ingrese la proporción de leche por gramo de gránulos:").ask())
            print(milk_needed(grains_weight, ratio))

        elif option =="Consultar historial":
            print("Historial pendiente")
        elif option == "Ver estadísticas":
            print("Estadísticas pendientes")
            
