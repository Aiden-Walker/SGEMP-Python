import csv
import pymysql
def cargar_reservas_desde_csv():
    #Como abrir un fichero
    #rt es readtext
    #encoding del archivo utf-8
    #Abrir archivo
    dic_reservas = {}
    with open('reservas.csv', mode = 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            id_reserva = int(fila["id"])
            #Meter datos del csv en diccionario
            dic_reservas[id_reserva] = {"nombre": fila["nombre"], "telefono": fila["telefono"], "fecha": fila["fecha"], "personas": int(fila["personas"]), "mesa": int(fila["mesa"])}
        return dic_reservas
def insertar_reservas_bbdd(reservas):
#Cursor y conexion base de datos
    conn  = pymysql.connect(host='db', user='root', password='test', database='examen')
    cursor = conn.cursor()
    for id , datos in reservas.items():
        cursor.execute("""INSERT INTO reserva
            (id, nombre_cliente, telefono, fecha_reserva, numero_personas, numero_mesa)
            VALUES (%s, %s, %s, %s, %s, %s)""", (id , datos["nombre"], datos["telefono"], datos["fecha"], datos["personas"], datos["mesa"]))
    cursor.close()
    conn.commit()
    conn.close()
def mostrar_reservas_fecha(fecha):
    #Crear conexion que da un diccionario
    conn  = pymysql.connect(host='db', user='root', password='test', database='examen', cursorclass = pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    sql = "SELECT * FROM reserva WHERE fecha_reserva = %s"
    cursor.execute(sql, (fecha, ))
    results = cursor.fetchall()
    output = f"RESERVAS PARA {fecha}:" + "\n" + 30*"=" + "\n"
    for reserva in resultados:
        output += f"Mesa {reserva['numero_mesa']}: {reserva['nombre_cliente']} ({reserva['numero_personas']} personas - Tel:{reserva['telefono']})" + "\n"
    reservas_totales = len(results)
    personas = sum(map(lambda reservas: reservas['numero_personas'], resultados))
    output += "\n" + f"Total: {reservastotal} reservas, {personastotal} personas" 
    print(output)
def main():

    print(cargar_reservas_desde_csv())

    insertar_reservas_bbdd(cargar_reservas_desde_csv())

    mostrar_reservas_fecha("2025-03-15")
if __name__ == "__main__":
    main()