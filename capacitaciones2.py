import os 

# En el global ponemos el total de capacitaciones que puedan solicitar el usuario.
capacitaciones = 5 

# Se pide que muestre las capacitaciones con el archivo plano a continuación.
def mostrar_capacitaciones():
    with open("BaseDeDatos.txt", "r") as archivo:
        print("\033[92m Capacitaciones del colaborador:\033[0m")
        for linea in archivo:
            print(linea.strip())

ver_capacitaciones = input("Desea ver las capacitaciones del colaborador? (si/no)")

# Verifica si queremos ver las capacitaciones
if ver_capacitaciones.lower() == "si":
    mostrar_capacitaciones() 
else:
    print("\033[91mIntente nuevamente más tarde\033[0m")

# Solicita nuevamente los datos del empleado
solicitar_capacitaciones = input("¿Quieres solicitar más capacitaciones? (si/no): ")

if solicitar_capacitaciones.lower() == "si":
    capacitaciones_solicitadas = int(input("¿Cuántas capacitaciones deseas solicitar?: "))
    if capacitaciones_solicitadas > capacitaciones:
        print("\033[91mNo hay suficientes capacitaciones disponibles.\033[0m")
    else:
        capacitaciones -= capacitaciones_solicitadas
        print("\033[90mLas capacitaciones que elegiste son: \033[0m", capacitaciones_solicitadas)

    # Se actualiza el archivo con la nueva cantidad de capacitaciones
    with open("BaseDeDatos.txt" , "a") as archivo:
        archivo.write(str(capacitaciones) + "\n")
        print("\033[92mSe aprobaron las siguientes capacitaciones, quedan:\033[0m", capacitaciones)

else:
    print("\033[91mError, intente más tarde.\033[0m")

# Se muestra nuevamente las capacitaciones del colaborador
mostrar_capacitaciones()
