# calculadora.py
# Programa que simula una calculadora básica usando condicionales

# Pedimos 2 numeros 
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Pedimos la operación que desea realizar
print("\nOperaciones disponibles: suma(1), resta(2), multiplicacion(3), division(3)")
operacion = input("Ingrese el numero de la operación que desea realizar: ").lower()

# Usamos condicionales para decidir la operación
# imprimimos el resultado de la operacion 
if operacion == "1":
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")

elif operacion == "2":
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")

elif operacion == "3":
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")

elif operacion == "4":
    if num2 == 0:
        print(" Error: No se puede dividir entre cero.")
    else:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")

else:
    print(" Error: Operación no válida. Intente de nuevo.")