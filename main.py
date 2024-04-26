from flask import Flask, render_template, session, request, redirect, url_for
import db
from models import Tarea


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/form_nueva_tarea')
def formulario_tarea():
    return render_template("form_nueva_tarea.html")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
