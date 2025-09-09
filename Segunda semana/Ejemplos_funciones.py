# Funcion basica sin parametros

# Funcion simple sin parametros
def saludar():
    print("Hola, bienvenido a la programacion en Python!")
    
# Funcion con 1 parametro
def saludar_param(nombre):
    print(f"Hola, {nombre}, bienvenido a la programacion en Python!")
    
#Funcion que retorna un valor
def sumar(a, b):
    return a + b

#Funcion con valor por defecto    
def presentar(nombre, edad=30):
    print(f"Me llamo {nombre} y tengo {edad} años.")
    
#Funcion que retorna varios valores
def operaciones(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    return suma, resta
    
#Funcion con *args lo toma como una lista dependiendo la cantidad que se pasen
def sumar_varios(*args):
    resu = 0
    for x in args:
        resu = x + resu
    return resu

#Funcio dentro de una funcion
def funcion_externa():
    print("Esta es la funcion externa.")
    
    def funcion_interna():
        print("Esta es la funcion interna.")
    
    funcion_interna()


# ========================================================= 
# Llamada a la funcion
# saludar()
# saludar_param("Juan")

# resultado = sumar(3, 5)
# print(f"La suma es: {resultado}")

# presentar("Emanuel", 25)
# presentar("Ana")

# suma, resta = operaciones(10, 4)
# print(f"Suma: {suma}, Resta: {resta}")

# print(sumar_varios(1, 2, 3, 4, 5))
# print(sumar_varios(10, 20, 50, 3.3))

# funcion_externa()
# funcion_interna() es un funcion local y no se puede llamar desde aqui