# app/routes.py
from flask import Blueprint, request, jsonify
from .models import create_user, get_users, get_user, update_user, delete_user

api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def home():
    return "API  it's okay!"

# cria usuario
@api_bp.route('/usuarios', methods=['POST'])
def criar_usuario():
    data = request.json
    if not data:
        return jsonify({'error': 'Dados ausentes'}), 400

    try:
        user_id = create_user(data)
        return jsonify({'id': user_id, 'message': 'Usuário criado com sucesso!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Listar todos os usuários
@api_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    try:
        users = get_users()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Lista usuário por ID
@api_bp.route('/usuarios/<int:user_id>', methods=['GET'])
def obter_usuario(user_id):
    try:
        user = get_user(user_id)
        if user:
            return jsonify(user), 200
        else:
            return jsonify({'error': 'Usuário não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Atualiza usuário por ID
@api_bp.route('/usuarios/<int:user_id>', methods=['PUT'])
def atualizar_usuario(user_id):
    data = request.json
    if not data:
        return jsonify({'error': 'Dados ausentes'}), 400

    try:
        updated_rows = update_user(user_id, data)
        if updated_rows:
            return jsonify({'message': 'Usuário atualizado com sucesso!'}), 200
        else:
            return jsonify({'error': 'Usuário não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Deleta usuário por ID
@api_bp.route('/usuarios/<int:user_id>', methods=['DELETE'])
def deletar_usuario(user_id):
    try:
        deleted_rows = delete_user(user_id)
        if deleted_rows:
            return jsonify({'message': 'Usuário deletado com sucesso!'}), 200
        else:
            return jsonify({'error': 'Usuário não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
