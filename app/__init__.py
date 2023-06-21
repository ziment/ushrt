from flask import Flask
from config import Config

from app.exts import db, id_codec
from app.api.routes import api
from app.front.routes import front


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    id_codec.init_app(app)

    app.register_blueprint(api)
    app.register_blueprint(front)

    with app.app_context():
        db.create_all()

    return app
