#Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

def num_par(numero):
    if numero %2 == 0 :
        return print(f"El numero ingresado es par")
    else:
        return print("El numero ingresado es impar")
num = int(input("Ingrese un numero: "))
num_par(num)