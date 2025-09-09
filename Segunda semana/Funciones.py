# def sumo_dos_numero(sumando1, sumando2):
#     resu = sumando1 + sumando2
#     return resu

# numero_1 = 10
# numero_2 = 5

# print(sumo_dos_numero(numero_1, numero_2))


"""
Nivel Básico
1. Función que saluda a una persona

Enunciado:
Escribí una función que reciba un nombre y muestre un saludo personalizado.
"""

# def saludo(nombre):
#     print("Hola " + nombre)

# nombre = input("Ingresa tu nombre: ")

# saludo(nombre)

# """
# Enunciado:
# Escribí una función que reciba base y altura, y devuelva el área.
# Datos por consola un argumento por defecto =10
# """

# def calculo (base = 10, altura = 0):
#     return (base * altura) / 2

# altura = float(input("Ingresa la altura del triangulo: "))

# resultado = calculo(altura = altura)

# print(f"Base: 10, Altura: {altura}")
# print(f"El área del triángulo es: {resultado}")


# """Nivel Intermedio
# Función que devuelva suma, resta y multiplicación

# Enunciado:
# Escribí una función que reciba dos números y devuelva los tres resultados: suma, resta y multiplicación."""

# def operaciones(numero_1, numero_2):
#     suma = numero_1 + numero_2
#     resta = numero_1 - numero_2
#     multiplicación = numero_1 * numero_2
#     return suma, resta, multiplicación

# numero_1 = float(input("Ingrese un numero: "))
# numero_2 = float(input("Ingrese un segundo numero: "))
# suma, resta, multiplicación = operaciones(numero_1, numero_2)

# print(f"Suma: {suma}")
# print(f"resta: {resta}")
# print(f"multiplicación: {multiplicación}")

"""
Enunciado:
Escribí una función que reciba cualquier cantidad de números y los sume los parametros por consola.

Ayuda: pedir al usuario cuantos numeros cargar, luego usar ese valor para iterar
"""
def suma_numeros ():
    cantidad = int(input("Cuantos numeros queres sumar?: "))
    
    suma = 0

    for i in range (cantidad):
        numero = int(input("Ingresa un numero: "))

        suma += numero
    return suma

resultado = suma_numeros()
print(f"La suma total es: {resultado}")