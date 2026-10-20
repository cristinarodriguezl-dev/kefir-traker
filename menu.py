import questionary

def main_menu ():
    while True:
        option = questionary.select(
            "Menú principal",
            choices=[
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
        elif option =="Consultar historial":
            print("Historial pendiente")
        elif option == "Ver estadísticas":
            print("Estadísticas pendientes")
            
