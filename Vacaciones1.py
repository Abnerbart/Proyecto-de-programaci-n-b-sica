import os
# Se solicita las vacaciones para hacer solicitud de estas mismas.
aprobar_vacaciones = int(input("ingrese la consulta de aprobación en días: "))

# Se agrega a la base de datos sus dias de vacaciones del trabajador.
    
def AgregarVacaciones():
    Vacaciones = input("Agregar vacaciones del colaborador: ") 
    file = open("BaseDeDatos.txt", "a")
    file.write(Vacaciones)
    file.close()


opcion = ""
while opcion != "Salir":
    print("\n1. Agregar colaborador")
    print("2. Salir")
    opcion = input("\nElige una opción: ")
    
    if opcion == "1":
        AgregarVacaciones()
    elif opcion == "2":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Por favor, elige nuevamente.")
    
# Se define la funcion verificar para luego ver si el empleado tiene las vacaciones.
def verificar(aprobar_vacaciones):
    if aprobar_vacaciones >= 15:
        print("\033[92mAprobar vacaciones por", aprobar_vacaciones, "días\033[0m")
    else:
        print("\033[91mNo aprobado, días insuficientes\033[0m")      
                    
verificar(aprobar_vacaciones) 