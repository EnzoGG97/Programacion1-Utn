#11
# Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.

numero = int(input("Ingresa un numero, el que mas te guste: "))
primos = 0

for n in range(2, numero +1):
    es_primo = True
    for i in range(2,n):
        if n % i == 0:
            es_primo = False
            break
    if es_primo:
        primos += 1

print(f"Se encontraron {primos} numeros primos")