# 8 Ingresar 10 números enteros. Determinar el máximo y el mínimo.

# Variables
cantidad = 0

#Ingreso de numero para comparar
entrada = int(input("Ingrese un numero entero: "))
maximo = entrada
minimo = entrada
cantidad += 1

#Bucle while
while cantidad < 10: 
    entrada = int(input("Ingrese un numero entero: "))

    if entrada > maximo: 
        maximo = entrada
    elif entrada < minimo:
        minimo = entrada  

    cantidad += 1

#Prints final
print(f"El numero mínimo es: {minimo}")
print(f"El numero máximo es: {maximo}")