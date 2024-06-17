import os

# Se crea el archivo base de datos.txt
def CrearArchivo(file):
    file = open("BaseDeDatos.txt", "w")
    print("Archivo de colaboradores creado.")
    file.close()

#Se crea de manera remota los desde la consola todo lo que necesitamos del colaborador
def Agregarcolaborador():
    colaborador = input("Agrega al colaborador: ")
    fecha_ingreso = (input("Ingrese la fecha en la que ingreso el colaborador: "))
    puesto = input("Ingrese el puesto del colaborador: ")
    correo = input("Ingrese el correo del colaborador: ")
    salario = (input("Ingrese el salario del colaborador: "))
    file = open("BaseDeDatos.txt", "a")
    file.write(colaborador)
    file.write("\n")
    file.write(fecha_ingreso)
    file.write("\n")
    file.write(puesto)
    file.write("\n")
    file.write(correo)
    file.write("\n")
    file.write(salario)
    file.write("\n")
    print("\nLos datos del colaborador han sido agregados.")
    file.close

# se imprime en pantalla los vendendores 
def Mostrarcolaborador():
    file = open("BaseDeDatos.txt", "r") 
    mensaje = file.read()
    print(mensaje)

# Se crea un bucle para agregar desde consola los nombre de los vendedores 
# o ya sea mostrarlos o simplemente salir de la consola.
opcion = ""
while opcion != "Salir":
    print("\n1. Agregar colaborador")
    print("2. Mostrar colaboradores")
    print("3. Salir")
    opcion = input("\nElige una opción: ")
    
    if opcion == "1":
        Agregarcolaborador()
    elif opcion == "2":
        Mostrarcolaborador()
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("\033[94mOpción no válida. Por favor, elige nuevamente.\033[0m")