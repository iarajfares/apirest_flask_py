from flask import Flask,jsonify,request, url_for
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from config import config


app = Flask(__name__)
CORS(app)
conexion=MySQL(app)

# Rutas de la app # 
# Mostrar todos los productos # 
@cross_origin
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

# Verificar si un producto existe. (REALIZADO POR CYNTHIA FERNANDEZ, POR UN ERROR SE ELIMINO EL COMMIT.)
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
        VALUES ('{0}', '{1}', '{2}', {3})""".format(request.json['idproductos'], request.json['productos_name'], request.json['productos_descripcion'], request.json['productos_precio'])
        cursor.execute(sql)
        conexion.connection.commit() # confirma la accion de agregar
        return jsonify({'Mensaje':"Producto registrado correctamente"})
    except Exception as ex:
       print(f"Error: {ex}")
       return jsonify({"Error": str(ex)})


# Actualizar productos #
@app.route('/productos/<idproductos>', methods=['PUT'])
def actualizar_producto(idproductos):
    try:
        cursor = conexion.connection.cursor()
        if producto_existe(idproductos):
            sql = """UPDATE productos SET productos_name = '{0}', productos_precio = '{1}' 
            WHERE idproductos = '{2}'""".format(request.json['productos_name'], request.json['productos_precio'], request.json['idproductos'])
            cursor.execute(sql)
            conexion.connection.commit() # confirma la accion de agregar
            return jsonify({'Mensaje':"Producto actualizado correctamente"})
        else:
            return jsonify({'Mensaje'"Producto no encontrado"})
    except Exception as ex:
        return jsonify({"Error"})

# Eliminar productos #
@app.route('/productos/<idproductos>', methods=['DELETE'])
def eliminar_producto(idproductos):
    try:
        cursor = conexion.connection.cursor()
        if producto_existe(idproductos):
            sql = "DELETE FROM productos WHERE idproductos = '{0}'".format(idproductos)
            cursor.execute(sql)
            conexion.connection.commit()
            return jsonify({'Mensaje':"Producto eliminado."})
        else:
            return jsonify({'Mensaje':"Producto no encontrado"})
    except Exception as ex:
        return jsonify({"Error"})

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
