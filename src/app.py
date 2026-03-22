from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="practica_db"
        )
        return "<h1>Hola Mundo desde Docker</h1><p>Conexion exitosa a MySQL</p>"
    except Exception as e:
        return f"<h1>Error de conexion</h1><p>{e}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)