# temperatura.py
# Programa que convierte temperaturas entre Celsius, Fahrenheit y Kelvin

# Pedimos la temperatura y las escalas
temp = float(input("Ingrese la temperatura a convertir: "))
origen = input("Ingrese la escala de origen (celsius, fahrenheit, kelvin): ").lower()
destino = input("Ingrese la escala de destino (celsius, fahrenheit, kelvin): ").lower()

resultado = None  # Variable para guardar el resultado

# Conversiones
if origen == "celsius":
    if destino == "fahrenheit":
        resultado = (temp * 9/5) + 32
    elif destino == "kelvin":
        resultado = temp + 273.15
    elif destino == "celsius":
        resultado = temp

elif origen == "fahrenheit":
    if destino == "celsius":
        resultado = (temp - 32) * 5/9
    elif destino == "kelvin":
        resultado = (temp - 32) * 5/9 + 273.15
    elif destino == "fahrenheit":
        resultado = temp

elif origen == "kelvin":
    if destino == "celsius":
        resultado = temp - 273.15
    elif destino == "fahrenheit":
        resultado = (temp - 273.15) * 9/5 + 32
    elif destino == "kelvin":
        resultado = temp

# Mostrar resultado o error si las escalas son incorrectas
if resultado is not None:
    print(f"{temp} {origen.capitalize()} equivalen a {resultado:.2f} {destino.capitalize()}")
else:
    print(" Error: Escalas ingresadas no válidas.")
