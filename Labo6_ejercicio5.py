saldoInicial=1000
saldo=0
retiro=0
print("Bienvenidos a su cajero virtual :O")
print("1-Ingrese dinero en la cuenta")
print("2-Retirar dinero de la cuenta")
print("3-Salir")
print("Opcion: ")
opcion=int(input())

if opcion==1:
    print("Digite la cantidad de dinero a ingresar: ")
    dinero=int(input())
    saldo=saldoInicial+dinero
    print("Dinero en cuenta: "+str(saldo))
elif opcion==2:
    print("Digiter la cantidad a retirar: ")
    retiro=int(input())
    if retiro > saldoInicial:
        print("Fondos insuficientes")
    else:
        saldo=saldoInicial-retiro
        print("Tu saldo es de: "+str(saldo))




