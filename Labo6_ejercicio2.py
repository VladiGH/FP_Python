"""2.  Realice un programa que dibuje una pirámide numérica de acuerdo al 
número de filas ingresado. Validaciones las entradas de la manera que 
considere necesaria.
"""


num = int(input("Ingresa la cantidad de filas: "))

for i in range (1, num+1):
    print(str(str(i)*i))