import os 


def AgregarCapacitaciones():
    capacitaciones = input("Registrar capacitaciones del colaborador \033[91m(5 máximo):\033[0m ").split(',')[:5] 
    if len(capacitaciones) > 5:
        print("Solo se permite al empleado 5 capacitaciones")
        return 
    file = open("BaseDeDatos.txt", "a")
    file.write(','.join(capacitaciones) + "\n")
    file.close()

def mostrar_Capacitacion():
  if os.path.exists("BaseDeDatos.txt"):
    file = open("BaseDeDatos.txt", "r")
    mensaje = file.read()
    print("Mostrando capacitaciones realizadas...\n" , mensaje)
    
    for line in file:
        print(line.strip())
    file.close

opcion = ""
menu_options = ["Agregar colaborador", "Salir"]

for opcion in menu_options:
    print("\n1. Agregar capacitaciones del colaborador")
    print("2. Mostrar las capacitaciones")
    print("3. Salir, espere un momento")
    opcion = input("\nElige entre las opción: ")

    if opcion == "1":
        AgregarCapacitaciones()
    elif opcion == "2":
        mostrar_Capacitacion()
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("\033[91mOpción no valida, Intente nuevamente.\033[0m")
