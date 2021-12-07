from flask import (Flask)
import database

app = Flask(__name__, template_folder='static/templates')
app.config.from_mapping(
        SECRET_KEY='dev'
    )


with app.app_context():
    database.init_db()


if __name__ == '__main__':
    app.run(debug=True)
