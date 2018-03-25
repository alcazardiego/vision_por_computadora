import random
def adivinar(intentos):
    
    numero = random.randint(0, 100)
    cont = 0

    #print (numero)
    while(cont < intentos):
        num = input('Ingrese un numero a adivinar:')
        cont += 1
        if(int(num) == numero):
            
            print('ADIVINO!!!! en ' + str(cont))
            break




#programa principal
intento = input('Ingrese los intentos:')
adivinar(int(intento))
