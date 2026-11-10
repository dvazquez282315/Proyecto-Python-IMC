# calculadora_imc.py
# Etapa 2: entrada dinamica de datos y calculo del IMC

# nombre: string (str)
nombre = input("Nombre: ")

# apellido_paterno: string (str)
apellido_paterno = input("Apellido paterno: ")

# apellido_materno: string (str)
apellido_materno = input("Apellido materno: ")

# edad: entero (int), en años -> casting con int()
edad = int(input("Edad (años): "))

# peso: decimal (float), en kilogramos -> casting con float()
peso = float(input("Peso (kg): "))

# estatura: decimal (float), en metros -> casting con float()
estatura = float(input("Estatura (m): "))

# IMC = peso / estatura^2
imc = peso / estatura ** 2

print("\n--- Resultado ---")
print("Nombre completo:", nombre, apellido_paterno, apellido_materno)
print("Edad:", edad, "años")
print("IMC:", round(imc, 2))
