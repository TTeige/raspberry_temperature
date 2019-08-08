from temperature_storage import TemperatureStorage


def run():
    storage = TemperatureStorage()
    [print(i) for i in storage.get_all('celsius')[-10:]]


if __name__ == '__main__':
    run()
