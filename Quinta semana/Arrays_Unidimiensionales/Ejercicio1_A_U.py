#Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.

def crear_array(cantidad):
    array = []
    for i in range(cantidad):
        n = int(input(f"Ingrese un numero:{i+1}  "))
        array.append(n)
    return array

cantidad_elementos = int(input("cuantos numero queres ingresar? : "))
numero = crear_array(cantidad_elementos)

print("Array de: ",numero)