from .channel import Channel


class AnalogDemodulation(Channel):
    # bandwidth
    @property
    def bandwidth_Hz(self):
        self.select()
        return float(self.vsa.query('SENS:BWID:DEM?'))

    @bandwidth_Hz.setter
    def bandwidth_Hz(self, value):
        self.select()
        self.vsa.write(f'SENS:BWID:DEM {value}')
