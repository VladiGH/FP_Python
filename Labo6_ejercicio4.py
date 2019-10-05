from random import * 

x=randrange(0,10)
contador = 0
y=12

while x!=y:
    print("Digite un numero entre 0 y 10: ")
    y=int(input())

    if y>x:
        print("Ingrese numero menor")
    elif y<x:
        print("Ingrese numero mayor")
    contador+=1
print("FELICIDADES GANASTE! ")    
print("Tu numero de intentos fue: "+ str(contador))
    


