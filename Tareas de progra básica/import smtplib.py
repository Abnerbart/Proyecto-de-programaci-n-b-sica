import smtplib
from email.mime.multipart import Empleados1
from email.mime.text import MIMEText

# Configuración del servidor SMTP
smtp_host = 'smtp.tu_servidor_smtp.com'
smtp_port = 587  # Puerto seguro TLS
smtp_user = 'tu_correo@gmail.com'
smtp_password = 'tu_contraseña'

# Crear mensaje
mensaje = Empleados1()
mensaje['From'] = smtp_user
mensaje['To'] = input("Registra el correo para enviarlo automaticamente: ")
mensaje['Subject'] = 'Felicidades "" por tu cumpleaños te damos un día más de vacaciones para que distrufes de tu estadía en la empresa!'

# Cuerpo del mensaje
cuerpo_mensaje = 'Hola, este es un correo de prueba enviado desde Python.'
mensaje.attach(MIMEText(cuerpo_mensaje, 'plain'))

# Iniciar conexión con el servidor SMTP
server = smtplib.SMTP(smtp_host, smtp_port)
server.starttls()  # Activar el modo de seguridad TLS
server.login(smtp_user, smtp_password)

# Enviar correo electrónico
texto_correo = mensaje.as_string()
server.sendmail(smtp_user, 'destinatario@example.com', texto_correo)

# Cerrar conexión con el servidor SMTP
server.quit()

print("Correo enviado exitosamente.")
