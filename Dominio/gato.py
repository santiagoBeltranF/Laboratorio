import uuid
from Dominio.mascota import Mascota

class Gato(Mascota):

    def __init__(self, nombre,edad, raza, precio, pelage):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.codigoGat = uuid.uuid4()
        self.precio = precio
        self.pelage = pelage


    def __str__(self):
        return f"{self.nombre}--{self.edad}--{self.raza}--{self.pelage}--{self.codigoGat}--{self.precio}"

    def __repr__(self):
        return str(self.codigoGat)

    def cumple_Gato(self, especificacion):
        dict_gato = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_gato or dict_gato[k] != especificacion.get_value(k):
                return False
        return True