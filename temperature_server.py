from flask import Flask

from temperature_storage import TemperatureStorage

storage = TemperatureStorage()

app = Flask(__name__)
app.run(host='0.0.0.0')


@app.route('/temperature')
def temperature():
    return storage.get_all('celsius')


@app.route('/')
def index():
    return ''
