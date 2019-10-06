"""Hacer un programa que dado un entero n, haga su tabla de multiplicar."""

flag = 0
while(flag == 0):
    try:
        n = int (input("Ingresa el número del cual quieres la tabla de multiplicar: "))
        if (n < 0):
            print ("Tu número es negativo, se aplicará valor absoluto.")
            n *= -1
        print("Tabla de multiplicar del número "+str(n))
        for i in range (1, 11):
            print ( str (n) + " * " + str(i) + " = " +str(n * i) )
        flag = 1   
    except ValueError:
        print("Tienes que meter un número, intentalo de nuevo")