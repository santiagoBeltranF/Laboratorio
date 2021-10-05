import random
from Dominio.EspecificacionMascota import EspecificacionMascota
from Dominio.inventarioMascotas import Inventario
from Dominio.tortuga import Tortuga


def test_buscar_tortuga():
    razas = ['Rusa', 'Estrellada', 'Mediterranea', 'Sulcata', 'Tortuga_caiman',
             'Orejas_rojas']
    precios = {
        'Rusa': ['400000', '300000', '200000', '100000'],
        'Estrellada': ['500000', '100000', '800000', '700000'],
        'Mediterranea': ['500000', '900000', '800000', '700000'],
        'Sulcata': ['500000', '150000', '200000', '300000'],
        'Tortuga_caiman': ['500000', '1000000', '800000', '700000'],
        'Orejas_rojas': ['500000', '200000', '800000', '700000']
    }
    inv = Inventario()
    for raza in razas:
        for precio in precios[raza]:
            inv.agregar_tortuga(Tortuga('Agata', 5, raza, precio, 'fria'))
    especificacion = EspecificacionMascota()
    especificacion.agregar_parametro('raza', raza)
    for tortuga in inv.buscar_tortuga(especificacion):
        assert tortuga is not None
    assert len(list(inv.buscar_tortuga(especificacion))) > 0


def test_fuzzing_buscar_tortuga():
    razas = ['Rusa', 'Estrellada', 'Mediterranea', 'Sulcata', 'Tortuga_caiman',
             'Orejas_rojas']
    precios = {
        'Rusa': ['400000', '300000', '200000', '100000'],
        'Estrellada': ['500000', '100000', '800000', '700000'],
        'Mediterranea': ['500000', '900000', '800000', '700000'],
        'Sulcata': ['500000', '150000', '200000', '300000'],
        'Tortuga_caiman': ['500000', '1000000', '800000', '700000'],
        'Orejas_rojas': ['500000', '200000', '800000', '700000']
    }
    nombres = ['lolita', 'lolito', 'pelusa', 'algodon', 'nieves', 'copito', 'tequila', 'tuercas', 'pepito']
    edades = [7, 6, 8, 9, 10, 7, 5, 11, 12, 13, 14, 1, 2, 3, 4]
    tipoSangres = ['cortas', 'largas']
    cantidad_tortugas = random.randint(100, 500)
    inventario = Inventario()
    especificaciones = []
    for i in range(cantidad_tortugas):
        raza = random.choice(razas)
        precio = random.choice(precios[raza])
        nombre = random.choice(nombres)
        edad = random.choice(edades)
        tipoSangre = random.choice(tipoSangres)
        if i % 10 == 0:
            especificacion = EspecificacionMascota()
            especificacion.agregar_parametro('raza', raza)
            especificacion.agregar_parametro('precio', precio)
            especificaciones.append(especificacion)
        g = Tortuga(nombre, edad, raza, precio, tipoSangre)
        inventario.agregar_tortuga(g)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscar_tortuga(esp))) > 0
        print('encontradas:')
        print(list(inventario.buscar_tortuga(esp)))
    esp_fake = EspecificacionMascota()
    esp_fake.agregar_parametro('motilado', 'nea')
    print(inventario.tortugas)
    assert len(list(inventario.buscar_tortuga(esp_fake))) == 0
    g = Tortuga(nombre, edad, raza, precio, tipoSangre)
    inventario.agregar_tortuga(g)
    try:
        inventario.agregar_tortuga(g)
        assert False
    except Exception as ex:
        assert ex;


if __name__ == '__main__':
    test_fuzzing_buscar_tortuga()
