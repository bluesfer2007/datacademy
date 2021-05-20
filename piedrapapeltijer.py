import random

#piedra papel o tijera
  
def jugada():
    opciones=['piedra', 'papel', 'tijera']
    valor=random.choice(opciones)
    return valor
def resul(resultados):
    if resultados.count('Ganador')>1:
        print('GANASTE UNA CEBOLLA DE HORA')
    elif resultados.count('Empate')==3:
        print('ES UN EMPATE WOW')
    else:
        print('PERDISTE LA CEBOLLA DE HORA')


if __name__=='__main__':
    intentos=0
    resultados=[]
    while intentos<3:
        intentos+=1
        jugador=input('valor1> ').lower()
        maquina=jugada()
        if jugador==maquina:
            print(f'tu contricante {maquina}')
            resultados.append('Empate')
        elif jugador=='piedra' and maquina=='papel':
            print(f'tu contricante {maquina}')
            resultados.append('Pierdes')
        elif jugador=='piedra' and maquina=='tijera':
            print(f'tu contricante {maquina}')
            resultados.append('Ganador')
        elif jugador=='papel' and maquina=='piedra':
            print(f'tu contricante {maquina}')
            resultados.append('Ganador')
        elif jugador=='papel' and maquina=='tijera':
            print(f'tu contricante {maquina}')
            resultados.append('Pierdes')
        elif jugador=='tijera' and maquina=='piedra':
            print(f'tu contricante {maquina}')
            resultados.append('Pierdes')
        elif jugador=='tijera' and maquina=='papel':
            print(f'tu contricante {maquina}')
            resultados.append('Ganador')
    resul(resultados)