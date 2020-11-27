#programa de arranque
import Mantenedor_agregar_peluche, Mantenedor_carrito, Mantenedor_usuario, Mantenedor_agregar_peluche_desc, Mantenedor_lista_deseo, Mantenedor_proceso_compra
import Clase_agregar_peluche, Clase_carrito_compras, Clase_usuario, Clase_agregar_peluche_desc, Clase_lista_deseos, Clase_proceso_compra
import random
from flask import Flask, render_template, request, flash, redirect, url_for 

app = Flask(__name__)

#ruta inicio

@app.route('/')


#pestañas
@app.route('/inicio')
def index():
    return render_template('index.html')

@app.route('/Registrarse')
def registrarse_html():
    return render_template('Registrarse.html')

@app.route('/Agregar_peluche_desc')
def add_peluche_desc_html():
    return render_template('Agregar_peluche_desc.html')

@app.route('/Agregar_peluche')
def add_peluche_html():
    return render_template('Agregar_peluche.html')  

@app.route('/Carrito_compras')
def carrito_html():
        datos = Mantenedor_carrito.consultar()
        return render_template('Carrito_compras.html', carrito_add = datos)

@app.route('/Descuentos')
def descuento_html():
    return render_template('Descuentos.html')

@app.route('/catalogo')
def catalogo_html():
    return render_template('catalogo.html')

@app.route('/editar_datos')
def editar_datos_html():
    return render_template('editar_datos.html')

@app.route('/Lista_deseos')
def lista_deseo_html():
    datos = Mantenedor_lista_deseo.consultar()
    return render_template('lista_deseos.html', deseos_add = datos)


@app.route('/lista_peluches_add')
def lista_peluches_add_html():
    datos = Mantenedor_agregar_peluche.consultar()
    return render_template('lista_peluches_add.html', peluches_add = datos)


@app.route('/login')
def login_html():
    return render_template('login.html')

@app.route('/Proceso_compra')
def proceso_compra_html():
    return render_template('Proceso_compra.html')

@app.route('/venta_frog')
def venta_frog_html():
    return render_template('venta_frog.html')

@app.route('/venta_horse')
def venta_horse_html():
    return render_template('venta_horse.html')

@app.route('/venta_monkey')
def venta_monkey_html():
    return render_template('venta_monkey.html')

@app.route('/venta_perezoso')
def venta_perezoso_html():
    return render_template('venta_perezoso.html')

@app.route('/venta_yoda')
def venta_yoda_html():
    return render_template('venta_yoda.html')

@app.route('/ejemplo')
def ejemplo():
    return render_template('ejemplo.html')

@app.route('/venta_yoshi')
def venta_yoshi_html():
    return render_template('venta_yoshi.html')

@app.route('/editar_peluche')
def editar_peluche_html():
    return render_template('editar_peluche.html')

@app.route('/lista_peluches_add_desc')
def lista_peluches_add_desc_html():
    datos = Mantenedor_agregar_peluche_desc.consultar()
    return render_template('lista_peluches_add_desc.html', peluches_add_desc = datos)

@app.route('/editar_peluche_desc')
def editar_peluche_desc_html():
    return render_template('editar_peluche_desc.html')

#agregar peluche
@app.route('/peluche_mantenedor', methods=['POST'])
def Mantenedor_add_peluche():
    #insertar
    if request.method=='POST':
        try:
            auxbotonInsertar = request.form['Aceptar_btn']
            if auxbotonInsertar == 'Aceptar':
                auxID = request.form['codigo_peluche'] 
                auxNombre = request.form['nombre_peluche_txt']
                auxDescripcion = request.form['descripcion_txt'] 
                auxValor = request.form['valor_txt']
                auxAdd_peluche = Clase_agregar_peluche.agregar_peluche(auxID, auxNombre, auxDescripcion, auxValor)
                Mantenedor_agregar_peluche.insertar(auxAdd_peluche)

                flash('datos guardados')   

        except:
            print('Error')
        return redirect(url_for('add_peluche_html'))

#agregar usuario
@app.route('/registrarse', methods=['POST'])
def Mantenedor_add_user():
    #insertar
    if request.method=='POST':
        try:
            auxbotonInsertar = request.form['Aceptar_btn']
            if auxbotonInsertar == 'Aceptar':
                auxrut = request.form['rut_txt']
                auxnombre= request.form['nombre_txt']
                auxapellido= request.form['apellido_txt']
                auxtelefono = request.form['telefono_txt']
                auxcorreo = request.form['correo_txt']
                auxpass = request.form['pass_txt']
                
                auxadd_user = Clase_usuario.usuario(auxrut, auxnombre, auxapellido, auxtelefono, auxcorreo, auxpass)
                Mantenedor_usuario.insertar(auxadd_user)

                flash('datos guardados')

        except:
            print('Error')
        return redirect(url_for('index'))

