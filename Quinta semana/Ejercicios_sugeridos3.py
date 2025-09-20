#Contar cuántas veces aparece el número 3 en una lista.
import random

lista_numeros = []
for i in range(10):
    num_random = random.randint(1,5)
    lista_numeros.append(num_random)
print("lista creada: " ,lista_numeros)
apareciones = lista_numeros.count(3)
print("apariciones del 3: " , apareciones)