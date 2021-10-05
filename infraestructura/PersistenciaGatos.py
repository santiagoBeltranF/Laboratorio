
import sqlite3
from Dominio.gato import Gato
import jsonpickle

class PersistenciaGatos():

    def connect_gatos(self):
        self.con = sqlite3.connect("la_tienda_de_santiago")
        self.__crear_tabla_gatos()


    def __crear_tabla_gatos(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE GATO(codigoGat text primary key, nombre text," \
                " edad int, raza text," \
                " precio float,pelage text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_gatos(self,gato :Gato):
        cursor = self.con.cursor()
        query = "insert into GATO(codigoGat , nombre ," \
                " edad,raza, precio ,pelage  ) values(" \
                f" ?,?,?,?,?,?)"
        cursor.execute(query,(str(gato.codigoGat),gato.nombre,gato.edad,
                              gato.raza,gato.precio,gato.pelage
                              ))
        self.con.commit()



    @classmethod
    def save_json_gato(cls, gato):
        text_open = open("files/gato/" + str(gato.codigoGat) + '.json', mode='w')
        json_gui = jsonpickle.encode(gato)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json_gato(cls, file_name):
        text_open = open("files/gato/" + file_name, mode='r')
        json_gui = text_open.readline()
        gato = jsonpickle.decode(json_gui)
        text_open.close()
        return gato