from flask import (Flask, render_template, request, session)
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
            return render_template('login.html')
        else:
            session['user'] = user
            return render_template('profile.html', text=data)
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
