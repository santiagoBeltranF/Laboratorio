import uuid
class Mascota:

    def __init__(self, nombre, edad, raza, precio):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.id = uuid.uuid4()
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}--{self.edad}--{self.raza}--{self.id}--{self.precio}"

    def __repr__(self):
        return str(self.id)

    def cumple(self, especificacion):
        dict_mascotas = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_mascotas or dict_mascotas[k] != especificacion.get_value(k):
                return False
        return True
