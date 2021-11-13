MIN = 0
MAX = 99

while True:
    nivel = input("Introduce un nivel: simple, intermedio, avanzado, experto, o Stephen Curry:  ")
    if nivel == "simple":
        MAX = 100
        break
    elif nivel == "intermedio":
        MAX = 1000
        break
    elif nivel == "avanzado":
        MAX = 1000000
        break
    elif nivel == "experto":
        MAX = 1000000000000
        break
    elif nivel == "Stephen Curry":
        MAX = 10000000000000000000000000000000000000000000000
        print("SUERTE CON LOS TRIPLES")
        break
    else:
        print("Como no has elegido te pongo el fácil pesao")
        break

minimo = MIN
maximo = MAX

def pedir_numero(invitacion, minimo, maximo):
    invitacion += " entre " + str(minimo) + " y " + str(maximo) + ": "
    while True:
        entrada = input(invitacion)
        try:
            entrada = int(entrada)
        except:
            pass
        else:
            if minimo <= entrada <= maximo:
                break
    return entrada

import random
numero = random.randint(0,100)
contador = 1

print("Intente adivinar el numero:")
while True:
    intento = pedir_numero("Adivine el numero", minimo, maximo,)
    if intento < numero:
        print("Demasiado pequeñito :(")
        minimo = intento + 1
        contador = contador + 1
        if contador > (maximo/10):
            print("TE HAS PASADO DEL NUMERO DE INTENTOS")
            break
    elif intento > numero:
        print("Demasiado grande")
        maximo = intento - 1
        contador = contador + 1
        if contador > (maximo/10):
            print("TE HAS PASADO DEL NUMERO DE INTENTOS")
            break
    else:
        print("MUY BIEN")
        contador = contador + 1
        break

print("has usado ", contador , "intentos")