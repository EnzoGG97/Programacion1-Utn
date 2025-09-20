import random
from Input import get_int

#1=piedra
#2=papel
#3=tijera


print("Bienvenido a Piedra-Papel-Tijeras")
print("")
print("Piedra aplasta Tijera → 🏆 Gana la Piedra")
print("Tijera corta Papel → 🏆 Gana la Tijera")
print("Papel envuelve Piedra → 🏆 Gana el Papel")
print("Si ambos jugadores eligen el mismo elemento, la ronda termina en empate.")

def verificar_ganador_ronda(jugador: int,maquina: int) -> str:
    if jugador == maquina :
        return "Empate"
    elif (jugador == 1 and maquina == 3) or (jugador == 2 and maquina == 1) or (jugador == 3 and maquina == 2):
        return "Gana el jugador"
    return "Gana la maquina"


def verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual) -> bool:
    pass


def verificar_ganador_partida(aciertos_jugador, aciertos_maquina) -> str:
    pass


def mostrar_elemento(eleccion) -> str:
    pass

def jugar_piedra_papel_tijera() -> str:
    aciertos_jugador = 0
    aciertos_maquina = 0
    ronda_actual = 0

    pass


print(random.randint(1,3))