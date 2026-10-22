# pyrefly: ignore[missing-import]
import questionary
from src.calculations import milk_needed, calculate_average_ratio
from src.storage import load_history, save_fermentation, delete_fermentation


def main_menu ():
    while True:
        option = questionary.select(
            "Menú principal",
            choices=[
                "Calcular cantidad de leche necesaria",
                "Registrar fermentación",
                "Eliminar fermentación",
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
                choices=["Buena", "Sobrefermentada", "Insuficiente", "Dañado"]
            ).ask()

            fermentation = {
                "grains_weight": grains_weight,
                "milk_ml": milk_ml,
                "duration_hours": duration_hours,
                "result": result
            }

            save_fermentation(fermentation)
            print("Fermentación guardada correctamente.")
        
        elif option == "Eliminar fermentación":
            history = load_history()

            if not history:
                print("No hay fermentaciones guardadas.")
            else:
                choices = [
                    f"{i}. {f['result']} - {f['grains_weight']} g de kéfir, {f['milk_ml']} ml de leche"
                    for i, f in enumerate(history, start=1)
                ]

                selected = questionary.select(
                    "¿Qué fermentación quieres eliminar?",
                    choices=choices
                ).ask()

                if selected is not None:
                    confirm = questionary.select(
                        "¿Seguro que quieres eliminar esta fermentación?",
                        choices=["Sí", "No"]
                    ).ask()

                    if confirm == "Sí":
                        index = choices.index(selected)
                        delete_fermentation(index)
                        print("Fermentación eliminada correctamente.")
                    else:
                        print("Eliminación cancelada.")
        
        elif option == "Calcular cantidad de leche necesaria":
            history = load_history()
            successful = [
                fermentation for fermentation in history
                if fermentation["result"] == "Buena"
            ]
            if len(successful) < 3:
                print("Necesitas al menos 3 fermentaciones buenas para hacer la recomendación.")

            else:
                grains_weight = float(
                questionary.text("Ingrese los gramos de gránulos de kéfir:").ask()
            )
                best_fermentations = successful[:3]

                ratios = [
                    fermentation["milk_ml"] / fermentation["grains_weight"]
                    for fermentation in best_fermentations
                ]

                ratio = calculate_average_ratio(ratios)
                milk = milk_needed(grains_weight, ratio)
                print(f"Cantidad de leche recomendada: {milk:.0f} ml")


        elif option =="Consultar historial":
            history = load_history()
            if not history:
                print("No hay fermentaciones registradas")
            else:
                for index, fermentation in enumerate(history, start=1):
                    print()
                    print(f"Fermentación {index}")
                    print(f"Gránulos: {fermentation['grains_weight']}g")
                    print(f"Leche: {fermentation['milk_ml']}ml")
                    print(f"Horas de fermentación: {fermentation['duration_hours']}h")
                    print(f"Resultado: {fermentation['result']}")
                    print("\n***********************")

        elif option == "Ver estadísticas":
            history = load_history()

            if not history:
                print("No hay fermentaciones registradas.")
            else:
                total = len(history)
                good = sum(1 for fermentation in history if fermentation["result"] == "Buena")
                overfermented = sum(1 for fermentation in history if fermentation["result"] == "Sobrefermentada")
                insufficient = sum(1 for fermentation in history if fermentation["result"] == "Insuficiente")
                damage = sum(1 for fermentation in history if fermentation["result"] == "Dañado")

                print(f"Total: {total}")
                print(f"Resultados buenos: {good}")
                print(f"Sobrefermentaciones: {overfermented}")
                print(f"Fermentaciones insuficientes: {insufficient}")
                print(f"Dañadas: {damage}")

                good_percentage = (good / total * 100)

                print(f"Porcentaje de éxito: {good_percentage:.1f}%")

                if overfermented > insufficient and overfermented > damage:
                    print("\nSugerencia: Reduce las horas de fermentación o la temperatura a la que fermentan tus gránulos.\n")
                elif insufficient > overfermented and insufficient > damage:
                    print("\nSugerencia: Aumenta las horas de fermentación o la cantidad de leche.\n")
                elif damage > overfermented and damage > insufficient:
                    print("\nSugerencia: Revisa tus gránulos de kéfir. Puede ser necesario reemplazarlos, cambiar su lugar de fermentación o lavar cuidadosamente los utensilios que usas.\n")