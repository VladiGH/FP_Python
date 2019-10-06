def FarenheitACelcius():
    print("Bienvenido al conversor de Celcuis a farenheit")
    faren=int(input("ingrese temperatura a convertir"))
    celcius=(faren - 32) * 5.0/9.0
    print("La temperatura en celcius es de: "+str(celcius))
def CelciusAFarenheit():
    print("Bienvenido al conversor de Farenheit a celsius")
    celci=int(input("Ingrese temperatura en farenheit: "))
    Faren=(celci * 9/5) + 32
    print("La temperatura es de: "+str(Faren))


def kelvinACelcius():
    print("Bienvenido al conversor de Kelvin a celsius")
    kelvin=int(input("Ingrese temperatura en kelvin: "))
    celi=kelvin-272
    print("La temperatura es de: "+str(celi))

    



x=0
while x!=4:
    print("1-------Convertir Farenheit a celcius")
    print("2-------Convertir Celcius a farenheit")
    print("3-------Convertir Kelvin a celcius")
    print("4-------Salir")
    x=int(input("Selecciona una opcion: "))

    if x==1:
        FarenheitACelcius()
    elif x==2:
        CelciusAFarenheit()
    elif x==3:
        kelvinACelcius()
    
    
    