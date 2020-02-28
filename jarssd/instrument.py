class Instrument:
    def open(self, address):
        pass

    def read(self):
        return ''

    def write(self, string):
        pass

    def query(self, string):
        self.write(string)
        return self.read()

    @property
    def errors(self):
        return self.query('SYST:ERR:ALL?').strip()
