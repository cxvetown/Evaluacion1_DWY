#Este es el programa de arranque
import mantenedorCliente
import claseCliente
from flask import Flask,render_template,request,flash,redirect,url_for

app = Flask(__name__)

#se rutean el home

@app.route('/')

def Index():
    #return 'Holi'
    datos = mantenedorCliente.consultar()
    return render_template('MantenedorCliente.html',clientes=datos)
    #return render_template('MantenedorCliente.html')

@app.route('/mantenedor',methods = ['POST'])

def mantenedor():
    if request.method == 'POST':
        #Insertar
        try:
            auxBotonInsertar = request.form['btoInsertar']
            if auxBotonInsertar == 'Insertar':
                auxRut = request.form['txtRut']
                auxNombre = request.form['txtNombre']
                auxCliente = claseCliente.Cliente(auxRut,auxNombre)
                mantenedorCliente.insertar(auxCliente)
                print('datos guardados')
                #flash('datos guardados')
        except:
            print('datos No guardados')
            #flash('datos No guardados')
        #Actualizar
        try:
            auxBotonActualizar = request.form['btoActualizar']
            if auxBotonActualizar == 'Actualizar':
                auxRut = request.form['txtRut']
                auxNombre = request.form['txtNombre']
                auxCliente = claseCliente.Cliente(auxRut,auxNombre)
                mantenedorCliente.actualizar(auxCliente)
                print('datos Actualizados')
                #flash('datos Actualizados')
        except:
            print('datos No Actualizados')
            #flash('datos No Actualizados')
        #Eliminar
        try:
            auxBotonEliminar = request.form['btoEliminar']
            if auxBotonEliminar == 'Eliminar':
                auxRut = request.form['txtRut']
                mantenedorCliente.eliminar(auxRut)
                print('datos Eliminados')
                #flash('datos Eliminados')
        except:
            print('datos No Eliminados')
            #flash('datos No Eliminados')
        return redirect(url_for('Index'))    





if __name__ == '__main__':
    app.run(port=3000,debug=True)
