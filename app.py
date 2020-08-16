import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

@app.route("/")
def index():
  return 'Hello World'

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)