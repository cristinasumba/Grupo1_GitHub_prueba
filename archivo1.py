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

#creacion de los objetos
oPersona2=Persona("Alison", 19)

print (oPersona2.getNombre())
oPersona2.setNombre("Shirley")

print (oPersona2.getNombre())


