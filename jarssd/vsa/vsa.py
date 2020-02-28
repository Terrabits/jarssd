from .channel import AnalogDemodulation, Channel, Spectrum, Type
from jarssd   import Instrument


class VSA(Instrument):
    @property
    def channels(self):
        return list(self._type_for_channel().keys())

    def create_channel(self, type=Type.SPECTRUM, name=None):
        if not name:
            name = self._next_channel_name()
        self.write(f"INST:CRE {type},'{name}'")
        return name

    def channel(self, name):
        if name not in self.channels:
            raise KeyError(f"Channel name '{name}' does not exist")

        type = self._type_for_channel()[name]
        if type == 'SANALYZER':
            return Spectrum(self, name)
        if type == 'ADEM':
            return AnalogDemodulation(self, name)
        # default?
        return Channel(self, name)

    # private-ish stuff

    # dict[name] => type
    def _type_for_channel(self):
        response = self.query('INST:LIST?')
        list     = response.strip().split(',')
        names    = list[1::2]  # even
        types    = list[::2]   # odd
        type_for_channel = dict()
        for name, type in zip(names, types):
            type_for_channel[name] = type
        return type_for_channel

    def _next_channel_name(self):
        i      = 1
        name_i = 'Ch{0}'
        while name_i.format(i) in self.channels:
            i += 1
        return name_i.format(i)
