from flask import Blueprint, render_template

front = Blueprint("front", __name__)


@front.get("/")
def index():
    return render_template("index.html")
