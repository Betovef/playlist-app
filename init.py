from flask import (Flask, render_template, request,
                   session, redirect, url_for, json)
import database

app = Flask(__name__, template_folder='static/templates')
app.config.from_mapping(
        SECRET_KEY='dev'
    )

with app.app_context():
    database.init_db()


@app.route('/login', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        data = database.get_profile(user, password)
        if data is None:
            return render_template('login.html', error="Invalid credentials")
        else:
            session['user'] = user
            session['password'] = password
            return redirect(url_for('profile'))
    return render_template('login.html')


@app.route('/profile', methods=['GET'])
def profile():
    data = database.get_profile(session['user'], session['password'])
    return render_template("profile.html", profile=data)


@app.route('/music', methods=['GET'])
def music():
    if request.method == 'POST':
        playlist = request.form['playlist_name']
        print(playlist)
        music_data = database.get_playlist_songs(playlist)
        return render_template("music.html", data=music_data)
    else:
        music_data = database.get_all_songs()
        return render_template("music.html", data=music_data)


# @app.route('/search_music', methods=['GET'])
# def music():
#     song = request.form['input']
#     music_data = database.get_song(song)
#     return render_template("music.html", data=music_data)



# @app.route('/login', methods=['GET', 'POST'])
# @app.route('/', methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run(debug=True)
