from flask import Flask

import app.models
from app.api import health_bp
from app.core.config import Config
from app.core.extensions import db, migrate


def create_app() -> Flask:
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(health_bp)
    print(app.config["SQLALCHEMY_DATABASE_URI"])

    return app