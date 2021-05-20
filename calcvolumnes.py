import math

def volcilindro(radio, altura):
    #variables esperadas: radio, altura
    #area de base
    ab=math.pi*math.pow(radio,2)
    #volumen= area de base * altura
    v=ab*altura
    return v
def volcubo(lado):
    volumen=math.pow(lado,3)
    return volumen



if __name__=='__main__':
    print('Hola a continuacion selecciona el calculo que requieres \n [1] Volumen de cilindro \n [2] Volumen de un cubo \n [3] Salir')
    
    while True:
        opcion=int(input('ingresa el numero 1 o 2 o salir 3> '))
        if opcion==1:
            radio=int(input('Ingresa el valor del radio> '))
            altura=int(input('Ingresa la altura del cilindro> '))
            volumen=volcilindro(radio, altura)
            print(f'El volumen del cilindro es {volumen} cm3')
        elif opcion==2:
            lado=int(input('Ingresa el valor de un lado del cubo> '))
            volumen=volcubo(lado)
            print(f'el valor del volumen del cubo es {volumen} cm3')
        else:
            break


    