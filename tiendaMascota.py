from Dominio.ave import Ave
from Dominio.inventarioMascotas import Inventario
from Dominio.perro import Perro
from Dominio.gato import Gato
from Dominio.tortuga import Tortuga
from infraestructura.PersistenciaPerros import PersistenciaPerros
from infraestructura.PersistenciaGatos import PersistenciaGatos
from infraestructura.PersistenciaAves import PersistenciaAves
from infraestructura.PersistenciaTortugas import PersistenciaTortugas

iventario=Inventario()
import  random
import os

if __name__== '__main__':
 saverPerro = PersistenciaPerros()
 saverGatos = PersistenciaGatos()
 saverAves = PersistenciaAves()
 saverTortugas = PersistenciaTortugas()
 saverPerro.connect_perro()
 saverGatos.connect_gatos()
 saverAves. connect_ave()
 saverTortugas.connect_tortugas()
 menu2 = True
 menu1 =True
 while(menu1):

    menu1 = int(input("1- agregar mascota\n"
                      "2- Salir del programa\n"
                      "Ingrese lo que quiere hacer en el menu: "))
    if(menu1==1):
        while (menu2):

            if(menu2 == 1):
                menu = int(input("1- Agregar perro\n"
                                 "2- Agregar gato\n"
                                 "3- Agregar ave\n"
                                 "4- Agregar tortuga\n"
                                 "5- Volver al menu principal\n"
                                 "Ingrese la mascota que desea agregar: "))

                if (menu == 1):

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
                    nombres = ['lolita', 'lolito', 'pelusa', 'algodon', 'nieves', 'copito', 'tequila', 'tuercas', 'pepito']
                    edades = [7, 6, 8, 9, 10, 7, 5, 11, 12, 13, 14, 1, 2, 3, 4]
                    colorPelajes = ['mono', 'blanco', 'gris', 'cafe', 'negro', 'negro_gris']
                    raza = random.choice(razas)
                    precio = random.choice(precios[raza])
                    nombre = random.choice(nombres)
                    edad = random.choice(edades)
                    colorPelaje = random.choice(colorPelajes)
                    g = Perro(nombre, edad, raza, precio, colorPelaje)
                    inventario = Inventario()
                    inventario_json = Inventario()

                    guardar1 = int(input("1- Agregar en save_json_perro\n"
                                         "2- Agregar en base de datos\n"
                                         "3- Volver al menu\n"
                                         "En que forma la deseas guardar: "))

                    if (guardar1 == 1):
                        PersistenciaPerros.save_json_perro(g)
                        for file in os.listdir("./files/perro"):
                            if '.json' in file:
                                inventario_json.agregar_perro(PersistenciaPerros.load_json_perro(file))
                        for g in inventario.perros:
                            PersistenciaPerros.save_json_perro(g)
                        print("La mascota ha siso guardada con exito")
                        print(menu)


                    elif (guardar1 == 2):
                        saverPerro.guardar_perro(g)
                        print("La mascota ha siso guardada con exito")
                        print(menu)




                    elif (guardar1 == 3):
                        print(menu)
                    else:
                        print("Por favor ingrese solo los numeros que pide el menu")
                        print(guardar1)
                        break


                elif (menu == 2):

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
                    nombres = ['lolita', 'lolito', 'pelusa', 'algodon', 'nieves', 'copito', 'tequila', 'tuercas', 'pepito']
                    edades = [7, 6, 8, 9, 10, 7, 5, 11, 12, 13, 14, 1, 2, 3, 4]
                    pelages = ['corto', 'largo', 'simiLargo', 'rizado', 'sin_Pelo', ]
                    raza = random.choice(razas)
                    precio = random.choice(precios[raza])
                    nombre = random.choice(nombres)
                    edad = random.choice(edades)
                    pelage = random.choice(pelages)
                    g = Gato(nombre, edad, raza, precio, pelage)
                    inventario = Inventario()
                    inventario_json = Inventario()

                    guardar2 = int(input("1- Agregar en save_json_gato\n"
                                         "2- Agregar en base de datos\n"
                                         "3- Volver al menu\n"
                                         "En que forma la deseas guardar: "))

                    if (guardar2 == 1):
                        PersistenciaGatos.save_json_gato(g)
                        for file in os.listdir("./files/gato"):
                            if '.json' in file:
                                inventario_json.agregar_gato(PersistenciaGatos.load_json_gato(file))
                        for g in inventario.gatos:
                            PersistenciaGatos.save_json_gato(g)
                        print("La mascota ha siso guardada con exito")
                        print(menu)


                    elif (guardar2 == 2):
                        saverGatos.guardar_gatos(g)
                        print("La mascota ha siso guardada con exito")
                        print(menu)


                    elif (guardar2 == 3):
                        print(menu)

                    else:
                        print("Por favor ingrese solo los numeros que pide el menu")
                        print(guardar2)
                        break


                elif (menu == 3):

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
                    nombres = ['lolita', 'lolito', 'pelusa', 'algodon', 'nieves', 'copito', 'tequila', 'tuercas', 'pepito']
                    edades = [7, 6, 8, 9, 10, 7, 5, 11, 12, 13, 14, 1, 2, 3, 4]
                    tipoPlumas = ['cortas', 'largas']
                    raza = random.choice(razas)
                    precio = random.choice(precios[raza])
                    nombre = random.choice(nombres)
                    edad = random.choice(edades)
                    tipoPluma = random.choice(tipoPlumas)
                    g = Ave(nombre, edad, raza, precio, tipoPluma)
                    inventario = Inventario()
                    inventario_json = Inventario()

                    guardar3 = int(input("1- Agregar en save_json_ave\n"
                                         "2- Agregar en base de datos\n"
                                         "3- Volver al menu\n"
                                         "En que forma la deseas guardar: "))

                    if (guardar3 == 1):
                        PersistenciaAves.save_json_ave(g)
                        for file in os.listdir("./files/ave"):
                            if '.json' in file:
                                inventario_json.agregar_ave(PersistenciaAves.load_json_ave(file))
                        for g in inventario.aves:
                            PersistenciaAves.save_json_ave(g)
                        print("La mascota ha siso guardada con exito")
                        print(menu)


                    elif (guardar3 == 2):
                        saverAves.guardar_ave(g)
                        print("La mascota ha siso guardada con exito")
                        print(menu)

                    elif (guardar3 == 3):
                        print(menu)

                    else:
                        print("Por favor ingrese solo los numeros que pide el menu")
                        print(guardar3)
                        break


                elif (menu == 4):

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
                    raza = random.choice(razas)
                    precio = random.choice(precios[raza])
                    nombre = random.choice(nombres)
                    edad = random.choice(edades)
                    tipoSangre = random.choice(tipoSangres)
                    g = Tortuga(nombre, edad, raza, precio, tipoSangre)
                    inventario = Inventario()
                    inventario_json = Inventario()

                    guardar4 = int(input("1- Agregar en save_json_tortuga\n"
                                         "2- Agregar en base de datos\n"
                                         "3- Volver al menu\n"
                                         "En que forma la deseas guardar: "))

                    if (guardar4 == 1):
                        PersistenciaTortugas.save_json_tortuga(g)
                        for file in os.listdir("./files/tortuga"):
                            if '.json' in file:
                                inventario_json.agregar_tortuga(PersistenciaTortugas.load_json_tortuga(file))
                        for g in inventario.tortugas:
                            PersistenciaTortugas.save_json_tortuga(g)
                        print("La mascota ha siso guardada con exito")
                        print(menu)


                    elif (guardar4 == 2):
                        saverTortugas.guardar_tortugas(g)
                        print("La mascota ha siso guardada con exito")
                        print(menu)

                    elif (guardar4 == 3):
                        print(menu)

                    else:
                        print("Por favor ingrese solo los numeros que pide el menu")
                        print(guardar4)
                        break


                elif (menu == 5):
                    menu2 = False

                else:
                    print("Por favor ingrese los numeros del menu")
                    break



    elif(menu1==2):
        menu1=False
    else:
        print("por favor ingrese los numeros del menu")
        break



