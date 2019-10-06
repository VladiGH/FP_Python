numero_ingresado = (input("Ingrese un número: "))
revertir = 0
valor = int(numero_ingresado)
while valor > 0:
    residuo = valor % 10
    revertir = (revertir * 10) + residuo
    #Division con floor, siempre va a omitir los decimales del resultado de una division 
    valor //= 10
print('El inverso del número ingresado es: ', revertir)