#importações
from flask import Blueprint, request, jsonify, current_app
import jwt
import datetime
from functools import wraps
import db_manager as db

users_bp = Blueprint('users', __name__)
users = db.load_data('data/users.json')


# verificar token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'response': False, 'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = next((user for user in users if user['email'] == data['email']), None)
        except jwt.ExpiredSignatureError:
            return jsonify({'response': False, 'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'response': False, 'message': 'Invalid token!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated


# login com token 
@users_bp.route('/user/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = next((user for user in users if user['email'] == email and user['password'] == password), None)
    if not user:
        return jsonify({"response": False, "message": "Invalid email or password"}), 401

    token = jwt.encode({
        'email': user['email'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, current_app.config['SECRET_KEY'], algorithm="HS256")

    return jsonify({"response": True, "token": token}), 200

# cadastra novo user
@users_bp.route('/user/new', methods=['POST'])
def set_user():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    name = data.get("name")

    if any(user['email'] == email for user in users):
        return jsonify({"response": False, "message": "User already registered"}), 200

    new_user = {
        "name": name,
        "email": email,
        "password": password,
    }
    users.append(new_user)
    db.save_data('data/users.json', users)
    return jsonify({"response": True, "message": "User registered successfully"}), 201

# rota para o perfil do user
@users_bp.route('/user/profile', methods=['GET'])
@token_required
def get_user_profile(current_user):
    return jsonify({
        "response": True,
        "user": {
            "name": current_user['name'],
            "email": current_user['email']
        }
    }), 200