#login usuario
@app.route('/login_mantenedor', methods=['POST'])
def login_mantenedor():
    #insertar
    if request.method=='POST':
        try:
            auxbotonInsertar = request.form['Aceptar_btn']
            if auxbotonInsertar == 'Aceptar':
                auxRut = request.form['rut_txt']
                auxNombre = request.form['nombre_txt']
                auxapellido  =request.form['apellido_txt']
                auxtelefono = request.form ['telefono_txt']
                auxcorreo = request.form['correo_txt']
                auxcontraseña = request.form['pass_txt']
                auxusuario = Clase_usuario.usuario(auxRut,auxNombre, auxapellido, auxtelefono, auxcorreo, auxcontraseña)
                Mantenedor_usuario.login(auxusuario)

                flash('datos guardados')
            return 'ok'

        except:
            print('Error')
        return redirect(url_for('index'))
@app.route('/editar_datos', methods=['POST'])
def editar_datos():
        try:
            auxBotonActualizar = request.form['Aceptar_btn']
            if auxBotonActualizar == 'Aceptar':
                auxRut = request.form['rut_txt']
                auxNombre = request.form['nombre_txt']
                auxapellido  =request.form['apellido_txt']
                auxtelefono = request.form ['telefono_txt']
                auxcorreo = request.form['correo_txt']
                auxcontraseña = request.form['pass_txt']
                auxusuario = Clase_usuario.usuario(auxRut,auxNombre, auxapellido, auxtelefono, auxcorreo, auxcontraseña)
                Mantenedor_usuario.actualizar(auxusuario)
                print('datos Actualizados')
                #flash('datos Actualizados')
        except:
            print('datos No Actualizados')
        return redirect(url_for('index'))

#agregar peluche descuento
@app.route('/peluche_descuento_mantenedor', methods=['POST'])
def peluche_descuento_mantenedor():
    #insertar
    if request.method=='POST':
        try:
            auxbotonInsertar = request.form['Aceptar_btn']
            if auxbotonInsertar == 'Aceptar':
                auxID = request.form['codigo_peluche_txt'] 
                auxNombre = request.form['nombre_peluche_txt']
                auxDescripcion = request.form['descripcion_txt'] 
                auxValor = request.form['valor_txt']
                auxDescuento = request.form['Descuento_txt']
                auxAdd_peluche = Clase_agregar_peluche_desc.agregar_peluche_desc(auxID, auxNombre, auxDescripcion, auxValor, auxDescuento)
                Mantenedor_agregar_peluche_desc.insertar(auxAdd_peluche)

                flash('datos guardados')   

        except:
            print('Error')
        return redirect(url_for('add_peluche_desc_html'))


@app.route('/editar_peluche', methods=['POST'])
def editar_peluche():
        #Actualizar
    if request.method=='POST':
        try:
            auxBotonActualizar = request.form['Aceptar_btn']
            if auxBotonActualizar == 'Aceptar':
                auxcodigo = request.form['codigo_peluche']
                auxNombre = request.form['nombre_peluche_txt']
                auxdescripcion = request.form['descripcion_txt']
                auxvalor = request.form['valor_txt']
                auxpeluche = Clase_agregar_peluche.agregar_peluche(auxcodigo,auxNombre, auxdescripcion, auxvalor)
                Mantenedor_agregar_peluche.actualizar(auxpeluche)
                print('datos Actualizados')
                #flash('datos Actualizados')
        except:
            print('datos No Actualizados')
            #flash('datos No Actualizados')

        try:
            auxbotonBorrar = request.form['Eliminar_btn']
            if auxbotonBorrar == 'Eliminar':
                aux_id = request.form['codigo_peluche']
                Mantenedor_agregar_peluche.eliminar(aux_id)

                flash('datos guardados')   
        except:
            print("error insertar")     
   
        return redirect(url_for('lista_peluches_add_html'))

