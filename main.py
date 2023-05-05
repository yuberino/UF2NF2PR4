from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
@app.route("/inicio")
def inici():
    return render_template("inicio.html")


@app.route("/servicios")
def servicios():
    return render_template("servicios.html")


@app.route("/submit_servicio", methods=["POST"])
def submit():
    global variable1
    variable1 = True
    nombre = request.form.get("nombre")
    return render_template("enviadoServicio.html", nombre=nombre, variable1=variable1)


@app.route("/submit_contacto", methods=["POST"])
def submit2():
    global variable2
    variable2 = True
    nombre = request.form.get("nombre")
    return render_template("enviadoContacto.html", nombre=nombre, variable2=variable2)


@app.route("/productos")
def productos():
    return render_template("productos.html")


@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


if __name__ == "__main__":
    app.run(debug=True)
