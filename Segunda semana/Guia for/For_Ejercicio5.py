#5
# Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.

suma = 0
contador = 0 

for maximo in range(10):
    numero = int(input("Ingrese un numero o ingrese 0 para terminar: "))
    if numero == 0 :
        break
    suma += numero
    contador += 1

promedio = suma / contador
print(f"Ingresaste un total de {contador} numeros, el promedio es {promedio:.2f}")