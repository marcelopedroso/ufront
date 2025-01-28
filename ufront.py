from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Frontend HTML/Página inicial.

@app.route("/api/data")
def get_data():
    node_red_url = "http://localhost:1880/api"  # Ajuste para o endpoint do Node-RED.
    data = requests.get(node_red_url).json()  # Consumindo a API do Node-RED
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

#teste