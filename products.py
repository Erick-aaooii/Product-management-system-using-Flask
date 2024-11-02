# Importações
from flask import Blueprint, request, jsonify
from users import token_required  
import db_manager as db  # Importa o db_manager

products_bp = Blueprint('products', __name__)

# Carrega os produtos do arquivo ao iniciar
products = db.load_data('data/products.json') 

# Adiciona produtos
@products_bp.route('/products/set', methods=['POST'])
@token_required
def set_products(current_user):
    data = request.json
    name = data.get("name")
    price = data.get("price")
    quantity = data.get("quantity")

    if not name or not price:
        return jsonify({"response": False, "message": "Nome, preço e quantidade são obrigatórios!"}), 400

    # Cria um novo produto
    new_product = {
        "id": len(products) + 1, 
        "name": name,
        "price": price,
        "quantity": quantity
    }
    products.append(new_product)

    # Salva os produtos no arquivo
    db.save_data('data/products.json', products)

    return jsonify({"response": True, "message": "Produto adicionado com sucesso!", "product": new_product}), 201

# pega um produt do products.json
@products_bp.route('/products/get/<int:product_id>', methods=['GET'])
@token_required
def get_products(current_user, product_id):
    
    product = next((prod for prod in products if prod["id"] == product_id), None)

    if product is None:
        return jsonify({"response": False, "message": "Produto não encontrado!"}), 404

    return jsonify({"response": True, "product": product}), 200

# deleta produto
@products_bp.route('/products/delete/<int:product_id>', methods=['DELETE'])
@token_required
def delete_products(current_user, product_id):
    global products  # Referencia a lista de produtos globalmente
    product = next((prod for prod in products if prod["id"] == product_id), None)

    if product is None:
        return jsonify({"response": False, "message": "Produto não encontrado!"}), 404

    products = [prod for prod in products if prod["id"] != product_id] 

    # salva
    db.save_data('data/products.json', products)

    return jsonify({"response": True, "message": "Produto deletado com sucesso!"}), 200

# atualiza produto
@products_bp.route('/products/update/<int:product_id>', methods=['PUT'])
@token_required
def update_products(current_user, product_id):
    data = request.json
    product = next((prod for prod in products if prod["id"] == product_id), None)

    if product is None:
        return jsonify({"response": False, "message": "Produto não encontrado!"}), 404

    name = data.get("name")
    price = data.get("price")
    quantity = data.get("quantity")
    
    # atualiza com base na informação que for dada
    if name:
        product["name"] = name
    if price is not None:  
        product["price"] = price
    if quantity is not None: 
        product["quantity"] = quantity

    # Salva 
    db.save_data('data/products.json', products)

    return jsonify({"response": True, "message": "Produto atualizado com sucesso!", "product": product}), 200
