import pymysql
from Clase_peluche import peluche

def conectar():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='', db='tienda_masitas')
    except:
        print("error conexion")
    return conn