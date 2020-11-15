import pymysql
from Clase_carrito_compras import carrito_compras

def conectar():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='', db='tienda_masitas')
    except:
        print("error conexion")
    return conn

def insertar(carrito_compras):
    conexion= conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO carrito_compra (id_compra, producto, valor, cantidad) VALUES (%s,%s,%s,%s);"
            #llamar el execute con distintos datos
            cursor.execute(consulta,(carrito_compras.id_compra, carrito_compras.producto, carrito_compras.valor, carrito_compras.cantidad))
        conexion.commit()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("error insertar", ex)
        conexion.close
        
def consultar():
    conexion= conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id_compra, producto, valor, cantidad FROM carrito_compra;")
            #llamar el execute con distintos datos
            aux_carrito = cursor.fetchall()

            for peluche in aux_carrito:
                print(peluche)
            return aux_carrito
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("error insertar", ex)
        conexion.close

def buscar(auxId):
    conexion= conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = cursor.execute("SELECT * FROM carrito_compra WHERE id_compra= %s")
            cursor.execute(consulta,(auxId))
            #fetchall para traer datos
            auxcarrito = cursor.fetchall()
            #recorrer datos
            for carrito in auxcarrito:
                print(carrito)
            return carrito
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("error insertar", ex)
        conexion.close


#separador
#conectar()
#print("conectado")

#auxcarrito = carrito_compras("0", "0", "0", "0")
#insertar(auxcarrito)
#print("datos ward")
#consultar()

        