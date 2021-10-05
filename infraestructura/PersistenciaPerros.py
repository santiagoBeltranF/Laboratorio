import sqlite3
from Dominio.perro import Perro

import jsonpickle


class PersistenciaPerros():

    def __init__(self):
        self.con = sqlite3.connect("la_tienda_de_santiago")

    def connect_perro(self):
        self.__crear_tabla_perro()

    def __crear_tabla_perro(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE PERRO(codigoPer text primary key, nombre text," \
                    " edad int, raza text," \
                    " precio float,colorPelage text)"
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_perro(self, perro: Perro):
        cursor = self.con.cursor()
        query = "insert into PERRO(codigoPer ,nombre ," \
                " edad ,raza,precio ,colorPelage ) values(" \
                f" ?,?,?,?,?,?)"
        cursor.execute(query, (str(perro.codigoPer), perro.nombre, perro.edad,
                               perro.raza,perro.precio, perro.colorPelage))
        self.con.commit()

    @classmethod
    def save_json_perro(cls, perro):
        text_open = open("files/perro/" + str(perro.codigoPer) + '.json', mode='w')
        json_gui = jsonpickle.encode(perro)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json_perro(cls, file_name):
        text_open = open("files/perro/" + file_name, mode='r')
        json_gui = text_open.readline()
        perro = jsonpickle.decode(json_gui)
        text_open.close()
        return perro
