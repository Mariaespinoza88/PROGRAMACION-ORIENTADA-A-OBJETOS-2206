"""
 Practica # 1 Implementar ejercicio el paradigma estructurado VS OO

 Elaborar un programa que calcule el area de un rectangulo
"""

print("\033c")

#Implementar el paradigma estructurado




#Implementar el paradigma Orientado a Objetos (OO)

def area_rectangulo(base, altura):
    return base * altura
print(area_rectangulo(5, 3))


class Rectangulo: 
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
rect=Rectangulo(5, 6)
print(rect.area())
    
 
class Rectangulos:
    def area(self,base, altura):
        area = base * altura
        return area
    
rectangulo1= Rectangulos()
print (f"El rectangulo es: {rectangulo1.area(5, 6)}")




