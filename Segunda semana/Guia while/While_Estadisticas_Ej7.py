#7 Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.
#!###########################################################################
suma =  0
cantidad = 0

while True :
    entrada = input("Ingrese un numero (o ingrese 'e' para salir): ")
    if entrada == 'e' or entrada == "E" :
        break

    numero = entrada 
    suma += numero
    cantidad += 1 
#!#############################################################################