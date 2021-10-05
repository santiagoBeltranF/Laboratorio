class EspecificacionMascota:
    def __init__(self):
        self.dict = dict()

    def get_keys(self):
        return self.dict.keys()

    def get_value(self, k):
        return self.dict[k]

    def agregar_parametro(self, llave, valor):
        self.dict[llave] = valor
