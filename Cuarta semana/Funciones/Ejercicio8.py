#Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

def maximos(num1, num2, num3):
    if num1 > num2 > num3 :
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer y ultimo numero: "))

mayor = max(num1, num2, num3)
print(f"El numero mas grande es: {mayor}")