from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "message": "Servidor Python funcionando!"
    })


@app.route("/api/test")
def test():
    return jsonify({
        "success": True,
        "message": "API funcionando!"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
