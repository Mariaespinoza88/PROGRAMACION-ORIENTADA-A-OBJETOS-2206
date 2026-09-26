"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de
las clases se definen los atributos (propiedades / caracteristicas) y los métodos 
(funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen 
a una clase, es decir para interacturar con la clase o clases y hacer uso de los
atributos y metodos es necesario crear un objeto o objetos.

Atributos de la clase Coches
marca, color, velocidad, potencia, numero de asientos

Metodos de la clase Coches 
acelerar, frenar, apagar, encender 

Que los atributos y metodos sean publicos
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y 
# apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

print("\033c")

class Coches:
    marca = ""
    color = "sin color"
    velocidad = 0 
    potencia = 0
    numero_asientos = 0

    def acelerar(self):
        self.velocidad +=1
        

    def frenar(self):
        pass

coche1 = Coches()

coche2 = Coches()

print("El color del coche 1 es: ", coche1.color) 
coche1.color

print("El color del coche 2 es: ", coche2.color)
coche2.color = "Azul"
print("El color del coche 2 es: ", coche2.color)

coche1.acelerar()
coche1.acelerar()
print("La velocidad del coche 1 es: ", coche1.velocidad)
