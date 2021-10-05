
import sqlite3
from Dominio.tortuga import Tortuga
import jsonpickle

class PersistenciaTortugas():
    def connect_tortugas(self):
        self.con = sqlite3.connect("la_tienda_de_santiago")
        self.__crear_tabla_tortugas()


    def __crear_tabla_tortugas(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE TORTUGA(codigoRep text primary key, nombre text," \
                " edad int, raza text," \
                " precio float,tipoSangre text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_tortugas(self,tortuga :Tortuga):
        cursor = self.con.cursor()
        query = "insert into TORTUGA(codigoRep , nombre ," \
                " edad,raza , precio ,tipoSangre  ) values(" \
                f" ?,?,?,?,?,?)"
        cursor.execute(query,(str(tortuga.codigoRep),tortuga.nombre,tortuga.edad,
                              tortuga.raza,tortuga.precio,tortuga.tipoSangre
                              ))
        self.con.commit()






    @classmethod
    def save_json_tortuga(cls, tortuga):
        text_open = open("files/tortuga/" + str(tortuga.codigoRep) + '.json', mode='w')
        json_gui = jsonpickle.encode(tortuga)
        text_open.write(json_gui)
        text_open.close()


    @classmethod
    def load_json_tortuga(cls, file_name):
        text_open = open("files/tortuga/" + file_name, mode='r')
        json_gui = text_open.readline()
        tortuga = jsonpickle.decode(json_gui)
        text_open.close()
        return tortuga