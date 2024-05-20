from flask import request, jsonify, Blueprint
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt
from src.composer.users_register_composer import users_register_composer
from src.composer.users_authenticate_composer import users_authenticate_composer
from src.composer.users_logout_composer import users_logout_composer
from src.composer.users_list_composer import users_list_composer
from src.validators.users_schema import validate_user_data
from src.validators.users_authenticate_schema import validate_user_authenticate_data

users_routes_bp = Blueprint('users', __name__)

@users_routes_bp.route('/create', methods=['POST'])
def create():
    data = request.json
    try:
        validate_user_data(data)
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        controller = users_register_composer()
        user = controller.register(name, email, password)
        return jsonify(user), 201
    except ValidationError as errors:
        return jsonify({'errors':errors.messages}), 400
    except Exception as exception:
        return jsonify({'error': str(exception)}), 400
    
@users_routes_bp.route('/login', methods=['POST'])
def authenticate():
    data = request.json
    try:
        validate_user_authenticate_data(data)
        email = data.get('email')
        password = data.get('password')
        controller = users_authenticate_composer()
        user = controller.authenticate(email, password)
        return jsonify(user), 200
    except ValidationError as errors:
        return jsonify({'errors':errors.messages}), 400
    except Exception as exception:
        return jsonify({'error': str(exception)}), 400
    
@users_routes_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    try:
        jti = get_jwt()['jti']
        controller = users_logout_composer()
        controller.logout(jti)
        return jsonify({'message':'Logout successful'}), 200
    except Exception as exception:
        return jsonify({'error': str(exception)}), 400

@users_routes_bp.route('/list', methods=['GET'])
@jwt_required()
def list_users():
    try:
        controller = users_list_composer()
        users = controller.all_users()
        return jsonify(users), 200
    except Exception as exception:
        return jsonify({'error': str(exception)}), 400