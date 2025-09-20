#from Validate import validate_numero, validate_longitud

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|None:
    # Mientras queden reintentos
    while reintentos > 0:
        try:
            # Pedir el valor mostrando el mensaje recibido por parametro
            valor = int(input(mensaje))
            # Validar el rango
            if minimo <= valor <= maximo:
                return valor
            else:
                print(mensaje_error)
        except ValueError:
            print(mensaje_error)
        # Restar un intento si hubo error
        reintentos -= 1
    # Si no se consiguió un valor valido, retornar None
    return None


def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: float) -> float|None:
    while reintentos > 0 : 
        try :
            valor = float(input("Ingresa un valor:"))
            if minimo <= valor <= maximo :
                return valor
            else :
                print(mensaje_error)
        except ValueError:
            print(mensaje_error)
        reintentos -= 1
    return None

def get_string(longitud: int) -> str|None:
    while reintentos > 0 : # Siempre que la cantidad de intentos sea mayor a 0 se hace el bucle
        cadena = input(f"Ingrese una cadena de texo con {longitud} caracteres: ") # Pide una cadena de texto 
        if len(cadena) == longitud : # Verifica con la funcion "len" que la cantidad de caracteres de la cadena sea la misma que longitud 
            return cadena # Si es correcto retona la cadena
        else:
            print("Error, ingrese una cadena con {longitud} caracteres")
            reintentos -= 1 # Si no es correcta, tira un mensaje marcando el error y resta un intento
    return None # Cuando se terminan los intentos, retorna none



