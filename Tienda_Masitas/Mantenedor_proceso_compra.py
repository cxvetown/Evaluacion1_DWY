import pymysql, random
from Clase_proceso_compra import proceso_compra

def conectar():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='', db='tienda_masitas')
    except:
        print("error conexion")
    return conn

def insertar(proceso_compra):
    conexion= conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO proceso_compra (codigo_compra, tipo_tarjeta, numero_tarjeta, año, nombre_usuario, codigo_verificacion) VALUES (%s,%s,%s,%s,%s,%s);"
            #llamar el execute con distintos datos
            cursor.execute(consulta,(proceso_compra.codigo_compra, proceso_compra.tipo_tarjeta, proceso_compra.numero_tarjeta, proceso_compra.año, proceso_compra.nombre_usuario, proceso_compra.codigo_verificacion))
        conexion.commit()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("error insertar", ex)
        conexion.close

def generar_codigo():
    numero = random.randint(1, 999999)
    return numero

def eliminar():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM carrito_compra")
            #llamar el execute con distintos datos
            cursor.fetchall()
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error de SQL:",e)
    conexion.close()
