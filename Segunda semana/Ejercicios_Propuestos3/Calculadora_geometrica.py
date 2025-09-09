'''
Calculadora geométrica
Crear un programa que permita al usuario elegir una figura geométrica (cuadrado, rectángulo, triángulo, círculo) mediante un menú. Luego, calcular su área y perímetro usando funciones específicas para cada caso.
'''
import math

def calcular_cuadrado (lado):
    area = lado * lado
    perimetro = lado * 4
    return area, perimetro

def calcular_cuadrado (altura, lado):
    area = lado * altura
    perimetro = (lado + altura) * 2
    return area, perimetro
def calcular_triangulo (base, altura):
    area = (base * altura) / 2
    perimetro = base * 3  # Asumiendo un triángulo equilátero
    return area, perimetro  
def calcular_circulo (radio):
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    return area, perimetro

def menu():
    print("Calculadora Geométrica")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Triángulo")
    print("4. Círculo")
    print("5. Salir")   

    opcion = int(input("Elige una figura geométrica (1-5): "))
    return opcion   
while True:
    opcion = menu()
    
    if opcion == 1:
        lado = float(input("Ingrese el lado del cuadrado: "))
        area, perimetro = calcular_cuadrado(lado)
        print(f"Área del cuadrado: {area}, Perímetro del cuadrado: {perimetro}")
        
    elif opcion == 2:
        altura = float(input("Ingrese la altura del rectángulo: "))
        lado = float(input("Ingrese el lado del rectángulo: "))
        area, perimetro = calcular_cuadrado(altura, lado)
        print(f"Área del rectángulo: {area}, Perímetro del rectángulo: {perimetro}")
        
    elif opcion == 3:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area, perimetro = calcular_triangulo(base, altura)
        print(f"Área del triángulo: {area}, Perímetro del triángulo (asumiendo equilátero): {perimetro}")
        
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        area, perimetro = calcular_circulo(radio)
        print(f"Área del círculo: {area}, Perímetro del círculo: {perimetro}")
        
    elif opcion == 5:
        print("Saliendo de la calculadora geométrica.")
        break
        
    else:
        print("Opción no válida. Por favor, elige una opción entre 1 y 5.")
    
    print()  # Línea en blanco para mejor legibilidad   