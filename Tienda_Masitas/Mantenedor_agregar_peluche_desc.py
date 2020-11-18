import pymysql, random
from Clase_agregar_peluche_desc import agregar_peluche_desc

def conectar():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='', db='tienda_masitas')
    except:
        print("error conexion")
    return conn

def insertar(agregar_peluche_desc):
    conexion= conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO peluche_nuevo_descuento (id_peluche_desc, nombre, descripcion, valor, descuento) VALUES (%s,%s,%s,%s,%s);"
            #llamar el execute con distintos datos
            cursor.execute(consulta,(agregar_peluche_desc.id_peluche_desc, agregar_peluche_desc.nombre, agregar_peluche_desc.descripcion, agregar_peluche_desc.valor, agregar_peluche_desc.descuento))
        conexion.commit()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("error insertar", ex)
        conexion.close

def consultar():
    conexion= conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id_peluche_desc, nombre, descripcion, valor, descuento FROM peluche_nuevo_descuento;")
            #llamar el execute con distintos datos
            AuxPeluche_add_desc = cursor.fetchall()

            for peluche_desc in AuxPeluche_add_desc:
                print(peluche_desc)
            return AuxPeluche_add_desc
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("error insertar", ex)
        conexion.close

def eliminar(Aux_ID):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM peluche_nuevo_descuento WHERE id_peluche_desc= %s;"
            cursor.execute(consulta,(Aux_ID))
            conexion.commit()
            print("datos borrados")

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("error insertar", ex)
        conexion.close

def actualizar(agregar_peluche_desc):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE peluche_nuevo_descuento SET nombre = %s, descripcion = %s, valor=%s, descuento =%s where id_peluche_desc = %s;"
            #Podemos ejecutar varios query
            cursor.execute(consulta,(agregar_peluche_desc.nombre, agregar_peluche_desc.descripcion, agregar_peluche_desc.valor, agregar_peluche_desc.descuento, agregar_peluche_desc.id_peluche_desc))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error de SQL:",e)
    conexion.close() 