import subprocess

# Los procesos se ejecutan en modo lista o tupla
modulos = ["Empleados1.py", "Vacaciones1.py", "Vacaciones2.py", "capacitaciones.py", "capacitaciones2.py" ,"deducciones.py" , "correos.py"]

# Los modulos se ejecutan uno por uno segun la lista anterior
for modulo in modulos:
    print(f"Ejecutando los procesos {modulos}....!")
    subprocess.run([f"python", modulo])

print("Los programas ejecutados han finalizado exitosamente.",)    