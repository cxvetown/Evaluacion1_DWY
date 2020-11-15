#programa de arranque
import Mantenedor_agregar_peluche, Mantenedor_carrito
import Clase_agregar_peluche, Clase_carrito_compras
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
    return render_template('lista_deseos.html')

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

@app.route('/venta_bunny')
def venta_bunny_html():
    return render_template('venta_bunny.html')

@app.route('/venta_cobaya')
def venta_cobaya_html():
    return render_template('venta_cobaya.html')

@app.route('/venta_elephant')
def venta_elephant_html():
    return render_template('venta_elephant.html')

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

@app.route('/venta_yoshi')
def venta_yoshi_html():
    return render_template('venta_yoshi.html')

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
        return redirect(url_for('index'))
    #Eliminar
def Mantenedor_delete_peluche():
    if request.method=='POST':
        try:
            auxbotonBorrar = request.form['Eliminar_btn']
            if auxbotonBorrar == 'Eliminar':
                aux_id = request.form['codigo_peluche']
                Mantenedor_agregar_peluche.eliminar(aux_id)

                flash('datos guardados')   
            return redirect(url_for('index'))

        except:
            print("error insertar")   



if __name__ == '__main__':
    app.run(port = 3000, debug = True)