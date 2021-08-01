from archivo1 import *
#creacion de la clase hija
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario=salario
