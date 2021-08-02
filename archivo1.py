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

#creacion de la clase hija profesor
class Profesor(Persona):
    def __init__(self, nombre, edad, titulo, aexp):
        super().__init__(nombre, edad)
        self.titulo=titulo
        self.aexp=aexp

    def getTitulo(self):
        return self.titulo

    def getAexp(self):
        return self.aexp

    def setTitulo(self, titulon):
        self.titulo=titulon

    def setAexp(self, aexpn):
        self.aexp=aexpn

