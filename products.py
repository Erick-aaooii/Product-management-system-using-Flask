from flask import Blueprint, request, jsonify
from users import token_required  # Importa o token_required do módulo de usuários

products_bp = Blueprint('products', __name__)

# Lista para armazenar produtos (substitua por um banco de dados em produção)
products = []

# Rota para adicionar produtos (protegida)
@products_bp.route('/products', methods=['POST'])
@token_required
def set_products(current_user):
    data = request.json
    name = data.get("name")
    price = data.get("price")

    # Verifica se o nome e o preço estão presentes
    if not name or not price:
        return jsonify({"response": False, "message": "Nome e preço são obrigatórios!"}), 400

    # Cria um novo produto
    new_product = {
        "id": len(products) + 1, 
        "name": name,
        "price": price
    }
    products.append(new_product)

    return jsonify({"response": True, "message": "Produto adicionado com sucesso!", "product": new_product}), 201

# Rota para obter um produto específico (protegida)
@products_bp.route('/products/<int:product_id>', methods=['GET'])
@token_required
def get_products(current_user, product_id):
    
    # Busca o produto pelo ID
    product = next((prod for prod in products if prod["id"] == product_id), None)

    if product is None:
        return jsonify({"response": False, "message": "Produto não encontrado!"}), 404

    return jsonify({"response": True, "product": product}), 200

# Rota para deletar produtos (protegida)
@products_bp.route('/products/delete/<int:product_id>', methods=['DELETE'])
@token_required
def delete_products(current_user, product_id):
    global products  # Referencia a lista de produtos globalmente
    product = next((prod for prod in products if prod["id"] == product_id), None)

    if product is None:
        return jsonify({"response": False, "message": "Produto não encontrado!"}), 404

    products = [prod for prod in products if prod["id"] != product_id]  # Remove o produto da lista
    return jsonify({"response": True, "message": "Produto deletado com sucesso!"}), 200

# Rota para atualizar produtos (protegida)
@products_bp.route('/products/update/<int:product_id>', methods=['PUT'])
@token_required
def update_products(current_user, product_id):
    data = request.json
    product = next((prod for prod in products if prod["id"] == product_id), None)

    if product is None:
        return jsonify({"response": False, "message": "Produto não encontrado!"}), 404

    name = data.get("name")
    price = data.get("price")

    # Atualiza os campos se eles foram fornecidos
    if name:
        product["name"] = name
    if price is not None:  # Verifica se o preço foi fornecido
        product["price"] = price

    return jsonify({"response": True, "message": "Produto atualizado com sucesso!", "product": product}), 200
