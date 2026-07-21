from flask import Flask

import app.models

from app.api import auth_bp, health_bp
from app.core.config import Config
from app.core.extensions import db, migrate, jwt
from app.routes.queue import queue_bp

def create_app() -> Flask:
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(queue_bp)
    print(app.config["SQLALCHEMY_DATABASE_URI"])

    return app