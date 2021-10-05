import uuid
from Dominio.mascota import Mascota
class Ave(Mascota):

    def __init__(self, nombre, edad, raza, precio,tipoPlumas):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.codigoAv= uuid.uuid4()
        self.precio = precio
        self.tipoPlumas = tipoPlumas

    def __str__(self):
        return f"{self.nombre}--{self.edad}--{self.raza}--{self.tipoPlumas}--{self.codigoAv}--{self.precio}"

    def __repr__(self):
        return str(self.codigoAv)

    def cumple_Ave(self, especificacion):
        dict_ave = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_ave or dict_ave[k] != especificacion.get_value(k):
                return False
        return True
