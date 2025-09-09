# 5 Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.

#Variables
a = 0
b = 0
c = 0
d = 0
e = 0

#pedido de datos
contador = 0
while contador < 5:
    if contador == 0:
        a = int(input("Ingrese el primer numero: "))
    elif contador == 1:
        b = int(input("Ingrese el segundo numero: "))
    elif contador == 2:
        c = int(input("Ingrese el tercer numero: "))
    elif contador == 3:
        d = int(input("Ingrese el cuarto numero: "))
    else:
        e = int(input("Ingrese por ultima vez un numero: "))
    contador += 1

#Suma de los numeros ingresados
    suma = a + b + c + d + e 

#Promedio de los numeros ingresados
    promedio = suma / 5

#Prints finales 
    print(f"La suma de los numeros ingresados es: {suma}")
    print(f"El promedio de los números ingresados es: {promedio}")