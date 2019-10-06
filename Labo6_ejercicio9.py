"""Hacer un programa que dado un rango de números (por ejemplo de 10 hasta 100) y 
muestre todos los números que son múltiplo de x número en
 ese rango (por ejemplo los múltiplos de 3)"""

flag = 0
while(flag == 0):
    try:
        limInferior = int(input("Ingresa el lim inferior del rango: "))
        limSuperior =  int(input("Ingresa el lim superior del rango: "))
        multiplo = int(input("Ingresa el múltiplo a evaluar: "))
        for i in range (limInferior, limSuperior+1):
            if(i % multiplo == 0):
                print("Es múltiplo de "+ str(multiplo) +": "+ str(i) )
        flag = 1   
    except ValueError:
        print("Tienes que meter un número, intentalo de nuevo")
