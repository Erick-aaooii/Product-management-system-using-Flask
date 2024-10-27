from flask import Flask
from users import users_bp
from products import products_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'

# Registra os blueprints dos módulos
app.register_blueprint(users_bp)
app.register_blueprint(products_bp)

if __name__ == '__main__':
    app.run(debug=True)
