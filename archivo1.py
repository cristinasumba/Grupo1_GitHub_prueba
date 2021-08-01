class Persona ():
    def __init__(self, nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
        #creacion de los metodos get y set
    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def setNombre(self, nombren):
        self.nombre=nombren

