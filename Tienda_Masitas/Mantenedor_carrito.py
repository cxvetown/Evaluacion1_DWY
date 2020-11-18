import pymysql, random
from Clase_carrito_compras import carrito_compras

def conectar():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='', db='tienda_masitas')
    except:
        print("error conexion")
    return conn

def generar_codigo():
    numero = random.randint(1, 9999)
    return numero

def insertar(carrito_compras):
    conexion= conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO carrito_compra (id_compra, producto, descripcion, valor) VALUES (%s,%s,%s,%s);"
            #llamar el execute con distintos datos
            cursor.execute(consulta,(carrito_compras.id_compra, carrito_compras.producto, carrito_compras.descripcion, carrito_compras.valor))
        conexion.commit()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("error insertar", ex)
        conexion.close
        
def consultar():
    conexion= conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id_compra, producto, descripcion, valor FROM carrito_compra;")
            #llamar el execute con distintos datos
            aux_carrito = cursor.fetchall()

            for peluche in aux_carrito:
                print(peluche)
            return aux_carrito
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("error insertar", ex)
        conexion.close

def eliminar(id_peluche):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM carrito_compra where id_compra = %s;"
            #Podemos ejecutar varios query
            cursor.execute(consulta,(id_peluche))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error de SQL:",e)
    conexion.close()
