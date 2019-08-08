from flask import Flask, jsonify

from temperature_storage import TemperatureStorage

app = Flask(__name__)


@app.route('/temperature')
def temperature():
    storage = TemperatureStorage()
    return jsonify(storage.get_all('celsius'))


@app.route('/')
def index():
    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0')
