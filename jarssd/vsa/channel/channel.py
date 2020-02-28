

# base class for channels

class Channel:
    def __init__(self, vsa, name):
        # vsa: keep a reference to main object
        self.vsa   = vsa
        self._name = name

    def select(self):
        self.vsa.write(f"INST '{self.name}'")

    # name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        # dare we try the impossible?
        scpi       = f"INST:REN '{self._name}', '{new_name}'"
        self.vsa.write(scpi)
        self._name = new_name

    # type
    @property
    def type(self):
        return self.vsa._type_for_channel()[self.name]
