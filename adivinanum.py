import random

def aleatorios(inferior,superior):
    numeros=random.randint(inferior,superior)
    
    return numeros


if __name__=="__main__":
    print('Escoge un numero bajo y luego un numero mas alto, e intenta adivinar de entre ese rango cual escogere yo')
    inferior=int(input('numero inferior> '))
    superior=int(input('numero superior> '))
    jugada=aleatorios(inferior, superior)
    
    while True:
        #print(f'esto devulve {jugada}')
        jugador=int(input('Que numero crees elegí? Escribe tu respuesta> '))
        if jugada==jugador:
            print('GANASTE!! ACASO LEES LA MENTE?')
            break
        elif jugador>superior:
            print(f'OH, Ese numero no esta en el rago solo puedes llegar entre {inferior} y {superior}')
        elif jugador<inferior:
            print(f'Este numero es mas bajo del rango elegido solo debe ser un numero entre {inferior} y {superior}')
        elif jugada<jugador:
            print('Bajale unos numeritos más, vuelve intententar')
        elif jugada>jugador:
            print('Subele unos numeritos ya casi, intenta de nuevo')
        

    