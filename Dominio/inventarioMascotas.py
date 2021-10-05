from Dominio.mascota import Mascota
from Dominio.perro import Perro
from Dominio.gato import Gato
from Dominio.ave import Ave
from Dominio.tortuga import Tortuga
from Dominio.EspecificacionMascota import EspecificacionMascota


class Inventario:

    def __init__(self):
        self.mascotas = []
        self.perros = []
        self.gatos=[]
        self.aves=[]
        self.tortugas=[]

    def agregar_mascota(self,mascota):
        if type(mascota) == Mascota:
            espec = EspecificacionMascota()
            espec.agregar_parametro('id', mascota.id)
            if len(list(self.buscar_mascotas(espec))) == 0:
                self.mascotas.append(mascota)
            else:
                raise Exception('Mascota repetida')

    def buscar_mascotas(self, especificacion):
        for m in self.mascotas:
            if m.cumple(especificacion):
                yield m

    def agregar_perro(self, perro):
        if type(perro) == Perro:
            espec = EspecificacionMascota()
            espec.agregar_parametro('codigoPer', perro.codigoPer)
            if len(list(self.buscar_perro(espec))) == 0:
                self.perros.append(perro)
            else:
                raise Exception('perro repetido')

    def buscar_perro(self, especificacion):
        for m in self.perros:
            if m.cumple_perro(especificacion):
                yield m


    def agregar_gato(self, gato):
        if type(gato) == Gato:
            espec = EspecificacionMascota()
            espec.agregar_parametro('codigoGat', gato.codigoGat)
            if len(list(self.buscar_gato(espec))) == 0:
                self.gatos.append(gato)
            else:
                raise Exception('gato repetido')

    def buscar_gato(self, especificacion):
        for m in self.gatos:
            if m.cumple_Gato(especificacion):
                yield m

    def agregar_ave(self, ave):
        if type(ave) == Ave:
            espec = EspecificacionMascota()
            espec.agregar_parametro('codigoAv', ave.codigoAv)
            if len(list(self.buscar_ave(espec))) == 0:
                self.aves.append(ave)
            else:
                raise Exception('ave repetido')

    def buscar_ave(self, especificacion):
        for m in self.aves:
            if m.cumple_Ave(especificacion):
                yield m

    def agregar_tortuga(self, tortuga):
        if type(tortuga) == Tortuga:
            espec = EspecificacionMascota()
            espec.agregar_parametro('codigoRep', tortuga.codigoRep)
            if len(list(self.buscar_tortuga(espec))) == 0:
                self.tortugas.append(tortuga)
            else:
                raise Exception('tortuga repetida')

    def buscar_tortuga(self, especificacion):
        for m in self.tortugas:
            if m.cumple_Tortuga(especificacion):
                yield m