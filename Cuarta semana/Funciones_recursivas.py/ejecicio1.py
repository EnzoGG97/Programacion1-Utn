def sumar_naturales(numero:int) ->int:
    if numero ==1:
        return numero
    else:
        return numero + sumar_naturales(numero - 1) # Llamada recursiva

print(sumar_naturales(6)) #(1+2+3+4+5+6)