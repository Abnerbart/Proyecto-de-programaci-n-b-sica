import os

# Se crea el archivo txt
def CrearArchivo(file):
    file = open("vendedores.txt", "w")
    print("Archivo de vendedores creado.")
    file.close()

#Se crea de manera remota los vendedores desde la consola
def AgregarVendedores():
    vendedor = input("Agrega al vendedor: ")
    cifra = input("Cuánto vendió?: ")
    file = open("vendedores.txt", "a")
    file.write(vendedor)
    file.write("\n")
    file.write(cifra)
    file.write("\n\n")
    print("\nLos vendedores han sido agregados.")
    file.close

# se imprime en pantalla los vendendores 
def MostrarVendedores():
    file = open("vendedores.txt", "r") 
    mensaje = file.read()
    print(mensaje)

# Se crea un bucle para agregar desde consola los nombre de los vendedores 
# o ya sea mostrarlos o simplemente salir de la consola.
opcion = ""
while opcion != "Salir":
    print("\n1. Agregar vendedor")
    print("2. Mostrar vendedores")
    print("3. Salir")
    opcion = input("\nElige una opción: ")
    
    if opcion == "1":
        AgregarVendedores()
    elif opcion == "2":
        MostrarVendedores()
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Por favor, elige nuevamente.")
