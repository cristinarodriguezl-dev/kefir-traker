import questionary
from calculations import milk_needed, calculate_average_ratio
from storage import load_history, save_fermentation


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
        elif option == "Registrar fermentación":
            grains_weight = float(
                questionary.text("Gramos de gránulos de kéfir:").ask()
            )
            milk_ml = float(
                questionary.text("Mililitros de leche utilizados:").ask()
            )
            duration_hours = float(
                questionary.text("Horas de fermentación:").ask()
            )
            result = questionary.select(
                "¿Cómo ha quedado la fermentación?",
                choices=["buena", "sobrefermentada", "insuficiente"]
            ).ask()

            fermentation = {
                "grains_weight": grains_weight,
                "milk_ml": milk_ml,
                "duration_hours": duration_hours,
                "result": result
            }

            save_fermentation(fermentation)
            print("Fermentación guardada correctamente.")
        
        
        elif option == "Calcular cantidad de leche necesaria":
            grains_weight = float(
                questionary.text("Ingrese los gramos de gránulos de kéfir:").ask()
            )

            history = load_history()

            successful = [
                fermentation for fermentation in history
                if fermentation["result"] == "buena"
            ]

            if len(successful) < 3:
                print("Necesitas al menos 3 fermentaciones buenas para hacer la recomendación.")
            else:
                best_fermentations = successful[:3]

                ratios = [
                    fermentation["milk_ml"] / fermentation["grains_weight"]
                    for fermentation in best_fermentations
                ]

                ratio = calculate_average_ratio(ratios)
                print(f"Cantidad de leche recomendada: {milk_needed(grains_weight, ratio):.0f} ml")


        elif option =="Consultar historial":
            print("Historial pendiente")
        elif option == "Ver estadísticas":
            print("Estadísticas pendientes")
            
