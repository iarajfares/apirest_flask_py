from flask import Flask,jsonify,request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from config import config


app = Flask(__name__)
CORS(app)
conexion= MySQL(app)

# Mostrar todos los productos # 
@app.route('/productos', methods=['GET'])
def listar_productos():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT idproductos, productos_name, productos_descripcion, productos_precio FROM productos"
        cursor.execute(sql)
        datos = cursor.fetchall()
        productos = []
        for fila in datos:
            producto = {'idproductos':fila[0], 'productos_name':fila[1], 'productos_descripcion':fila[2], 'productos_precio':fila[3]}
            productos.append(producto)
        return jsonify({'Productos':productos, 'Mensaje':"Productos disponibles"})
    except Exception as ex:
        return jsonify({'Mensaje':"Error"})

# Mostrar un solo producto por ID #
@app.route('/productos/<idproductos>', methods=['GET'])
def leer_producto(idproductos):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT idproductos, productos_name, productos_descripcion, productos_precio FROM productos WHERE idproductos = '{0}'".format(idproductos)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            producto = {'idproductos': datos[0], 'productos_name': datos[1], 'productos_descripcion': datos[2], 'productos_precio': datos[3]}
            return jsonify({'Producto': producto, 'Mensaje': "Producto encontrado."})
        else: 
            return jsonify({'Mensaje': "Producto no encontrado."})
    except Exception as ex:
        return jsonify({'Mensaje':"Error"})
def pagina_no_encontrada(error):
    return "<h1>Pagina no encontrada.</h1>", 404

# Verificar si un producto existe. (REALIZADO POR MARY GALINDO, POR UN ERROR SE ELIMINO EL COMMIT.)
def producto_existe(idproductos):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT idproductos FROM productos WHERE idproductos = '{0}'".format(idproductos)
        cursor.execute(sql)
        return cursor.fetchone() is not None
    except Exception as ex:
        print('Error')
        return False 

# Agregar productos #
@app.route('/productos', methods=['POST'])
def registrar_producto():
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO productos (idproductos, productos_name, productos_descripcion, productos_precio)
        VALUES (%s, %s, %s, %s)"""
        cursor.execute(sql, (
            request.form['idproductos'],
            request.form['productos_name'],
            request.form['productos_descripcion'],
            request.form['productos_precio']
        ))
        conexion.connection.commit()
        return jsonify({'mensaje':"producto registrado."})
    except Exception as ex:
        return jsonify({'mensaje':"error"})

# Actualizar productos #
@app.route('/productos/<idproductos>', methods=['PUT'])
def actualizar_producto(idproductos):
    if producto_existe(idproductos):
        try:
            cursor = conexion.connection.cursor()
            sql = """UPDATE productos SET productos_name = %s, productos_descripcion = %s, productos_precio = %s 
            WHERE idproductos = %s"""
            cursor.execute(sql, {
                request.form['productos_name'],
                request.form['productos_descripcion'],
                request.form['productos_precio'],
                idproductos
            })
            conexion.connection.commit() # confirma la accion de agregar
            return jsonify({'mensaje':'Producto actualizado correctamente'})
        except Exception as ex:
            return jsonify({'mensaje':"Error al actualizar"})
    else:
        return jsonify({"Producto no encontrado"})

# Eliminar productos #
@app.route('/productos/<idproductos>', methods=['DELETE'])
def eliminar_producto(idproductos):
    if producto_existe(idproductos):
        try:
            cursor = conexion.connection.cursor()
            sql = "DELETE FROM productos WHERE idproductos = '{0}'".format(idproductos)
            cursor.execute(sql)
            conexion.connection.commit()
            return jsonify(["Producto eliminado."])
        except Exception as ex:
            return jsonify(["Error"])
    else:
        return jsonify(["Producto no encontrado"])

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
