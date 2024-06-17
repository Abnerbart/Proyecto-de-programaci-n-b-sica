# En el global ponemos los días de vacaciones con sus asignaciones.
dias = 15

solicitar_vacaciones = input("Deseas solicitar vacaciones (si/no): ")
aprobacion = int(input("Ingresar los días: "))

#Se calcula la cantidad de días de vacaciones y luego se resta por los mismos pero sin poder consultar las vacaciones.
if solicitar_vacaciones.lower() == "si":
    if aprobacion <= dias:
        dias -= aprobacion 
        print("\033[92mVacaciones aprobadas por", aprobacion, "días\033[0m")
        print("\033[92mVacaciones reducidas por", dias, "días\033[0m")
    else:
        print("\033[91mNo tiene vacaciones disponibles\033[0m")
else:
    print("\033[91mIntente más tarde!\033[0m")