@app.route('/mantenedor_lista_deseos', methods=['POST'])
def mantenedor_lista_deseos():
    #insertar
    if request.method=='POST':
        try:
            auxbotonInsertar = request.form['Aceptar_btn']
            if auxbotonInsertar == 'Aceptar':
                auxcodigo = request.form['codigo_peluche']
                auxnombre= request.form['nombre_peluche_txt']
                auxvalor= request.form['valor_txt']

                
                auxadd_lista = Clase_lista_deseos.lista_deseos(auxcodigo, auxnombre, auxvalor)
                Mantenedor_lista_deseo.insertar(auxadd_lista)

                flash('datos guardados')

        except:
            print('Error')

    #eliminar  
        try:
            auxBotonEliminar = request.form['Eliminar_btn']
            if auxBotonEliminar == 'Eliminar':
                aux_codigo = request.form['codigo_peluche']
                Mantenedor_lista_deseo.eliminar(aux_codigo)
                print('datos Eliminados')
                #flash('datos Eliminados')
        except:
            print('datos No Eliminados')
            #flash('datos No Eliminados') 
    #Actualizar
        try:
            auxBotonActualizar = request.form['Actualizar_btn']
            if auxBotonActualizar == 'Actualizar':
                auxCodigo = request.form['codigo_peluche']
                auxNombre = request.form['nombre_peluche_txt']
                auxValor = request.form['valor_txt']
                aux_actualizar_lista = Clase_lista_deseos.lista_deseos(auxCodigo, auxNombre, auxValor)
                Mantenedor_lista_deseo.actualizar(aux_actualizar_lista)
                print('datos Actualizados')
                #flash('datos Actualizados')
        except:
            print('datos No Actualizados')
            #flash('datos No Actualizados') 
        return redirect(url_for('lista_deseo_html'))

@app.route('/proceso_venta_rana', methods=['POST'])
def proceso_venta_rana():
    #insertar
    if request.method=='POST':
        try:
            auxbotonInsertar = request.form['Aceptar_btn']
            if auxbotonInsertar == 'Aceptar':
                auxcodigo = Mantenedor_carrito.generar_codigo()
                auxnombre= 'Peluche rana'
                auxdesc = 'Peluche de rana bastante alegre que quiere jugar'
                auxvalor= '4990'

                aux_add_rana = Clase_carrito_compras.carrito_compras(auxcodigo, auxnombre, auxdesc, auxvalor)
                Mantenedor_carrito.insertar(aux_add_rana)

                flash('datos guardados')

        except:
            print('Error')
        return redirect(url_for('index'))

@app.route('/proceso_venta_caballo', methods=['POST'])
def proceso_venta_caballo():
    #insertar
    if request.method=='POST':
        try:
            auxbotonInsertar = request.form['Aceptar_btn']
            if auxbotonInsertar == 'Aceptar':
                auxcodigo = Mantenedor_carrito.generar_codigo()
                auxnombre= 'Peluche Caballo'
                auxdesc = 'Un caballo que te acompañara en todas tus aventuras por el oeste'
                auxvalor= '2990'

                aux_add_caballo = Clase_carrito_compras.carrito_compras(auxcodigo, auxnombre, auxdesc, auxvalor)
                Mantenedor_carrito.insertar(aux_add_caballo)

                flash('datos guardados')

        except:
            print('Error')
        return redirect(url_for('index'))

@app.route('/proceso_venta_monkey', methods=['POST'])
def proceso_venta_monkey():
    #insertar
    if request.method=='POST':
        try:
            auxbotonInsertar = request.form['Aceptar_btn']
            if auxbotonInsertar == 'Aceptar':
                auxcodigo = Mantenedor_carrito.generar_codigo()
                auxnombre= 'Peluche Mono'
                auxdesc = 'Descuento especial para el peluche de mono'
                auxvalor= '2500'

                aux_add_caballo = Clase_carrito_compras.carrito_compras(auxcodigo, auxnombre, auxdesc, auxvalor)
                Mantenedor_carrito.insertar(aux_add_caballo)

                flash('datos guardados')

        except:
            print('Error')
        return redirect(url_for('index'))

@app.route('/proceso_venta_perezoso', methods=['POST'])
def proceso_venta_perezoso():
    #insertar
    if request.method=='POST':
        try:
            auxbotonInsertar = request.form['Aceptar_btn']
            if auxbotonInsertar == 'Aceptar':
                auxcodigo = Mantenedor_carrito.generar_codigo()
                auxnombre= 'Peluche Perezoso'
                auxdesc = 'Este peluche te acompañara a dormir todas las noches'
                auxvalor= '4990'

                aux_add_caballo = Clase_carrito_compras.carrito_compras(auxcodigo, auxnombre, auxdesc, auxvalor)
                Mantenedor_carrito.insertar(aux_add_caballo)

                flash('datos guardados')

        except:
            print('Error')
        return redirect(url_for('index'))

