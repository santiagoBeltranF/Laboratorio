import sqlite3

import jsonpickle
from Dominio.ave import Ave

class PersistenciaAves():
    def connect_ave(self):
        self.con = sqlite3.connect("la_tienda_de_santiago")
        self.__crear_tabla_Aves()


    def __crear_tabla_Aves(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE AVE(codigoAV text primary key, nombre text," \
                " edad int, raza text," \
                " precio float,tipoPlumas text)"
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_ave(self,ave : Ave):
        cursor = self.con.cursor()
        query = "insert into AVE(codigoAv, nombre ," \
                " edad,raza, precio ,tipoPlumas  ) values(" \
                f" ?,?,?,?,?,?)"
        cursor.execute(query,(str(ave.codigoAv),ave.nombre,ave.edad,
                              ave.raza,ave.precio,ave.tipoPlumas
                              ))
        self.con.commit()





    @classmethod
    def save_json_ave(cls, ave):
        text_open = open("files/ave/" + str(ave.codigoAv) + '.json', mode='w')
        json_gui = jsonpickle.encode(ave)
        text_open.write(json_gui)
        text_open.close()


    @classmethod
    def load_json_ave(cls, file_name):
        text_open = open("files/ave/" + file_name, mode='r')
        json_gui = text_open.readline()
        ave = jsonpickle.decode(json_gui)
        text_open.close()
        return ave