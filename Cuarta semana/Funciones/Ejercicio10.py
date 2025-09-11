#Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
def primo(num):
    if num < 1:
        return False
    for i in range(2, num):
        if num % i == 0 :
            return False
    return True
num = int(input("Ingrese un numero"))
prim = primo(num)
print(f"El numero {num} es primo? {prim}")

