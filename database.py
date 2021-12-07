import sqlite3
from flask import current_app, g


def init_db():
    db = get_db()

    with current_app.open_resource('create-schema-tpch.sql') as f:
        db.executescript(f.read().decode('utf8'))


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('tpch.db')
    return db


def close_db(e=None):
    db = g.pop('tpch', None)
    if db is not None:
        db.close()