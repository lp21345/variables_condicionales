# edad_votante.py
# Verifica si una persona puede votar según su edad y país

edad = int(input("Ingrese su edad: "))
pais = input("Ingrese su país (Colombia, Estados Unidos, Japón, Brasil, Alemania): ").lower()

if pais == "colombia" and edad >= 18:
    print("Puede votar en Colombia.")
elif pais == "estados unidos" and edad >= 18:
    print("Puede votar en Estados Unidos.")
elif pais == "japon" and edad >= 20:
    print("Puede votar en Japón.")
elif pais == "brasil" and edad >= 16:
    print("Puede votar en Brasil.")
elif pais == "alemania" and edad >= 18:
    print("Puede votar en Alemania.")
else:
    print("No puede votar en ese país o el país no está registrado.")