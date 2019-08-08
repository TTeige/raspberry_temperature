import time

from temperature_reader import TemperatureReader
from temperature_storage import TemperatureStorage


def run():
    reader = TemperatureReader()
    storage = TemperatureStorage()
    while True:
        reader.update_temperature()
        stored = storage.store(reader.celsius, 'celsius')
        print(stored)
        print(reader.celsius)
        time.sleep(60)


if __name__ == '__main__':
    run()
