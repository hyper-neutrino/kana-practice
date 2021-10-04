import json

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def serve_root():
    return "Hello, World!"

with open("data.json", "r") as f:
    data = json.load(f)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5375, debug = True)
