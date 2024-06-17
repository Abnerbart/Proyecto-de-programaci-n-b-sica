#Importamos la librería de días
import datetime
import os

#Importamos la librería que habilita la opción de envío de mensajes SMTP
import smtplib
from email.message import EmailMessage

# Obtener el día y mes actual
dia_actual = datetime.date.today().day
mes_actual = datetime.date.today().month
fecha_hoy= datetime.date.today()

#Creamos una lista vacía
lista= []
   
#Hacemos la entrada de datos en la matriz
empleados= int(input("Ingrese la cantidad de empleados a ingresar: "))
for i in range(empleados):
    i+=1
    str_nacimiento= input(f"\nIngrese la fecha de nacimiento del empleado {i}(en formato DD/MM/AAAA): ")

    # Convertimos la fecha ingresada a un objeto datetime
    fecha_nacimiento = datetime.datetime.strptime(str_nacimiento, "%d/%m/%Y")

    # Convertimos la fecha de nacimiento a timestamp Unix
    timestamp = fecha_nacimiento.timestamp()
    
    correo= input(f"\nIngrese el correo del empleado {i}: ")
    lista.append([timestamp,correo])

#Creamos una lista vacía que almacenará los correos cuyas fechas sean cumpleaños
coincidencias_correos= []

#Buscamos coincidencias entre la fecha actual y las ingresadas
for fecha, correo in lista:
    # Convertir la fecha de nacimiento a un objeto de fecha
    fecha_nacimiento = datetime.date.fromtimestamp(fecha)

    # Verificar si el día y mes de la fecha de nacimiento coinciden con el día y mes actuales
    if fecha_nacimiento.month == mes_actual and fecha_nacimiento.day == dia_actual:
        coincidencias_correos.append(correo)

# Si hay correos de cumpleaños, enviamos los correos electrónicos
if coincidencias_correos:
    
    # Definimos el usuario remitente
    remitente = "fitofreddy6@gmail.com"

    # Indicamos por medio de qué protocolo enviaremos el correo
    smtp = smtplib.SMTP_SSL("smtp.gmail.com")

    # Permitimos el login a Gmail a través de la cuenta de aplicación
    smtp.login(remitente, "nele bpht crpf gdud")
    
    # Creamos un mensaje de correo
    email = EmailMessage()
    email["From"] = remitente
    email["Subject"] = "Feliz cumpleaños!"
    email.set_content("¡Feliz cumpleaños! Esperamos que tengas un día maravilloso.")


    # Enviamos un correo a cada empleado cuyo cumpleaños coincida con la fecha actual
    for correo in coincidencias_correos:
        email = EmailMessage()
        email["From"] = remitente
        email["To"] = correo
        email["Subject"] = "Feliz cumpleaños!"
        email.set_content("¡Feliz cumpleaños! Esperamos que tengas un día maravilloso.")

        #Hacemos envío del correo
        smtp.send_message(email)

    # Cerramos la conexión SMTP
    smtp.quit()
    print("Correos electrónicos de cumpleaños enviados exitosamente.")
else:
    print("No hay cumpleaños hoy.")


def registro_cumpleaños():
    arch = open ("Cumpleaños.txt", "a")
    arch.write ("---Entrada de Datos Detectada---\n")
    arch.write (f"\nEl {fecha_hoy} se le envió correos a: ")
    for correo in coincidencias_correos:
        arch.write(f"- {correo}\n")
    arch.close()

registro_cumpleaños()
