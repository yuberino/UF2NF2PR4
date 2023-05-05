from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/inicio")
def inici():
    return render_template("inicio.html")

if __name__ == "__main__":
    app.run(debug=True)