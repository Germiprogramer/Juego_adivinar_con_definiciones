MIN = 0
MAX = 99

while True:
    nivel = input("Introduce un nivel: simple, intermedio, avanzado, experto, o Stephen Curry:  ")
    if nivel == "simple":
        MAX = 100
        numero_intentos = 15
        break
    elif nivel == "intermedio":
        MAX = 1000
        numero_intentos = 55
        break
    elif nivel == "avanzado":
        MAX = 1000000
        numero_intentos = 105
        break
    elif nivel == "experto":
        MAX = 1000000000000
        numero_intentos = 155
        break
    elif nivel == "Stephen Curry":
        MAX = 10000000000000000000000000000000000000000000000
        numero_intentos = 100000000000000000
        print("SUERTE CON LOS TRIPLES")
        break
    else:
        print("Como no has elegido te pongo el fácil pesao")
        break

def help():
    ayuda = input(print("¿Quieres una ayudita ;)? (Para ayudita pulse 1)"))
    try:
        if ayuda == "1":
            print("Lo sentimos todavía no sabemos programar eso pero quería demostrarle a mi profe que entiendo funciones")
        else:
            print("pues nada...")
    except:
        pass
    return ayuda

help()

minimo = MIN
maximo = MAX
import random
numero = random.randint(minimo,maximo)

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

contador = 1

while True:
    intento = pedir_numero("Adivine el numero", minimo, maximo,)
    if intento < numero:
        print("Demasiado pequeñito :(")
        minimo = intento + 1
        contador = contador + 1
        if contador > numero_intentos:
            print("TE HAS PASADO DEL NUMERO DE INTENTOS")
            break
    elif intento > numero:
        print("Demasiado grande")
        maximo = intento - 1
        contador = contador + 1
        if contador > numero_intentos:
            print("TE HAS PASADO DEL NUMERO DE INTENTOS")
            break
    else:
        print("MUY BIEN")
        contador = contador + 1
        break

print("has usado ", contador , "intentos")