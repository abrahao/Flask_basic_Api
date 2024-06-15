# app/__init__.py
from flask import Flask
from .db import init_db

def create_app():
    app = Flask(__name__)

    # Inicializa o banco de dados
    init_db(app)

    # Importa e registra rotas
    from .routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app
