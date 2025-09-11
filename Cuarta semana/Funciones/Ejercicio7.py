#Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.

def numero(numero_t_f):
    if numero_t_f % 2 == 0:
        return True
    else:
        return False
num = int(input("Ingrese un numero: "))
numero(num)
