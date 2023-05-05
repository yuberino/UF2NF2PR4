from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/inicio")
def inici():
    return render_template("inicio.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/submit", methods=["POST"])
def submit():
    global variable
    variable = True
    nombre = request.form.get("nombre")
    return render_template("enviado.html", nombre=nombre, variable=variable)

@app.route("/productos")
def productos():
    return render_template("productos.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


if __name__ == "__main__":
    app.run(debug=True)