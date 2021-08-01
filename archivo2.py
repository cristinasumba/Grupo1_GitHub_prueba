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
