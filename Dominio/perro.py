import uuid


class Perro :

    def __init__(self, nombre, edad, raza, precio,colorPelage):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.codigoPer = uuid.uuid4()
        self.precio = precio
        self.colorPelage=colorPelage

    def __str__(self):
        return f"{self.nombre}--{self.edad}--{self.raza}--{self.colorPelage}--{self.codigoPer}--{self.precio}"

    def __repr__(self):
        return str(self.codigoPer)

    def cumple_perro(self, especificacion):
        dict_perro = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_perro or dict_perro[k] != especificacion.get_value(k):
                return False
        return True