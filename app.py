from app import Flask, render_template, request, redirect, url_for, flash

#dependencia de modelo
from flask_sqlalchemy import SQLAlchemy

from .config import Config

#dependencia de modelo
from flask_sqlalchemy import SQLAlchemy

#Configuracion del objeto flask
app.config.from_object(Config)

#creamos una aplicacion
app=Flask(__name__)

app.secret_key = "VelaDanAik123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/VENTAS_EN_LINEA'  # Reemplaza con tu contraseña si es necesaria
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



app.register_blueprint(cliente_blueprint, url_prefix='/clientes')
app.register_blueprint(administrador_blueprint, url_prefix='/administrador')


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'VENTAS_EN_LINEA'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
db = SQLAlchemy(app)


@app.route('/')
def inicio():
    return render_template('/index.html')

@app.route('/login')
def mostrar_login():
    return render_template('login/login.html')

@app.route('/dashboard-proyectos')
def mostrar_dashboardproyectos():

    return render_template('/Dashboard-Admin/proyectos/index.html')

@app.route('/dashboard-srv-create')
def mostrar_dashboardservicioscreate():

    return render_template('/Dashboard-Admin/servicios/create.html')

@app.route('/dashboard-proy-create')
def mostrar_dashboardproycreate():

    return render_template('/Dashboard-Admin/proyectos/create.html')

@app.route('/dashboard-admin')
def mostrar_dashboardadmin():

    return render_template('/Dashboard-Admin/admin_Dashboard.html')

@app.route('/dashboard-clie')
def mostrar_dashboardemple():

    return render_template('/Dashboard-Admin/clientes/index.html')

@app.route('/dashboard-clie-create')
def mostrar_dashboardemplecreate():

    return render_template('/Dashboard-Admin/clientes/create.html')

@app.route('/dashboard-emp')
def mostrar_dashboardemp():

    return render_template('/Dashboard-Empleado/index.html')

@app.route('/dashboard-cli')
def mostrar_dashboardcli():

    return render_template('/Dashboard-Cliente/Clie-Dashboard.html')

@app.route('/dashboard-emp-create')
def mostrar_dashboardempcreate():

    return render_template('/Dashboard-Admin/empleados/create.html')

@app.route('/admin-chat')
def mostrar_adminchat():

    return render_template('/Dashboard-Admin/chat.html')

@app.route('/admin-profile')
def mostrar_adminedit():

    return render_template('/Dashboard-Admin/administrador/edit.html')

@app.route('/logout')
def logout():
    session.clear()
    return render_template('/index.html')


    
    return render_template('')

if __name__=="__main__":
    app.run(debug=True, port=5000)
