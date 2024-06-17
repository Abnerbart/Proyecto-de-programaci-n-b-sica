#Creamos una matriz vacía
salarios_netos= []

#Función que define los empleados a los que se les pagará
def deducciones():
    
    #Permite elegir a cuántos empleados se les pagará
    cantEmpleados= int(input("Ingrese la cantidad de empleados a pagar: "))
    
    #Condicional que define que deducciones se le aplican al salario bruto y que muestra el precio por hora laborada
    for i in range (cantEmpleados):
        contador= i+1
        salario_mes = float(input(f"\nIngrese el salario bruto a pagar del empleado {contador}: "))
        laboradas= float(input(f"\nIngrese la cantidad de horas laboradas mensuales del empleado {contador}: "))

        if salario_mes<=929000:
            CCSS= salario_mes * 0.1067
            salario_neto= salario_mes - CCSS

            #Añadimos el salario a la lista
            salarios_netos.append(salario_neto)

            #Calculo del precio por hora laborada
            precioHoras= salario_mes / laboradas
            print (f"\nAl haber trabajado {laboradas} horas el precio por hora es de: {precioHoras}")

    
        elif salario_mes>929000 and salario_mes<=1363000:
            dif= (salario_mes - 929000) *0.10
            CCSS= salario_mes * 0.1067
            difTotal= dif + CCSS
            salario_neto= salario_mes - difTotal

            #Añadimos el salario a la lista
            salarios_netos.append(salario_neto)

            #Calculo del precio por hora laborada
            precioHoras= salario_mes / laboradas
            print (f"\nAl haber trabajado {laboradas} horas el precio por hora es de: {precioHoras}")


        elif salario_mes>1363000 and salario_mes<=2392000:
            dif_uno= (salario_mes - 929000) * 0.10
            dif_dos= (salario_mes - 1363000) * 0.15
            CCSS= salario_mes * 0.1067
            difTotal= dif_uno + dif_dos + CCSS
            salario_neto= salario_mes - difTotal

            #Añadimos el salario a la lista
            salarios_netos.append(salario_neto)

            #Calculo del precio por hora laborada
            precioHoras= salario_mes / laboradas
            print (f"\nAl haber trabajado {laboradas} horas el precio por hora es de: {precioHoras}")

        elif salario_mes>2392000 and salario_mes<= 4783000:
            dif_uno= (salario_mes - 929000) * 0.10
            dif_dos= (salario_mes - 1363000) * 0.15
            dif_tres= (salario_mes - 2392000) * 0.20
            CCSS= salario_mes * 0.1067
            difTotal= dif_uno + dif_dos + dif_tres + CCSS
            salario_neto= salario_mes - difTotal

            #Añadimos el salario a la lista
            salarios_netos.append(salario_neto)

            #Calculo del precio por hora laborada
            precioHoras= salario_mes / laboradas
            print (f"\nAl haber trabajado {laboradas} horas el precio por hora es de: {precioHoras}")

        elif salario_mes>4783000:
            dif_uno= (salario_mes - 929000) * 0.10
            dif_dos= (salario_mes - 1363000) * 0.15
            dif_tres= (salario_mes - 2392000) * 0.20
            dif_cuatro= (salario_mes - 4783000) * 0.25
            CCSS= salario_mes * 0.1067
            difTotal= dif_uno + dif_dos + dif_tres + dif_cuatro + CCSS           
            salario_neto= salario_mes - difTotal

            #Añadimos el salario a la lista
            salarios_netos.append(salario_neto)

            #Calculo del precio por hora laborada
            precioHoras= salario_mes / laboradas
            print (f"\nAl haber trabajado {laboradas} horas el precio por hora es de: {precioHoras}")

#Mensaje de entrada        
print ("---Activando módulo de pagos---\n\n")

#Llamamos la función
deducciones()

#Definición de variables con el fin de poder hacer un escalafón      
salarios_ordenados= sorted(salarios_netos)

#Salida de los resultados
print (f"\nDe manera ordenada los salarios netos van:", salarios_ordenados)
print ("\n---Saliendo del módulo de pagos---")