@app.route('/proceso_venta_yoda', methods=['POST'])
def proceso_venta_yoda():
    #insertar
    if request.method=='POST':
        try:
            auxbotonInsertar = request.form['Aceptar_btn']
            if auxbotonInsertar == 'Aceptar':
                auxcodigo = Mantenedor_carrito.generar_codigo()
                auxnombre= 'Peluche Yoda'
                auxdesc = 'Original de LucasFilms peluche de yoda en oferta'
                auxvalor= '3000'

                aux_add_caballo = Clase_carrito_compras.carrito_compras(auxcodigo, auxnombre, auxdesc, auxvalor)
                Mantenedor_carrito.insertar(aux_add_caballo)

                flash('datos guardados')

        except:
            print('Error')
        return redirect(url_for('index'))

@app.route('/proceso_venta_yoshi', methods=['POST'])
def proceso_venta_yoshi():
    #insertar
    if request.method=='POST':
        try:
            auxbotonInsertar = request.form['Aceptar_btn']
            if auxbotonInsertar == 'Aceptar':
                auxcodigo = Mantenedor_carrito.generar_codigo()
                auxnombre= 'Peluche Yoshi'
                auxdesc = 'Peluche original de Nintendo en oferta'
                auxvalor= '3500'

                aux_add_caballo = Clase_carrito_compras.carrito_compras(auxcodigo, auxnombre, auxdesc, auxvalor)
                Mantenedor_carrito.insertar(aux_add_caballo)

                flash('datos guardados')

        except:
            print('Error')
        return redirect(url_for('index'))

@app.route('/carrito_compras_mantenedor', methods=['POST'])
def carrito_compras_mantenedor():
    if request.method=='POST':
        try:
            auxBotonEliminar = request.form['Eliminar_btn']
            if auxBotonEliminar == 'Eliminar':
                aux_codigo = request.form['codigo_peluche_txt']
                Mantenedor_carrito.eliminar(aux_codigo)
                print('datos Eliminados')
                #flash('datos Eliminados')
        except:
            print('datos No Eliminados')
            #flash('datos No Eliminados') 
        return redirect(url_for('carrito_html'))

@app.route('/editar_peluche_descuento', methods=['POST'])
def editar_peluche_descuento():
 #eliminar  
        try:
            auxBotonEliminar = request.form['Eliminar_btn']
            if auxBotonEliminar == 'Eliminar':
                aux_codigo = request.form['codigo_peluche']
                Mantenedor_agregar_peluche_desc.eliminar(aux_codigo)
                print('datos Eliminados')
                #flash('datos Eliminados')
        except:
            print('datos No Eliminados')
            #flash('datos No Eliminados') 
    #Actualizar
        try:
            auxBotonActualizar = request.form['Actualizar_btn']
            if auxBotonActualizar == 'Actualizar':
                auxCodigo = request.form['codigo_peluche']
                auxNombre = request.form['nombre_peluche_txt']
                auxDescripcion = request.form['descripcion_txt']
                auxValor = request.form['valor_txt']
                auxdescuento = request.form['descuento_txt']

                aux_actualizar_lista = Clase_agregar_peluche_desc.agregar_peluche_desc(auxCodigo, auxNombre, auxDescripcion, auxValor, auxdescuento)
                Mantenedor_agregar_peluche_desc.actualizar(aux_actualizar_lista)
                print('datos Actualizados')
                #flash('datos Actualizados')
        except:
            print('datos No Actualizados')
            #flash('datos No Actualizados') 
        return redirect(url_for('lista_peluches_add_desc_html'))

@app.route('/transaccion_proceso_compra', methods=['POST'])
def transaccion_proceso_compra():
    if request.method=='POST':
        try:
            Auxaceptar = request.form['Aceptar_btn']
            if Auxaceptar == 'Aceptar':
                aux_codigo = Mantenedor_proceso_compra.generar_codigo()
                aux_tipo = request.form['TIPO_TARJETA']
                aux_numero = request.form['numero_tarjeta_txt']
                aux_año = request.form['año_txt']
                aux_nombre = request.form['nombre_txt']
                aux_verificacion = request.form['verificacion_txt']

                aux_add_proceso = Clase_proceso_compra.proceso_compra(aux_codigo,aux_tipo, aux_numero, aux_año, aux_nombre, aux_verificacion)
                Mantenedor_proceso_compra.insertar(aux_add_proceso)
                Mantenedor_proceso_compra.eliminar()
                print('datos Eliminados')
                #flash('datos Eliminados')
        except:
            print('datos No Eliminados')
            #flash('datos No Eliminados') 
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port = 3000, debug = True)