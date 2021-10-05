import random
from Dominio.EspecificacionMascota import EspecificacionMascota
from Dominio.inventarioMascotas import Inventario
from Dominio.perro import Perro

def test_buscar_perro():
    razas = ['Pitbull', 'Bulldog', 'Doberman', 'Pug', 'Poodle',
             'Golden_retreiver']
    precios = {
        'Pitbull': ['400000', '300000', '200000', '100000'],
        'Bulldog': ['500000', '100000', '800000', '700000'],
        'Doberman': ['500000', '900000', '800000', '700000'],
        'Pug': ['500000', '150000', '200000', '300000'],
        'Poodle': ['500000', '1000000', '800000', '700000'],
        'Golden_retreiver': ['500000', '200000', '800000', '700000']
    }
    inv = Inventario()
    for raza in razas:
        for precio in precios[raza]:
            inv.agregar_perro(Perro('thor', 5, raza, precio,'gris'))
    especificacion = EspecificacionMascota()
    especificacion.agregar_parametro('raza', raza)
    for perro in inv.buscar_perro(especificacion):
        assert perro is not None
    assert len(list(inv.buscar_perro(especificacion))) > 0

def test_fuzzing_buscar_perro():
    razas = ['Pitbull','Bulldog', 'Doberman', 'Pug','Poodle',
             'Golden_retreiver']
    precios = {
        'Pitbull': ['400000', '300000', '200000', '100000'],
        'Bulldog': ['500000', '100000', '800000', '700000'],
        'Doberman': ['500000', '900000', '800000', '700000'],
        'Pug': ['500000', '150000', '200000', '300000'],
        'Poodle': ['500000', '1000000', '800000', '700000'],
        'Golden_retreiver': ['500000', '200000', '800000', '700000']
    }
    nombres = ['lolita','lolito','pelusa','algodon','nieves','copito','tequila','tuercas','pepito']
    edades = [7,6,8,9,10,7,5,11,12,13,14,1,2,3,4]
    colorPelajes=['mono','blanco','gris','cafe','negro','negro_gris']
    cantidad_perros=random.randint(100,500)
    inventario=Inventario()
    especificaciones=[]
    for i in range(cantidad_perros):
        raza = random.choice(razas)
        precio= random.choice(precios[raza])
        nombre= random.choice(nombres)
        edad= random.choice(edades)
        colorPelaje=random.choice(colorPelajes)
        if i%10==0:
            especificacion=EspecificacionMascota()
            especificacion.agregar_parametro('raza',raza)
            especificacion.agregar_parametro('precio',precio)
            especificaciones.append(especificacion)
        g = Perro(nombre,edad,raza,precio,colorPelaje)
        inventario.agregar_perro(g)
    cantidad_busquedas= random.randint(1,len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscar_perro(esp)))>0
        print('encontradas:')
        print(list(inventario.buscar_perro(esp)))
    esp_fake=EspecificacionMascota()
    esp_fake.agregar_parametro('motilado','nea')
    print(inventario.perros)
    assert len(list(inventario.buscar_perro(esp_fake)))==0
    g = Perro(nombre,edad,raza,precio,colorPelaje)
    inventario.agregar_perro(g)
    try:
        inventario.agregar_perro(g)
        assert  False
    except Exception as ex:
        assert ex;
if __name__ == '__main__':
    test_fuzzing_buscar_perro()


