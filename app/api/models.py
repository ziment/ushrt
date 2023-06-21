from app.exts import db


class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text)
    token = db.Column(db.Text)
