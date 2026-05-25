from flask import Flask, render_template
from route import mis_rutas

app=Flask(__name__)

app.register_blueprint(mis_rutas, url_prefix="/API")

@app.route("/")
def bienvenida():
    return render_template("index.html", nombre="Capybara")


if __name__ == "__main__":
    app.run(port=5000, debug= True)