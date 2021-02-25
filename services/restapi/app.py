from flask import Flask, jsonify, request
from cars_api import cars_bp

app = Flask(__name__)

API_PREFIX = '/api/v1/{app_route}'

app.register_blueprint(cars_bp, url_prefix=API_PREFIX.format(app_route='cars'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

