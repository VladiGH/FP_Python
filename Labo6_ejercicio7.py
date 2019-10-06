#Hacer un programa que dibuje un cuadrilátero de longitud n asteriscos.

flag = 0
while(flag == 0):
    try:
        num = int (input("Ingresa la longitud del cuadrilátero: "))
        for i in range (1, num + 1):
            print ( ("*"+" ") * num )
        flag = 1   
    except ValueError:
        print("Tienes que meter un número, intentalo de nuevo")