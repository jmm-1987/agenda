from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea
from datetime import date, datetime, timedelta
from db import session


app = Flask(__name__)

@app.route('/')
def home():
    hoy = datetime.today().date()
    manana = hoy + timedelta(days=1)
    lista_hoy = db.session.query(Tarea).filter(Tarea.fecha_alerta == hoy).all()
    lista_proxima = db.session.query(Tarea).filter(Tarea.fecha_alerta >= manana).all()


    return render_template("index.html", lista_hoy = lista_hoy, lista_proxima = lista_proxima, hoy=hoy)

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
@app.route('/borrar_tarea/<id>', methods=["POST", "GET"])
def borrar_tarea(id):
    registro_borrar = db.session.query(Tarea).filter_by(id=id).first()
    db.session.delete(registro_borrar)
    db.session.commit()
    return redirect(url_for('home'))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
