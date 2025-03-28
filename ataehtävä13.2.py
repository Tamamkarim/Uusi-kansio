"""Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja
 kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta. Esimerkiksi 
 EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport",
 "Municipality":"Helsinki"}."""

from flask import Flask, Response, jsonify
import json
import mysql.connector

# Database connection
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='lento_peli',
    user='root',
    password='Karim88',
    autocommit=True
)

app = Flask(__name__)

@app.route('/kenttä/<koodi>')
def kenttä(koodi):
    try:
        # Use parameterized query to prevent SQL injection
        sql = "SELECT ICAO, Name, Municipality FROM lentokentat WHERE ICAO = %s"
        cursor = yhteys.cursor()
        cursor.execute(sql, (koodi,))
        tulos = cursor.fetchone()

        if tulos:
            icao, name, municipality = tulos
            vastaus = {"ICAO": icao, "Name": name, "Municipality": municipality}
            return jsonify(vastaus), 200
        else:
            # If no result is found
            vastaus = {"status": "Not Found"}
            return jsonify(vastaus), 404
    except mysql.connector.Error as e:
        # Handle database errors
        vastaus = {"status": "Database Error", "message": str(e)}
        return jsonify(vastaus), 500
    except Exception as e:
        # Handle other unexpected errors
        vastaus = {"status": "Error", "message": str(e)}
        return jsonify(vastaus), 500

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "1234",
        "message": "Not Found Error TK 404"
    }
    return jsonify(vastaus), 404

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


