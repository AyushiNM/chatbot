from distutils.log import debug
from email import message
from urllib import response
from flask import Flask, jsonify, render_template, request
from infer import get_response

app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("base.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    print("Hi!")
    response = get_response(text, "firstaid")
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug = True)
