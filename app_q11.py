# app_q11.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/search", methods=["GET"])
def search_q11():
    query_q11 = request.args.get("q", "")
    return jsonify({"result": f"You searched for: {query_q11}"})

if __name__ == "__main__":
    app.run(debug=True, port=5001)