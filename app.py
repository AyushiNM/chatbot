from distutils.log import debug
from email import message
from urllib import response
from flask import Flask, jsonify, render_template, request
from infer import get_response

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


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
