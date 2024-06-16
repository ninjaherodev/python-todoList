import colors as col

def mostrar_opciones():
    print("\nOpciones:")
    print("1. Crear una tarea")
    print("2. Marcar como realizada una tarea")
    print("3. Borrar una tarea")
    print("4. Salir")

def main():
    
    print(f'{col.COLOR_ROJO}\nwelcome to a python to do list:{col.RESET_COLOR}')
    while True:
        mostrar_opciones()
        opcion = int(input("Seleccione una opción (1-4): "))
        match opcion:
            case 1:
                print('Crear tarea...')
            case 2:
                print('Marcar como realizada...')
            case 3:
                print('Borrar una tarea')
            case 4:
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número del 1 al 4.")

if __name__ == '__main__':
    main()