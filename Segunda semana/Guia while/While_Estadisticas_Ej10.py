# 10 Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.

#Variables
suma = 0
contador = 0 

#Texto inicial
print("Debes ingresar de 5 a 10 numeros")

#Bucle while
while contador < 10 :
    numero = int(input("Ingrese un numero: "))
    suma += numero
    contador += 1

#A partir del 5 numero ingresado da opcion de terminar
    if contador >= 5 :
        parar = input("Si queres seguir ingrsando presiona ENTER, sino presiona 'e':")
        if parar == "e" or parar == "E":
            break

#Promedio
promedio = suma / contador

#Prints finales
print(f"La suma de los numeros ingresados son: {suma}")
print(f"El promedio es: {promedio:.2f}")