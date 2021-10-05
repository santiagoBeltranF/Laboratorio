import  uuid
from Dominio.mascota import Mascota

class Tortuga (Mascota):

    def __init__(self, nombre, edad, raza, precio,tipoSangre):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.codigoRep = uuid.uuid4()
        self.precio = precio
        self.tipoSangre=tipoSangre

    def __str__(self):
        return f"{self.nombre}--{self.edad}--{self.raza}--{self.tipoSangre}--{self.codigoRep}--{self.precio}"

    def __repr__(self):
        return str(self.codigoRep)

    def cumple_Tortuga(self, especificacion):
        dict_reptil = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_reptil or dict_reptil[k] != especificacion.get_value(k):
                return False
        return True
