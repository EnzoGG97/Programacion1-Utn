import math

def cuadrado(lado:float) -> float: 
    """ return: (area, perimetro) """
    return lado**2, lado * 4


def rectangulo(base: float, altura: float) -> float: 
    """ return: (area, perimetro) """
    return base * altura, 2 * (base  +  altura)


def triangulo(base : float, altura : float) -> float:
    """ return: (area, perimetro) """
    area = (base * altura) / 2 
    perimetro = base + altura + math.sqrt(base**2 + altura**2)
    return area, perimetro
    

def circulo(radio: float) -> float:
    """ return: (area, perimetro) """
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio 
    return area, perimetro

figura_geometrica = input("que figura desea saber su area y perimetro?: ").lower()
match figura_geometrica:
    case "rectangulo":
        base = float(input("ingrese la base del rectangulo: "))
        altura = float(input("ingrese la altura del rectangulo: "))
        area, perimetro = rectangulo(base, altura)
    case "cuadrado":
        lado = float(input("ingrese un lado del rectangulo"))
        area, perimetro = cuadrado(lado)
    case "triangulo":
        base = input("Ingrese la base del triangulo: ")
        altura = input("Ingrese la altura: ")
        area, perimetro = triangulo(base, altura)
    case "circulo":
        radio = float(input("ingrese un radio del rectangulo"))
        area, perimetro = circulo(radio)

print(f"del {figura_geometrica} el es {area} y su perimetro es {perimetro}")