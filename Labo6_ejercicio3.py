"""
Escriba un programa que pida números pares mientras 
el usuario indique que quiere seguir introduciendo números. Para indicar que quiere 
seguir escribiendo números, el usuario deberá contestar S o N a la pregunta.
"""
def esPar (num):
    if num % 2 == 0:
        return True
    else:
        return False

question = 'S'
while(question == 'S' or question == 's'):
    try:
        num = int(input("Ingrese un número par: "))
        if(esPar(num) == True):
            question = input("¿Quieres escribir otro número par? S/N ")
        else:
            print("El número ingresado no es un número par.")
            question = 's'
    except ValueError:
        print("Tienes que meter un número, intentalo de nuevo")