import glob
import os


class TemperatureReader:
    def __init__(self):
        # Sketchy but ok
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')
        self.device_file = glob.glob('/sys/bus/w1/devices/' + '28*')
        if len(self.device_file) > 0:
            self.device_file = self.device_file[0] + '/w1_slave'
        self.celsius = 0.
        self.fahrenheit = 0.

    def update_temperature(self):
        self._convert_temp(self._read_temp())

    def _convert_temp(self, lines):
        try:
            if lines[0].strip()[-3:] != 'YES':
                return

            temperature_pos = lines[1].find('t=')

            if temperature_pos != -1:
                temp_string = lines[1][temperature_pos + 2:]
                self.celsius = float(temp_string) / 1000.0
                self.fahrenheit = self.celsius * 9.0 / 5.0 + 32.0
        except IndexError:
            return ""

    def _read_temp(self):
        if len(self.device_file) > 0:
            if not os.path.exists(self.device_file):
                return ""
        else:
            return ""
        with open(self.device_file, 'r') as f:
            lines = f.readlines()
        return lines
