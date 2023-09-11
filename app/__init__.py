#Dependencia de flask
from flask import Flask, render_template,url_for
#Dependencia de configuración
from .config import Config
#dependencia de modelo
from flask_sqlalchemy import SQLAlchemy
#dependencia para las migraciones 
from flask_migrate import Migrate


#crear el objeto flask
app = Flask(__name__)

#Configuracion del objeto flask
app.config.from_object(Config)


#Importar el modulo venta
from app.venta import venta_blueprint

#Vincular submodulos del proyecto
app.register_blueprint(venta_blueprint)

#Importar el modulo producto
from app.producto import producto_blueprint

#Vincular submodulos del proyecto
app.register_blueprint(producto_blueprint)

#Importar el modulo cliente
from app.cliente import cliente_blueprint

#Vincular submodulos del proyecto
app.register_blueprint(cliente_blueprint)



#Crear el objetto de Moldelos
db = SQLAlchemy(app)

#Crear objeto de migración
migrate = Migrate(app,db)

@app.route('/')
def index():
    return render_template('index.html' )

@app.route('/login')
def login():
    return render_template('login.html' )

@app.route('/menuAdministrador')
def menuAdministrador():
    return render_template('menuAdministrador.html' )

@app.route('/menuCliente')
def menuCliente():
    return render_template('menuCliente.html' )

@app.route('/verProducto')
def verProducto():
    return render_template('verProducto.html' )

@app.route('/contactenos')
def contactenos():
    return render_template('contactenos.html' )

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html' )

@app.route('/productos')
def productos():
    return render_template('productos.html' )



#importar los modelos  de .models
from .models import Producto,Usuario,Cliente,Venta,Administrador