from archivo1 import *
#creacion de la clase hija
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario=salario

    #creacion de los metodos get y set
    def getSalario(self):
        return self.salario

    def setSalario(self, salarion):
        self.salario=salarion

#creacion de una clase hija (Estudiante)
class Estudiante(Persona):
    def __init__(self, nombre, edad, correo=None, telefono=None):
        super().__init__(nombre, edad)
        self.correo=str(input("Ingrese su correro electrónico: "))
        self.telefono=str(input("Ingrese su número de teléfono: "))

    #Metodos set y get
    def getCodigo(self):
        return self.correo

    def getTelefono(self):
        return self.telefono

    def setCodigo(self, correon):
        self.correo=correon

    def setTelefono(self, telefonon):
        self.telefono=telefonon
        

#creacion de los objetos
oPersona=Persona("Juan", 19)
oEmpleado=Empleado("Mery", 25, 500)
oEstudiante=Estudiante("Marco", 14)

print(oPersona.getEdad())
print(oEmpleado.getSalario())
