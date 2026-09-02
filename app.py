from flask import Flask, request, jsonify, send_file
from ml import get_recommendation

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/style.css")
def style():
    return send_file("style.css")

@app.route("/script.js")
def script():
    return send_file("script.js")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    text = data.get("message", "")
    history = data.get("history", [])
    reply = get_recommendation(text, history)
    return jsonify({
        "reply": reply
    })

if __name__ == "__main__":
    app.run(debug=True)