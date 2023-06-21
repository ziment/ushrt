from flask_sqlalchemy import SQLAlchemy
from hashids import Hashids


class FlaskHashids:
    def __init__(self, app=None):
        self._hashids = None

        if app is not None:
            self.init_app(app)


    def init_app(self, app):
        config = {}
        if "HASHIDS_SALT" in app.config:
            config["salt"] = app.config["HASHIDS_SALT"]

        if "HASHIDS_MIN_LENGTH" in app.config:
            config["min_length"] = app.config["HASHIDS_MIN_LENGTH"]

        if "HASHIDS_ALPHABET" in app.config:
            config["alphabet"] = app.config["HASHIDS_ALPHABET"]

        self._hashids = Hashids(**config)


    def encode(self, *args, **kwargs):
        return self._hashids.encode(*args, **kwargs)


    def decode(self, *args, **kwargs):
        return self._hashids.decode(*args, **kwargs)


db = SQLAlchemy()

id_codec = FlaskHashids()
