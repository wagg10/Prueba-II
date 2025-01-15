from flask import Flask, request, jsonify
from inventario import consultar_producto, agregar_producto, actualizar_stock, inventario


app = Flask(__name__)

@app.before_request
def validar_json():
    if request.method in ['POST', 'PUT'] and not request.is_json:
        return jsonify({"error": "El cuerpo de la solicitud debe ser JSON."}), 400

@app.route('/producto/<int:id_producto>', methods=['GET'])
def api_consultar_producto(id_producto):
    resultado = consultar_producto(id_producto)
    if "error" in resultado:
        return jsonify(resultado), 404  # Cambié el código a 404 si no se encuentra el producto
    return jsonify(resultado), 200

@app.route('/producto', methods=['POST'])
def api_agregar_producto():
    datos = request.get_json()
    
    # Validar que los datos requeridos estén presentes
    if "id_producto" not in datos or "cantidad" not in datos:
        return jsonify({"error": "Se requieren 'id_producto' y 'cantidad' en el cuerpo de la solicitud."}), 400
    
    id_producto = datos.get("id_producto")
    cantidad = datos.get("cantidad")
    resultado = agregar_producto(id_producto, cantidad)
    if "error" in resultado:
        return jsonify(resultado), 400  # Devuelve 400 si hay error
    return jsonify(resultado), 200

@app.route('/producto/<int:id_producto>', methods=['PUT'])
def api_actualizar_stock(id_producto):
    datos = request.get_json()
    
    # Validar que los datos requeridos estén presentes
    if "cantidad" not in datos:
        return jsonify({"error": "Se requiere 'cantidad' en el cuerpo de la solicitud."}), 400
    
    nueva_cantidad = datos.get("cantidad")
    try:
        resultado = actualizar_stock(id_producto, nueva_cantidad)
        return jsonify(resultado), 200
    except AssertionError as e:
        return jsonify({"error": str(e)}), 400  # Devuelve 400 si no se cumple el contrato
    except ValueError as e:
        return jsonify({"error": str(e)}), 404  # Devuelve 404 si no se encuentra el producto

@app.route('/inventario', methods=['GET'])
def ver_inventario():
    return jsonify(inventario), 200

@app.route('/')
def home():
    return jsonify({
        "mensaje": "BIENVENIDO A LA API DEL INVENTARIO DE MODAS",
        "endpoints": {
            "GET /producto/<int:id_producto>": "Consulta un producto por su ID.",
            "POST /producto": "Agrega un producto con 'id_producto' y 'cantidad' en el cuerpo.",
            "PUT /producto/<int:id_producto>": "Actualiza la cantidad de un producto existente."
        }
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
