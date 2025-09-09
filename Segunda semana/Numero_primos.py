# #Numeros primos
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

numero_ingresado = int(input("Ingresa un numero: "))

if es_primo(numero_ingresado):
    print(f"El número {numero_ingresado} es primo.")
else:
    print(f"El número {numero_ingresado} no es primo.")