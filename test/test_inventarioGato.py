import random
from Dominio.EspecificacionMascota import EspecificacionMascota
from Dominio.inventarioMascotas import Inventario
from Dominio.gato import Gato

def test_buscar_gato():
    razas = ['Persa', 'Bengala', 'Siames', 'sfinge', 'Ragdoll',
             'Savannah']
    precios = {
        'Persa': ['400000', '300000', '200000', '100000'],
        'Bengala': ['500000', '100000', '800000', '700000'],
        'Siames': ['500000', '900000', '800000', '700000'],
        'sfinge': ['500000', '150000', '200000', '300000'],
        'Ragdoll': ['500000', '1000000', '800000', '700000'],
        'Savannah': ['500000', '200000', '800000', '700000']
    }
    inv = Inventario()
    for raza in razas:
        for precio in precios[raza]:
            inv.agregar_gato(Gato('Agata', 5, raza, precio,'Pelo_semilargo'))
    especificacion = EspecificacionMascota()
    especificacion.agregar_parametro('raza', raza)
    for gato in inv.buscar_gato(especificacion):
        assert gato is not None
    assert len(list(inv.buscar_gato(especificacion))) > 0

def test_fuzzing_buscar_gato():
    razas = ['Persa', 'Bengala', 'Siames', 'sfinge', 'Ragdoll',
             'Savannah']
    precios = {
        'Persa': ['400000', '300000', '200000', '100000'],
        'Bengala': ['500000', '100000', '800000', '700000'],
        'Siames': ['500000', '900000', '800000', '700000'],
        'sfinge': ['500000', '150000', '200000', '300000'],
        'Ragdoll': ['500000', '1000000', '800000', '700000'],
        'Savannah': ['500000', '200000', '800000', '700000']
    }
    nombres = ['lolita','lolito','pelusa','algodon','nieves','copito','tequila','tuercas','pepito']
    edades = [7,6,8,9,10,7,5,11,12,13,14,1,2,3,4]
    pelages=['corto','largo','simiLargo','rizado','sin_Pelo',]
    cantidad_perros=random.randint(100,500)
    inventario=Inventario()
    especificaciones=[]
    for i in range(cantidad_perros):
        raza = random.choice(razas)
        precio= random.choice(precios[raza])
        nombre= random.choice(nombres)
        edad= random.choice(edades)
        pelage=random.choice(pelages)
        if i%10==0:
            especificacion=EspecificacionMascota()
            especificacion.agregar_parametro('raza',raza)
            especificacion.agregar_parametro('precio',precio)
            especificaciones.append(especificacion)
        g = Gato(nombre,edad,raza,precio,pelage)
        inventario.agregar_gato(g)
    cantidad_busquedas= random.randint(1,len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscar_gato(esp)))>0
        print('encontradas:')
        print(list(inventario.buscar_gato(esp)))
    esp_fake=EspecificacionMascota()
    esp_fake.agregar_parametro('motilado','nea')
    print(inventario.gatos)
    assert len(list(inventario.buscar_perro(esp_fake)))==0
    g = Gato(nombre,edad,raza,precio,pelage)
    inventario.agregar_gato(g)
    try:
        inventario.agregar_gato(g)
        assert  False
    except Exception as ex:
        assert ex;
if __name__ == '__main__':
    test_fuzzing_buscar_gato()
