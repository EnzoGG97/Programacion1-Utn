# 9 Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.

#Variables
contador = 0 
suma = 0

#Primer bucle while para tener un minimo de 5
while contador <5:
    numero = int(input("Ingrese un numero (como minimo deben ser 5): "))
    suma += numero
    contador += 1

#Segundo bucle while con opcion a salida
while True : 
    numero = input("Ingrese tantos numero como quiera (o ingrese 'e' para terminar): ")
    if numero == 'e' or numero == 'E':
        break
    suma += int(numero) 
    contador += 1

#Promedio 
promedio = suma / contador 

#Prints finales
print(f"La suma de los numeros ingresados es: {suma}")
print(f"El promedio es: {promedio:.2f}")