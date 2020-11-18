import pymysql
from Clase_lista_deseos import lista_deseos

def conectar():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='', db='tienda_masitas')
    except:
        print("error conexion")
    return conn

def consultar():
    conexion= conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT codigo_lista_deseo, nombre, valor FROM lista_deseos;")
            #llamar el execute con distintos datos
            aux_deseos = cursor.fetchall()

            for deseos in aux_deseos:
                print(deseos)
            return aux_deseos
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("error insertar", ex)
        conexion.close

def insertar(lista_deseos):
    conexion= conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO lista_deseos (codigo_lista_deseo, nombre, valor) VALUES (%s,%s,%s);"
            #llamar el execute con distintos datos
            cursor.execute(consulta,(lista_deseos.codigo_lista_deseo, lista_deseos.nombre, lista_deseos.valor))
        conexion.commit()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("error insertar", ex)
        conexion.close

def eliminar(aux_id_peluche):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM lista_deseos where codigo_lista_deseo = %s;"
            #Podemos ejecutar varios query
            cursor.execute(consulta,(aux_id_peluche))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error de SQL:",e)
    conexion.close()

def actualizar(lista_deseos):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE lista_deseos SET nombre = %s, valor = %s where codigo_lista_deseo = %s;"
            #Podemos ejecutar varios query
            cursor.execute(consulta,(lista_deseos.nombre, lista_deseos.valor, lista_deseos.codigo_lista_deseo))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error de SQL:",e)
    conexion.close() 
