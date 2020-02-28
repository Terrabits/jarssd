from .channel import Channel


class Spectrum(Channel):
    # center frequency
    @property
    def center_frequency_Hz(self):
        self.select()
        return self.vsa.query(f'SENS:FREQ:CENT?')

    @center_frequency_Hz.setter
    def center_frequency_Hz(self, value):
        self.select()
        self.vsa.write(f'SENS:FREQ:CENT {value}')
