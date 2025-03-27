"""Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei. Hyödynnä toteutuksessa
aiempaa tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa:
http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}."""

from flask import Flask, jsonify
import math

app = Flask(__name__)

def is_prime(n):
    """Tarkistaa, onko luku alkuluku."""
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

@app.route("/")
def index():
    return jsonify({"Viesti": "Tervetuloa Alkuluku-API:iin! Käytä /alkuluku/<numero> tarkistaaksesi, onko numero alkuluku."})

@app.route("/alkuluku/<int:luku>")
def alkuluku(luku):
    return jsonify({"numero": luku, "isPrime": is_prime(luku)})

@app.route("/favicon.ico")
def favicon():
    return "", 204

if __name__ == "__main__":
    app.run(port=3000, debug=True)

