from app.models import app, db
from flask import jsonify, request
from app.models.productos import Products
from app.models.carrito import Carts
from app.models.compras import Shopping


@app.route("/", methods=["GET"])
def main():
    return jsonify({'message': 'Hello'}), 200


@app.route("/Products", methods=["GET"])
def get_products():
    products = Products.query.all()
    all_products: list = []
    for product in products:
        product_data = {
            "id_product": product.id_product,
            "name": product.name,
            "quantity": product.quantity
        }
        all_products.append(product_data)
    return jsonify(all_products), 200


@app.route("/Products", methods=["POST"])
def add_new_product():
    if not request.is_json:
        return jsonify({"error": "Los datos no están en formato JSON, no se agregó el producto"}), 400

    data = request.get_json()
    new_product = Products(name=data['name'], quantity=data['quantity'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Producto agregado correctamente"}), 201


@app.route("/Carts", methods=["GET"])
def get_carts():
    carts = Carts.query.all()
    all_carts: list = []
    for cart in carts:
        cart_data = {
            "id_cart": cart.id_cart,
            "product_id": cart.product_id,
            "quantity": cart.quantity
        }
        all_carts.append(cart_data)
    return jsonify(all_carts), 200


@app.route("/Carts", methods=["POST"])
def add_new_cart():
    if not request.is_json:
        return jsonify({"error": "Los datos no están en formato JSON, no se agregó el carrito"}), 400

    data = request.get_json()
    new_cart = Carts(product_id=data['id_product'], quantity=data['quantity'])
    db.session.add(new_cart)
    db.session.commit()
    return jsonify({"message": "Carrito agregado correctamente"}), 201


@app.route("/Carts/<int:id_cart>/add_product", methods=["PUT"])
def add_product_to_cart(id_cart):
    if not request.is_json:
        return jsonify({"error": "Los datos no están en formato JSON, no se pudo agregar el producto al carrito"}), 400

    data = request.get_json()

    cart = Carts.query.filter_by(id_cart=id_cart).first()

    if not cart:
        return jsonify({"error": "Carrito no encontrado"}), 404

    existing_cart_item = Carts.query.filter_by(id_cart=id_cart, product_id=data['id_product']).first()

    if existing_cart_item:
        existing_cart_item.quantity += data['quantity']
        db.session.commit()
        return jsonify({"message": "Cantidad del producto actualizada en el carrito"}), 200
    else:
        new_cart_item = Carts(product_id=data['id_product'], quantity=data['quantity'])
        db.session.add(new_cart_item)
        db.session.commit()
        return jsonify({"message": "Producto agregado al carrito"}), 201
