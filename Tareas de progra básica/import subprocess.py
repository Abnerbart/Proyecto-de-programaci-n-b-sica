import subprocess

# Lista de módulos a ejecutar en secuencia
modulos = ["Empleados1.py" , "Empleados2.py" , "Vacaciones1"  , "capacitaciones" , "deducciones_ccss1" ]

# Itera sobre la lista de módulos y ejecútalos
for modulo in modulos:
    print(f"Ejecutando {modulo}...")
    subprocess.run(["python", modulo])

print("Todos los módulos han sido ejecutados.")
