from enum import Enum


# Types are taken from
# `INSTrument:LIST?` documentation:
# https://www.rohde-schwarz.com/webhelp/FSW_HTML_UserManuals_en/FSW_HTML_UserManuals_en_CSH.htm#Topic=Content/7e60c7ba2d6241b1.htm|OpenType=Javascript

class Type(Enum):
    SPECTRUM            = 'SANALYZER'
    ANALOG_DEMODULATION = 'ADEM'
    # ...

    def __str__(self):
        return self.value
