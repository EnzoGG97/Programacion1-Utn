# 6 Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.

# Variables
suma = 0
cantidad = 0 

#Bucle while
while True :
    entrada = input("Ingrese un numero (o presione 'e' para salir): ")
    if entrada == 'e' or  entrada == 'E':
        break

#Calculos y promedios
    numero = entrada
    suma += numero 
    cantindad += 1

    if cantidad > 0:
        promedio = suma / cantidad
#Prints finales
    print(f"La suma de los números es: {suma}")
    print(f"El promedio de los números es: {promedio}")
else:
    print("No se ingresaron números.")