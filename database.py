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

def get_profile(user, password):
    try:
        cur = get_db()
        user_data = cur.execute("""SELECT u_userName,
                                           u_email,
                                           n_name
                                      FROM user,
                                           userProfile,
                                           nation
                                     WHERE upr_userKey = u_userkey AND 
                                           upr_nationKey = n_nationKey AND 
                                           u_userName = ? AND 
                                           u_passcode = ?;
                                    """, (user, password)).fetchone()
        if user_data is None:
            return None
        else:
            return user_data
    except sqlite3.Error as error:
        print(error)


def get_all_songs():
    try:
        cur = get_db()
        music_data = cur.execute("""SELECT * FROM music; """).fetchall()
        if music_data is None:
            return None
        else:
            return music_data
    except sqlite3.Error as error:
        print(error)


def get_playlist_songs(playlist):
    """
    FIXME: Need to find a query to return the music in the selcted playlist name
    :param playlist: playlist name in the database
    :return: list of songs
    """
    try:
        cur = get_db()
        music_data = cur.execute("""SELECT * FROM music; """).fetchall()
        if music_data is None:
            return None
        else:
            return music_data
    except sqlite3.Error as error:
        print(error)