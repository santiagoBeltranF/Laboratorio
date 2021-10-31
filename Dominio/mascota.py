import uuid
class Mascota:

    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria
        self.id = uuid.uuid4()


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
