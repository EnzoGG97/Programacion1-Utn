def pedir_notas():
    notas = []
    for i in range(3):
        while True:
            n = float(input(f"Introduzca la nota {i+1}: "))
            if 0 <= n <= 10:
                notas.append(n)
                break
            else:
                print("Introduzca una nota valida de 0 a 10")
    return notas


def calcular_promedio(notas):
    return sum(notas) / len(notas)

def mostrar_resultado(nombre, promedio):
    if promedio >= 6:
        print(f"El alumno {nombre} ha aprobado con un promedio de {promedio:.2f}")
    else:
        print(f"El alumno {nombre} ha desaprobado con un promedio de {promedio:.2f}")

nombre = input("Introduzca el nombre del alumno: ")
notas = pedir_notas()


promedio = calcular_promedio(notas)
mostrar_resultado(nombre, promedio)
resultados = {nombre: promedio}

print("Diccionario de resultados:", resultados)

#3. Gestor de notas de alumnos El programa debe pedir el nombre de un alumno y sus 3 notas. Usando una función, calcular el promedio y mostrar si aprobó o desaprobó (mínimo 6). Guardar los resultados en un diccionario {nombre: promedio}.