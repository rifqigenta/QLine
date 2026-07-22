from flask import Flask

import app.models

from app.api import (
    auth_bp,
    health_bp,
    queue_bp,
    events_bp,
)
from app.core.config import Config
from app.core.extensions import db, migrate, jwt
from app.exceptions import register_error_handlers

from flask_cors import CORS

def create_app() -> Flask:
    app = Flask(__name__)
    
    CORS(
        app,
        resources={
            r"/api/*": {
                "origins": "http://localhost:5173",
            },
            r"/shops/*": {
                "origins": "http://localhost:5173",
            },
        },
    )

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    register_error_handlers(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(queue_bp)
    app.register_blueprint(events_bp)
    print(app.config["SQLALCHEMY_DATABASE_URI"])

    return app