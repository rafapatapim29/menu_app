from flask import Flask, render_template

app = Flask(__name__, static_folder="static")

# El menu se simula con una lista de diccionarios
menu = [
    {"nombre": "Snack 1", "precio": 20},
    {"nombre": "Snack 2", "precio": 30},
    {"nombre": "Snack 3", "precio": 40}
]


@app.route("/")
def index():
    return render_template("index.html", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
# Para ejecutar la aplicación, guarda este archivo como app.py
