# Juego del número secreto
# Generar un número aleatorio entre 1 y 100. El usuario debe adivinarlo. El programa debe dar pistas ("más alto", "más bajo") hasta que acierte. Llevar un contador de intentos y mostrarlo al final.
import random
def juego_numero_secreto():
    numero_secreto = random.randint(1,100)
    intentos = 0
    adivinado = False

    print("Existe un numero secreto, ¿podes adivinar cual es?")

    while not adivinado :
        intento = int(input("Introduce un numero: "))
        intentos += 1
        
        if intento < numero_secreto:
            print("¡Mas alto!")
        elif intento > numero_secreto:
            print("¡Mas bajo!")
        else:
            adivinado = True
            print(f"Felicitaciones, adivinaste el numero {numero_secreto} en {intentos} intentos.")
juego_numero_secreto()