from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from src.database.settings import db
from src.routes.users_routes import users_routes_bp
from src.server.config import config

app = Flask(__name__)


jwt = JWTManager()
migrate = Migrate()

app.register_blueprint(users_routes_bp, url_prefix='/users')

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    return jsonify({"message": "Token has expired", "error": "token_expired"}), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return (
        jsonify(
                {"message": "Signature verification failed", "error": "invalid_token"}
            ),
            401,
        )
@jwt.unauthorized_loader
def missing_token_callback(error):
    return (
        jsonify(
            {
                "message": "Request doesnt contain valid token",
                "error": "authorization_header",
            }
        ),
        401,
    )

def create_app(config_mode):
    app.config.from_object(config[config_mode])
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    return app
    