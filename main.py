from flask import Flask, render_template, session, request, redirect, url_for
import db
from models import Tarea
from datetime import date, datetime


app = Flask(__name__)


@app.route('/')
def home():
    tareas_hoy = db.session.query(Tarea).filter(Tarea.fecha_alerta == date.today()).all()
    print (tareas_hoy)
    return render_template("index.html")

@app.route('/form_nueva_tarea')
def formulario_tarea():
    return render_template("form_nueva_tarea.html")

@app.route('/grabar_tarea', methods=["POST"])
def grabar_tarea():
    tarea = Tarea(titulo=request.form["titulo"],
              contenido=request.form["contenido"],
              fecha_alta = date.today(),
              fecha_alerta=datetime.strptime(request.form["fecha_alerta"], '%Y-%m-%d'),
              realizada = False)

    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for('home'))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
