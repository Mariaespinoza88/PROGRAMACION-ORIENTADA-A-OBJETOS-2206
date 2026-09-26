"""
Ejercicio Practico #2 “Modelar y Diagramar en POO”

"""
print("\033c")

#Clase de Coches
class Coches:
    #Atributos de la clase Coches
    def __init__(self, marca, color, velocidad):  
        self.marca = marca
        self.color = color
        self.__velocidad = velocidad

    #Metodos de la clase Coches
    def acelerar(self):
        self.velocidad +=1
        return self.velocidad

    def frenar(self):
        self.velocidad -=1
        return self.velocidad

    def tocar_claxon(self):
        print("Beep Beep!")
        return "Beep Beep!"

coche1=Coches("Toyota", "Rojo", 0)
coche2=Coches("Honda", "Azul", 0)

#print("El color del coche es", coche1.color) 
#no se puede usar metodos privados fuera de la clase

print("El coche 1 con el claxon hace, ", coche1.tocar_claxon())
print("El coche 2 con el claxon hace, ")
coche2.tocar_claxon()

coche1.acelerar()
print("El coche 1 acelera y su velocidad es de: ", coche1._Cochesvelocidad)



#Instanciar o crear objetos de la clase Coches

#el guion bajo va antes del atributo 
#los metodos privados no se pueden usar fuera de la clase
#los atributos d una clase son publicos y se pueden usar fuera de la clase
#get y set son metodos que se usan para acceder a los atributos de una clase


