import questionary
from src.kefir_tracker import KefirTracker
from src.models import Fermentation


def main_menu ():
    tracker = KefirTracker()

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

            fermentation = Fermentation(
                grains_weight,
                milk_ml,
                duration_hours,
                result
            )

            tracker.register_fermentation(fermentation)
            print("Fermentación guardada correctamente.")
        
        elif option == "Eliminar fermentación":
            history = tracker.get_history()

            if not history:
                print("No hay fermentaciones guardadas.")
            else:
                choices = [
                    f"{i}. {f.result} - {f.grains_weight} g de kéfir, {f.milk_ml} ml de leche"
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
                        tracker.remove_fermentation(index)
                        print("Fermentación eliminada correctamente.")
                    else:
                        print("Eliminación cancelada.")
        
        elif option == "Calcular cantidad de leche necesaria":
            if not tracker.has_enough_good_fermentations():
                print("Necesitas al menos 3 fermentaciones buenas para hacer el cálculo.")
            else:
                try:
                    grains_weight = float(
                        questionary.text(
                            "Ingrese los gramos de gránulos de kéfir:"
                        ).ask()
                    )
                    milk = tracker.calculate_milk(grains_weight)
                    print(f"Cantidad de leche recomendada: {milk:.0f} ml")
                except ValueError as error:
                    print(error)


        elif option =="Consultar historial":
            history = tracker.get_history()
            if not history:
                print("No hay fermentaciones registradas")
            else:
                for index, fermentation in enumerate(history, start=1):
                    print()
                    print(f"Fermentación {index}")
                    print(f"Gránulos: {fermentation.grains_weight}g")
                    print(f"Leche: {fermentation.milk_ml}ml")
                    print(f"Horas de fermentación: {fermentation.duration_hours}h")
                    print(f"Resultado: {fermentation.result}")
                    print("\n***********************")

        elif option == "Ver estadísticas":
            history = tracker.get_history()

            stats = tracker.get_statistics()

            total = stats["total"]

            if total == 0:
                print("No hay fermentaciones registradas.")
            else:
                good = stats["good"]
                overfermented = stats["overfermented"]
                insufficient = stats["insufficient"]
                damage = stats["damaged"]
                good_percentage = good / total * 100

                print("\n-- ESTADÍSTICAS DE FERMENTACIÓN --\n")
                print(f"Total: {total}")
                print(f"Resultados buenos: {good}")
                print(f"Sobrefermentaciones: {overfermented}")
                print(f"Fermentaciones insuficientes: {insufficient}")
                print(f"Dañadas: {damage}")
                print(f"Porcentaje de éxito: {good_percentage:.1f}%")

                if overfermented > insufficient and overfermented > damage:
                    print("\nSugerencia: Reduce las horas de fermentación o la temperatura a la que fermentan tus gránulos.\n")
                elif insufficient > overfermented and insufficient > damage:
                    print("\nSugerencia: Aumenta las horas de fermentación o la cantidad de leche.\n")
                elif damage > overfermented and damage > insufficient:
                    print("\nSugerencia: Revisa tus gránulos de kéfir. Puede ser necesario reemplazarlos, cambiar su lugar de fermentación o lavar cuidadosamente los utensilios que usas.\n")