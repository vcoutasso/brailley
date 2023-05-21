from translator.translator import Translator
from reader.reader import Reader


class Brailley:
    _translator: Translator
    _reader: Reader

    def __init__(self, translator: Translator, reader: Reader):
        self._translator = translator
        self.reader = reader

    def capture_and_display(self):
        input_string = self._reader.read()
        self._translator.translate(input_string)
