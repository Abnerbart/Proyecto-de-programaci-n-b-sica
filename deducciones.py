import os
#Creamos una lista vacía
salarios_netos= []

#Función del cálculo de los salarios netos y el cálculo de precio por hora
def calcular_salario_neto(salario_bruto_mensual):
    # Deducciones de Hacienda
    renta_exenta = 929000
    exceso_renta = max(0, salario_bruto_mensual - renta_exenta)
    
    if exceso_renta <= 1363000:
        impuesto_renta = exceso_renta * 0.10
    elif exceso_renta <= 2392000:
        impuesto_renta = 136300 + (exceso_renta - 1363000) * 0.15
    elif exceso_renta <= 4783000:
        impuesto_renta = 136300 + 103050 + (exceso_renta - 2392000) * 0.20
    else:
        impuesto_renta = 136300 + 103050 + 478200 + (exceso_renta - 4783000) * 0.25
    
    # Deducciones de Seguro Social
    CCSS = salario_bruto_mensual * 0.09
    Pension = salario_bruto_mensual * 0.0725
    
    # Salario neto
    salario_neto = salario_bruto_mensual - impuesto_renta - CCSS - Pension
    salarios_netos.append(salario_neto)

    # Precio por hora trabajada
    precioHoras= salario_bruto_mensual / laboradas
    print (f"\nAl haber trabajado {laboradas} horas el precio por hora es de: {precioHoras}")

    return salario_neto

#Mensaje de entrada        
print ("---Activando módulo de pagos---\n\n")

# Ingresar la cantidad de empleados a pagar
cant = int(input("Ingrese la cantidad de empleados a pagar: "))

for i in range(cant):
    salario_bruto_mensual = float(input(f"\nIngrese el salario bruto mensual {i + 1}: ₡"))
    laboradas= float(input(f"\nIngrese la cantidad de horas laboradas mensuales del empleado {i + 1}: "))
    salario_neto = calcular_salario_neto(salario_bruto_mensual,)
    
    print("-" * 30)

# Ordenamos los salarios de menor a mayor
salarios_ordenados= sorted(salarios_netos)
print (f"\nDe manera ordenada los salarios netos van:", salarios_ordenados)

#Mensaje de salida  
print ("\n\n---Saliendo del módulo de pagos---")

def registro_de_pagos():
    arch = open ("Pagos.txt", "a")
    arch.write ("---Entrada de Datos Detectada---\n")
    arch.write (f"\nDe manera ordenada los salarios netos van: {str(salarios_ordenados)}")
    arch.close()

registro_de_pagos()


