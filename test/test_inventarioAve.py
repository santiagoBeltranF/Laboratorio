import random
from Dominio.EspecificacionMascota import EspecificacionMascota
from Dominio.inventarioMascotas import Inventario
from Dominio.ave import Ave

def test_buscar_ave():
    razas = ['Pavo_Real', 'loro_arco_iris', 'Ganso', 'Faisan', 'Bengali_Babero',
             'Fisher']
    precios = {
        'Pavo_Real': ['400000', '300000', '200000', '100000'],
        'loro_arco_iris': ['500000', '100000', '800000', '700000'],
        'Ganso': ['500000', '900000', '800000', '700000'],
        'Faisan': ['500000', '150000', '200000', '300000'],
        'Bengali_Babero': ['500000', '1000000', '800000', '700000'],
        'Fisher': ['500000', '200000', '800000', '700000']
    }
    inv = Inventario()
    for raza in razas:
        for precio in precios[raza]:
            inv.agregar_ave(Ave('Agata', 5, raza, precio,''))
    especificacion = EspecificacionMascota()
    especificacion.agregar_parametro('raza', raza)
    for ave in inv.buscar_ave(especificacion):
        assert ave is not None
    assert len(list(inv.buscar_ave(especificacion))) > 0

def test_fuzzing_buscar_ave():
    razas = ['Pavo_Real', 'loro_arco_iris', 'Ganso', 'Faisan', 'Bengali_Babero',
             'Fisher']
    precios = {
        'Pavo_Real': ['400000', '300000', '200000', '100000'],
        'loro_arco_iris': ['500000', '100000', '800000', '700000'],
        'Ganso': ['500000', '900000', '800000', '700000'],
        'Faisan': ['500000', '150000', '200000', '300000'],
        'Bengali_Babero': ['500000', '1000000', '800000', '700000'],
        'Fisher': ['500000', '200000', '800000', '700000']
    }
    nombres = ['lolita','lolito','pelusa','algodon','nieves','copito','tequila','tuercas','pepito']
    edades = [7,6,8,9,10,7,5,11,12,13,14,1,2,3,4]
    tipoPlumas=['cortas','largas']
    cantidad_aves=random.randint(100,500)
    inventario=Inventario()
    especificaciones=[]
    for i in range(cantidad_aves):
        raza = random.choice(razas)
        precio= random.choice(precios[raza])
        nombre= random.choice(nombres)
        edad= random.choice(edades)
        tipoPluma=random.choice(tipoPlumas)
        if i%10==0:
            especificacion=EspecificacionMascota()
            especificacion.agregar_parametro('raza',raza)
            especificacion.agregar_parametro('precio',precio)
            especificaciones.append(especificacion)
        g = Ave(nombre,edad,raza,precio,tipoPluma)
        inventario.agregar_ave(g)
    cantidad_busquedas= random.randint(1,len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscar_ave(esp)))>0
        print('encontradas:')
        print(list(inventario.buscar_ave(esp)))
    esp_fake=EspecificacionMascota()
    esp_fake.agregar_parametro('motilado','nea')
    print(inventario.aves)
    assert len(list(inventario.buscar_ave(esp_fake)))==0
    g = Ave(nombre,edad,raza,precio,tipoPluma)
    inventario.agregar_ave(g)
    try:
        inventario.agregar_ave(g)
        assert  False
    except Exception as ex:
        assert ex;
if __name__ == '__main__':
    test_fuzzing_buscar_ave()