import pymysql
from Clase_usuario import usuario

def conectar():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='', db='tienda_masitas')
    except:
        print("error conexion")
    return conn

def insertar(usuario):
    conexion= conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO usuario (rut, nombre, apellido, telefono, correo, contraseña) VALUES (%s,%s,%s,%s,%s,%s);"
            #llamar el execute con distintos datos
            cursor.execute(consulta,(usuario.rut, usuario.nombre, usuario.apellido, usuario.telefono, usuario.correo, usuario.contraseña))
        conexion.commit()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as ex:
        print("error insertar", ex)
        conexion.close

def login(usuario):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT rut, nombre, apellido, telefono, correo, contraseña FROM usuario where rut = %s and contraseña= %s"
            #Podemos ejecutar varios query
            cursor.execute(consulta,(usuario.nombre,usuario.apellido, usuario.telefono, usuario.correo, usuario.contraseña ,usuario.rut))
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error de SQL:",e)
    conexion.close() 

def actualizar(usuario):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE usuario SET nombre = %s, apellido = %s, telefono  = %s, correo = %s, contraseña=%s  where rut = %s"
            #Podemos ejecutar varios query
            cursor.execute(consulta,(usuario.nombre,usuario.apellido, usuario.telefono, usuario.correo, usuario.contraseña ,usuario.rut))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error de SQL:",e)
    conexion.close() 