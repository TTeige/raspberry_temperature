from flask import Flask, request, render_template

from temperature_storage import TemperatureStorage

app = Flask(__name__)


@app.route('/temperature')
def temperature():
    storage = TemperatureStorage()
    n = request.args.get('n')
    if n is None:
        n = -1
    else:
        n = 0 - int(n)
    n = int(n)
    return render_template('temperature.html', temperatures=storage.get_all('celsius')[n:])


@app.route('/')
def index():
    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0')
