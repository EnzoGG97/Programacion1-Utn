#Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.


def pedir_float():
    numero = float(input("Ingrese un numero flotante: "))
    return numero
num = pedir_float()

print(f"El numero flotante es: {num}")

