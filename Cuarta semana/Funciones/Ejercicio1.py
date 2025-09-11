#Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def pedir_entero():
    numero = int(input("Ingrese un numero entero: "))
    return numero
numero_entero = pedir_entero()
print(f"El numero entero ingresado es: {numero_entero}")