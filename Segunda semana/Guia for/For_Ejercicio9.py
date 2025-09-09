#9
# Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.

divisores = 0
numero = int(input("Ingresa un numero: "))

for i in range(1, numero + 1):
    if numero % i == 0:    
        print(i)     
        divisores += 1         

print(f"Cantidad de divisores: {divisores}")


