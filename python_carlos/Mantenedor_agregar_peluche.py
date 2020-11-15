import pymysql, random
from Clase_agregar_peluche import agregar_peluche

def conectar():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='', db='tienda_masitas')
    except:
        print("error conexion")
    return conn

def insertar(agregar_peluche):
    conexion= conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO peluche_nuevo (id_peluche, nombre, descripcion, valor) VALUES (%s,%s,%s,%s);"
            #llamar el execute con distintos datos
            cursor.execute(consulta,(agregar_peluche.id_peluche, agregar_peluche.nombre, agregar_peluche.descripcion, agregar_peluche.valor))
        conexion.commit()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("error insertar", ex)
        conexion.close

def consultar():
    conexion= conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id_peluche, nombre, descripcion, valor FROM peluche_nuevo;")
            #llamar el execute con distintos datos
            AuxPeluche_add = cursor.fetchall()

            for peluche in AuxPeluche_add:
                print(peluche)
            return AuxPeluche_add
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("error insertar", ex)
        conexion.close

def eliminar(Aux_ID):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM peluche_nuevo WHERE id_peluche= %s;"
            cursor.execute(consulta, (Aux_ID))
            conexion.commit()
            print("datos borrados")

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("error insertar", ex)
        conexion.close
