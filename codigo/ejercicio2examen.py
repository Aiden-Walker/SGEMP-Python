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
print(leer_ventas_tapas())
def calcular_estadisticas_tapas(lista_ventas):
    #Creacion de un diccionario
    skibidiLista = {}