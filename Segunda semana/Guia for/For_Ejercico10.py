#10
# Ingresar un número. Determinar si el número es primo o no

numero = int(input("Ingresa un numero, el que mas te guste: "))

if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print("No es primo")
            break
    else:
        print("Es primo")
else:
    print("No es primo")
