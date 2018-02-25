from flask import Flask, Blueprint
from .. import app as default_app
from flask_sqlalchemy import SQLAlchemy
from .config import config


def create_app(*, app, config):
    _app = app or Flask(__name__)
    users = Blueprint('users', __name__)
    _app.config = {**_app.config, **config}
    _app.register_blueprint(users)
    return _app


def generate_db(*, app):
    db = SQLAlchemy(app)
    return db


def init_db(*, db):
    from .models import users # noqa
    db.create_all()
    import pdb; pdb.set_trace()
    return db


app = create_app(app=default_app, config=config)
db = generate_db(app=app)
init_db(db=db)
