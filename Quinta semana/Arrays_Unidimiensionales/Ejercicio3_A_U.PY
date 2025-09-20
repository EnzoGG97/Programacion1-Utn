#Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. 
def pedir_numeros():
    lista = []
    vueltas = int(input("¿Cuantos numeros quiere ingresar?: "))
    for i in range(vueltas):
        numero = int(input(f"Ingrese el numero {i+1}: "))
        lista.append(numero)
    return lista

def calcular_promedio(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista) # sum suma todos los numeros de la lista y len se fija cuantos elementos hay, para despues dividir

numeros = pedir_numeros()
promedio = calcular_promedio(numeros)

print(f"El promedio de los numeros ingresados es: {promedio:.2f}")
