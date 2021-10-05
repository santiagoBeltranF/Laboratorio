import random
from Dominio.EspecificacionMascota import EspecificacionMascota
from Dominio.inventarioMascotas import Inventario
from Dominio.mascota import Mascota



def test_buscar():
    razas = ['pavos_domesticos','gallinas_domesticos', 'perro_criollo', 'perro_raza_Fina','gato_criollo',
             'gato_raza_Fina']
    precios = {
        'pavos_domesticos': ['9000', '70000', '60000', '80000'],
        'gallinas_domesticos': ['10000', '20000', '30000', '15000'],
        'perro_criollo': ['30000', '20000', '10000', '25000'],
        'perro_raza_Fina': ['500000', '1000000', '800000', '700000'],
        'gato_criollo': ['30000', '20000', '10000', '25000'],
        'gato_raza_Fina': ['500000', '1000000', '800000', '700000']
    }
    inv = Inventario()
    for raza in razas:
        for precio in precios[raza]:
            inv.agregar_mascota(Mascota('kira', 5, raza, precio))
    especificacion = EspecificacionMascota()
    especificacion.agregar_parametro('raza', raza)
    for mascota in inv.buscar_mascotas(especificacion):
        assert mascota is not None
    assert len(list(inv.buscar_mascotas(especificacion))) > 0


def test_fuzzing_buscar():
    razas = ['pavos_domesticos', 'gallinas_domesticos', 'perro_criollo', 'perro_raza_Fina', 'gato_criollo',
             'gato_raza_Fina']
    precios = {
        'pavos_domesticos': ['9000', '70000', '60000', '80000'],
        'gallinas_domesticos': ['10000', '20000', '30000', '15000'],
        'perro_criollo': ['30000', '20000', '10000', '25000'],
        'perro_raza_Fina': ['500000', '1000000', '800000', '700000'],
        'gato_criollo': ['30000', '20000', '10000', '25000'],
        'gato_raza_Fina': ['500000', '1000000', '800000', '700000']
    }
    nombres = ['lolita','lolito','pelusa','algodon','nieves','copito','tequila','tuercas','pepito']
    edades = [7,6,8,9,10,7,5,11,12,13,14,1,2,3,4]
    cantidad_mascotas=random.randint(100,500)
    inventario=Inventario()
    especificaciones=[]
    for i in range(cantidad_mascotas):
        raza = random.choice(razas)
        precio= random.choice(precios[raza])
        nombre= random.choice(nombres)
        edad= random.choice(edades)
        if i%10==0:
            especificacion=EspecificacionMascota()
            especificacion.agregar_parametro('raza',raza)
            especificacion.agregar_parametro('precio',precio)
            especificaciones.append(especificacion)
        g = Mascota(nombre,edad,raza,precio)
        inventario.agregar_mascota(g)
    cantidad_busquedas= random.randint(1,len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscar_mascotas(esp)))>0
        print('encontradas:')
        print(list(inventario.buscar_mascotas(esp)))
    esp_fake=EspecificacionMascota()
    esp_fake.agregar_parametro('motilado','nea')
    print(inventario.mascotas)
    assert len(list(inventario.buscar_mascotas(esp_fake)))==0
    g = Mascota(nombre,edad,raza,precio)
    inventario.agregar_mascota(g)
    try:
        inventario.agregar_mascota(g)
        assert  False
    except Exception as ex:
        assert ex;
if __name__ == '__main__':
    test_fuzzing_buscar()



