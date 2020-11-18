import pymysql
from claseCliente import Cliente

def conectar():
    try:
        conexion = pymysql.connect(host='localhost',
                                   user = 'root',
                                   password='',
                                   db='prueba')
    except:
        print("Problemas al conectar")
    return conexion

def insertar(cliente):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO cliente (rut,nombre) VALUES (%s,%s);"
            #Podemos ejecutar varios query
            cursor.execute(consulta,(cliente.rut,cliente.nombre))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error de SQL:",e)
    conexion.close()    
        
def actualizar(cliente):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE cliente SET nombre = %s where rut = %s;"
            #Podemos ejecutar varios query
            cursor.execute(consulta,(cliente.nombre,cliente.rut))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error de SQL:",e)
    conexion.close()    

def eliminar(auxRut):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM cliente where rut = %s;"
            #Podemos ejecutar varios query
            cursor.execute(consulta,(auxRut))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error de SQL:",e)
    conexion.close()    

def consultar():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            #Podemos ejecutar varios query
            cursor.execute("SELECT rut,nombre FROM cliente;")
            #se usa fetchall para cargar una coleccion de datos
            auxClientes = cursor.fetchall()
            #Se muestran los datos recorriendo la coleccion
            for cli in auxClientes:
                print(cli)
            return auxClientes        
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error de SQL:",e)
    conexion.close()

def buscar(auxRut):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM cliente WHERE rut = %s;"
            #Podemos ejecutar varios query
            cursor.execute(consulta,(auxRut))
            #se usa fetchall para cargar una coleccion de datos
            auxClientes = cursor.fetchall()
            #Se muestran los datos recorriendo la coleccion
            for cli in auxClientes:
                print(cli)
            return auxClientes        
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as e:
        print("Error de SQL:",e)
    conexion.close()



#programa principal
conectar()
print("Estamos conectados")
#auxCliente = Cliente("1-9","El Guru")
#insertar(auxCliente)
#print("Datos Guardados")
#auxCliente = Cliente("1-9","El Guru Viernes")
#actualizar(auxCliente)
#print("Datos Actualizados")
#eliminar("1-9")
#print("Datos Eliminados")
#consultar()
buscar("234")                                                                              