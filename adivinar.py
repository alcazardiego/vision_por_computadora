# PRACTICA 1
#
#Crear una funcion "adivinar" que permita adivinar un numero generado en forma aleatoria
#-el numero debe estar entre 0 y 100
#-el numero se genera dentro de la funcion
#-la funcion debe recibir un parametro que sea la cantidad de intentos, y en caso de que esta cantidad de intentos sea superada, el programa debe terminar con un mensaje
#-si el usuario adivina antes de superar el numero de intentos maximos, se debe imprimir un mensaje con el numero de intentos en los que adivino
#-crear la funcion y llamarla en el mismo archivo
#
#

import random
def adivinar(intentos): #se define la funcion
    
    numero = random.randint(0, 100) #se genera un numero entre 0 y 100
    cont = 0 #contador de intentos a adivinar

    #print (numero) #imprimo el numero aleatorio para comprobar funcionamiento del programa
    while(cont < intentos): #se ejecuta mientras el contador de intentos sea menor a los intentos elegidos
        num = input('Ingrese un numero a adivinar:') #se guarda por teclado el numero a adivinar
        cont += 1 #se incrementa el contador de intentos
        if(int(num) == numero): #pregunto si el numero ingresado es igual al numero aleatorio obtenido
            print('ADIVINO!!!! en intento ' + str(cont))
            break
        if(cont == intentos): #si el contador de intentos es igual al numero de intentos, NO se adivino el numero
            print('NO ADIVINO!!! SUERTE LA PRÓXIMA VEZ....')
            break



#programa principal
intento = input('Ingrese los intentos:')
adivinar(int(intento))
