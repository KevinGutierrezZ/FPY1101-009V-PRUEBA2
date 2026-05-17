#Ejercicio prueba parcial2

from random import randint

#Flag para asegurar que el primer numero sea menor
#Try para asegurar que no se usen letras
flag_numero = True
while flag_numero == True:
    try:
        num1 = int(input("Ingrese su primero numero: "))
        num2 = int(input("Ingrese su segundo numero: ")) 
        if num1 < num2:
            numero = randint(num1, num2)
            flag_numero = False
        else:
            print ("El primer numero debe ser menor que el segundo")
    except:
        print ("Debe ingresar un numero entero.")

#Convirtiendo en numero par
if numero % 2 != 0:
    numero += 1
    if numero > num2:
        numero -= 2

#While para acierto

while True:

#Simulando juego
#Intento 1
    intento1 = int(input("Intento 1: Debe adivinar el numero: "))
    if intento1 < num1 or intento1 > num2:
        print ("Intento Fallido! El numero debe estar entre el primero y el segundo")
    elif intento1 == numero:
        print ("Felicidades! has acertado en tu primer intento!")
        break
    elif intento1 < numero:
        print ("El numero es mayor")
    else:
        print ("El numero es menor")

    #Intento 2
    intento2 = int(input("Intento 2: Debe adivinar el numero: "))
    if intento2 < num1 or intento2 > num2:
        print ("Intento Fallido! El numero debe estar entre el primero y el segundo")
    elif intento2 == numero:
        print ("Felicidades! has acertado en tu segundo intento!")
        break
    elif intento2 < numero:
        print ("El numero es mayor")
    else:
        print ("El numero es menor")

    #Pista para saber cual intento estuvo mas cerca
    distancia1 = abs(numero - intento1)
    distancia2 = abs(numero - intento2)
    if distancia1 < distancia2:
        print(f"El numero que buscas esta mas cerca de {intento1} que de {intento2}")
    else:
        print(f"El numero que buscas esta mas cerca de {intento2} que de {intento1}")

    #Intento 3
    intento3 = int(input("Intento final: Debe adivinar el numero: "))
    if intento3 != numero:
        print (f"Perdiste! el numero correcto era {numero}")
        break
    else:
        print ("Felicidades! has acertado en tu ultimo intento!")
        break

