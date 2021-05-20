import pandas as pd
import numpy as np
import math
import random


#definir classe triangulo
class Triangulo:
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
        
    def area(self):
        base=self.base
        altura=self.altura
        area=(base*altura)/2
        return area
    
    def perimetro(self,area):
        lado1=self.base
        lado2=np.round(math.sqrt(area),2)
        hip=np.round(math.sqrt(math.pow(lado1,2)-math.pow(lado2,2)),2)
        return lado1, lado2, hip
    
    def main(self):
        area=self.area()
        perimetro=self.perimetro(area)
        if perimetro[0]==perimetro[1] and perimetro[2]==0:
            print(f'Su área es de {area}m2 y es un Triángulo Equilátero')
        elif perimetro[1]==perimetro[2]:
            print(f'Su área es de {area}m2 y es un Triángulo Isósceles')
        else:
            print(f'Su área es de {area}m2 y es un Triángulo escaleno')
if __name__=='__main__':
    triangulo1=Triangulo(12,15)
    area=triangulo1.area()
    lados=triangulo1.perimetro(area)
    triangulo1.main()   