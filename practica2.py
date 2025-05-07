 
import random


def obtener_palabra_secreta() -> str:
    palabras = ['python','javascript','angular','django','tensorflow','git']
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta,letras_adivinadas):
    adivinado = ''
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    
    return adivinado

def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False
    
    print('Bienvenido al juego del ahorcado')
    print(f'Tienes {intentos} intentos para adivinar la palabra secreta')
    print(mostrar_progreso(palabra_secreta,letras_adivinadas))

    while not juego_terminado and intentos>0:
        adivinanza = input("Introduce una letra :").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Escriba una letra")
        elif adivinanza in letras_adivinadas:
            print("Ya haz utilizado la letra")
        else:
            letras_adivinadas.append(adivinanza)
            if adivinanza in palabra_secreta:
                print(f"Haz acertado... la letra {adivinanza} esta presente en la palabra")
            else:
                intentos -= 1
                print(f"La letra no esta presente {adivinanza}, ")
                print(f"Te quedan {intentos} intentos")
        
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado=True
            print(f"Felicidades, la palabra completa es: {palabra_secreta}")
        
    if intentos == 0:
        print(f"Se acabron los intentos, la palabra era {palabra_secreta}")

juego_ahorcado()

