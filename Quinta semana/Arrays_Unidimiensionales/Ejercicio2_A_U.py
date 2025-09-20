#Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.


from Ejercicio1_A_U import crear_array
from Ejercicio1_A_U import numero

cantidad = int(input("Ingrese cuantos numeros quiere ingresar: "))
elementos = crear_array(cantidad)

print("Nuevos parametros: ", elementos)
print(numero + elementos)