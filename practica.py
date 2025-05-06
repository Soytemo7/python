# CONFIGURAR POR PRIMERA VEZ GITHUB
# git config --global user.name "NOMBREGITHUB"
# git config --global user.name "EMAILGITHUB"

import random

def juego_adininanza():
    numero_secreto = random.randint(1,100)
    intentos=0
    adivinado = False

    print("Bienvenido al juego de adivinanza de numero")
    print("Debes adivinar un numero entre el 1 al 100")
    print("¡Intenta adivionarlo!")

    while not adivinado:
        adivinanza = input("Introduzca un numero del 1 al 100: ")
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"el numero secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"el numero secreto es menor a {adivinanza}")
            else:
                print(f"Felicidades, el numero {adivinanza} es el secreto y lo haz logrado en {intentos} intentos.")
                adivinado=True
        else:
            print("Introduzca un numero valido")                      

juego_adininanza()

