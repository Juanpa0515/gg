from flask import Flask, render_template, request, redirect, url_for, flash
from flask import Flask, flash
from flask import render_template,request,redirect,url_for,session, Response
from flask_mysqldb import MySQL,MySQLdb,db
from flask import send_from_directory
from datetime import datetime
import os
from sqlalchemy import text

# Importamos Flask y otros módulos necesarios

app = Flask(__name__)

@app.route('/login', methods=["GET", "POST"])
def login():
    # Consultas para obtener la cantidad de usuarios, empleados, clientes y proyectos
    consulta_usuario = text("SELECT COUNT(*) FROM usuario")
    resultado_usuario = db.session.execute(consulta_usuario)
    cantidad_usuarios = resultado_usuario.scalar()

    consulta_cliente = text("SELECT COUNT(*) FROM cliente")
    resultado_cliente = db.session.execute(consulta_cliente)
    cantidad_cliente = resultado_cliente.scalar()


    if request.method == 'POST' and 'correoUsuario' in request.form and 'claveUsuario' in request.form:
       
        _correo = request.form['correoUsuario']
        _password = request.form['claveUsuario']


        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuario WHERE correoUsuario = %s AND claveUsuario = %s', (_correo, _password,))
        account = cur.fetchone()

    if account:
            
            session['logueado'] = True
            session['codigoUsuario'] = account['codigoUsuario']
            session['tipoUsuario'] = account['tipoUsuario']

            if session['tipoUsuario']==1:
                return render_template("app/templates/menuAdministrador.html")
            elif session['tipoUsuario']==2:
                return render_template("app/templates/menuCliente.html")
  
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        _correo = request.form['correoUsuario']
        _contrasena = request.form['claveUsuario']
        _nombre = request.form['nombreCliente']

        # Utiliza MySQL para conectar y ejecutar consultas
        cur = mysql.connection.cursor()

        try:
            # Inserta el usuario en la tabla de usuarios
            cur.execute("INSERT INTO usuario (correoUsuario, claveUsuario, nombreUsuario) VALUES (%s, %s, %s)", (_correo, _contrasena, _nombre))
            mysql.connection.commit()

            # Obtiene el ID del usuario recién registrado
            codigoUsuario = cur.lastrowid

            # Inserta el cliente en la tabla de clientes
            cur.execute("INSERT INTO cliente (nombreCliente, codigoUsuario) VALUES (%s, %s)", (_nombre, Usua_Id))
            mysql.connection.commit()

            cur.close()

            flash('Registro exitoso', 'success')
            return redirect(url_for('/login'))
        except Exception as e:
            # Manejar cualquier excepción que pueda ocurrir durante la inserción
            flash(f'Error: {str(e)}', 'danger')

    return render_template('login/login.html')



app.route('/proceso')
def proceso():
    
    return render_template('')


if __name__== '__main__':
    app.run(debug=True)