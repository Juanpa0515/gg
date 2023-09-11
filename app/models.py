from app import db
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Text, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class Producto(db.Model):
    __tablename__="producto"
    codigoProducto = db.Column(db.Integer, primary_key = True, autoincrement = True )
    nombreProducto = db.Column(db.String(50), nullable = False)
    precioVentaProducto = db.Column(db.DECIMAL(10, 2), nullable = False)
    unidadMedidaProducto = db.Column(db.String(25), nullable = False)
    stockProducto = db.Column(db.DECIMAL(10,2), nullable = False)
    descripcionProducto = db.Column(db.Text, nullable = False)

class Usuario(db.Model):
    __tablename__="usuario"
    codigoUsuario = db.Column(db.Integer, primary_key = True, autoincrement = True )
    correoUsuario = db.Column(db.String(100), nullable = False)
    nombreUsuario = db.Column(db.String(32), nullable = False)
    claveUsuario = db.Column(db.String(32), nullable = False)
    tipoUsuario = db.Column(db.String(50), nullable = False)

class Cliente(db.Model):
    __tablename__="cliente"
    codigoCliente = db.Column(db.Integer, primary_key = True, autoincrement = True )
    identificacionCliente = db.Column(db.String(20), nullable = False)
    tipoIdentificacionCliente = db.Column(db.String(15), nullable = False)
    nombreCliente = db.Column(db.String(50), nullable = False)
    telefonoCliente = db.Column(db.String(15), nullable = False)
    direccionCliente = db.Column(db.String(50), nullable = False)
    telefono2Cliente = db.Column(db.String(15), nullable = False)
    correoCliente = db.Column(db.String(50), nullable = False)
    codigoUsuarioFK = db.Column(Integer, ForeignKey('usuario.codigoUsuario'))

class Venta(db.Model):
    __tablename__="venta"
    codigoVenta = db.Column(db.Integer, primary_key = True, autoincrement = True )
    fechaVenta = db.Column(db.Date, nullable = False)
    cantidadVenta = db.Column(db.DECIMAL(10, 2), nullable = False)
    totalVenta = db.Column(db.DECIMAL(10, 2), nullable = False)
    codigoProductoFK = db.Column(Integer, ForeignKey('producto.codigoProducto'))

class Administrador(db.Model):
    __tablename__="administrador"
    codigoAdministrador = db.Column(db.Integer, primary_key = True, autoincrement = True )
    identificacionAdministrador = db.Column(db.String(20), nullable = False)
    tipoIdentificacionAdministrador = db.Column(db.String(15), nullable = False)
    nombreAdministrador = db.Column(db.String(50), nullable = False)
    apellidoAdministrador = db.Column(db.String(50), nullable = False)
    celularAdministrador = db.Column(db.String(15), nullable = False)
    direccionAdministrador = db.Column(db.String(50), nullable = False)
    codigoUsuarioFK = db.Column(Integer, ForeignKey('usuario.codigoUsuario'))
    codigoVentaFK = db.Column(Integer, ForeignKey('venta.codigoVenta'))
