from flask import Flask
from users import users_bp
from products import products_bp
import secrets 

app = Flask(__name__)
#Cria uma chave secreta que nem eu sei
app.config['SECRET_KEY'] = secret_key = secrets.token_hex(32)

# Registra os blueprints dos módulos e dividi o códigos
app.register_blueprint(users_bp)
app.register_blueprint(products_bp)

if __name__ == '__main__':
    app.run(debug=True)
