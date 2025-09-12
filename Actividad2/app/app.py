
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    message = os.getenv("MESSAGE", "hola mundo")
    release = os.getenv("RELEASE", "v0")
    return jsonify({"message": message, "release": release})

print(">>> app.py cargado")  # <-- debug 1

if __name__ == "__main__":
    print(">>> entrando a __main__")  # <-- debug 2
    port = int(os.getenv("PORT", 8080))
    print(f">>> arrancando en 0.0.0.0:{port}  MESSAGE={os.getenv('MESSAGE')}  RELEASE={os.getenv('RELEASE')}")
    app.run(host="0.0.0.0", port=port)
