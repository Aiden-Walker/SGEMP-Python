def leer_ventas_tapas():
    listaWasa = []
    #Bucle for
    for _ in range(4):
        nombre = input("Introduce el nombre de la tapa (WASAAAAAAA)")
        precio_unitario = float(input("Introduce el precio de la tapita (no mu caro porfis)"))
        cantidad = int(input("Introduce la cantidad de tapas en stock (69420)"))
        #Introduccion de tupla en una lista
        listaWasa.append((nombre, precio_unitario, cantidad))
    return listaWasa
#print(leer_ventas_tapas())
def calcular_estadisticas_tapas(lista_ventas):
    #Creacion de un diccionario
    skibidiDiccionario = {}
    #Recorrer una lista
    for (nombre, precio_unitario, cantidad) in lista_ventas:
        total_ventas = precio_unitario * cantidad
        iva_aplicado = total_ventas * 10 / 100
        #If con else y else if
        if cantidad > 25:
            popularidad = "Alta"
        elif cantidad > 15:
            popularidad = "Media"
        else:
            popularidad = "Baja"
        #Switch
       #  match cantidad_v:
        
       #     case e if e > 25:
       #        popularidad = "alta"
       #   case e if e > 15:
       #        popularidad = "media"
       # case e if e <= 15:
       #         popularidad = "baja"
        #Meter una llave en el diccionario
        skibidiDiccionario[nombre] = (total_ventas, iva_aplicado, popularidad)
    return skibidiDiccionario
print(calcular_estadisticas_tapas([('Serranito', 3.5, 25), ('Solomillo al whisky', 4.2, 18), ('Montadito de pringá', 2.8, 32), ('Espinacas con garbanzos', 3.0, 21)]))