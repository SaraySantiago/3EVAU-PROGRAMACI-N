# servidor (API REST simple con Flask)
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify({"message": "Hola desde el servidor"}), 200

if __name__ == "__main__":
    app.run(port=5000)
