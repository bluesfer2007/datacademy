def conversor(valor,opcion):
    factor=1.609344
    try:
        if opcion==1:
            print(f'{valor} millas son', valor*factor, 'kilometros')
        elif opcion==2:
            print(f'{valor} km son ', valor/factor, 'millas')
    except: print('debes ingresar un valor numerico')

if __name__=='__main__':

    print('Bienvenido al conversor de millas a kilometros')    
        
    while True:
        print('Escoge una opcion \n [1] millas a km \n [2] km a millas \n [3] salir') 
        opcion=int(input('Escoge la opción 1 o 2> '))       
        if opcion not in [1,2]:
            print('Gracias por usar el conversor')
            break
        else:
            valor=int(input('Ingresa el valor a convertir> '))            
            conversor(valor, opcion)