from flask import Blueprint, request, redirect, url_for, abort
from app.api.models import Urls
from app.exts import db, id_codec
import secrets
import validators

api = Blueprint("api", __name__)


def _add_schema(url, https=False):
    if not url.startswith("http"):
        url = ("https://" if https else "http://") + url
    return url


@api.post("/")
def index():
    if "shorten" not in request.form:
        abort(400)

    long_url = request.form["shorten"]
    long_url = _add_schema(long_url)

    if not validators.url(long_url):
        abort(400)

    token = secrets.token_urlsafe()
    entry = Urls(url=long_url, token=token)

    db.session.add(entry)
    db.session.commit()

    short_url = id_codec.encode(entry.id)

    return {"shortened": short_url, "token": token}


@api.route("/<entry_hash>", methods=["GET", "DELETE"])
def url_redirect(entry_hash):
    if request.method == "GET":
        entry = _get_entry(entry_hash)
        if entry:
            return redirect(entry.url)

    else:
        return _manage_entry(entry_hash)

    return abort(404)


def _get_entry(short_hash):
    url_id = id_codec.decode(short_hash)

    if not url_id:
        return None

    entry = db.session.get(Urls, url_id)

    if not entry:
        return None

    return entry


def _manage_entry(entry_hash):
    entry = _get_entry(entry_hash)

    if not entry:
        abort(404)

    if "token" not in request.form or not secrets.compare_digest(request.form["token"], entry.token):
        abort(401)

    db.session.delete(entry)
    db.session.commit()
    return "", 204
