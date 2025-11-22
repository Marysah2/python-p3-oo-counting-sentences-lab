class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value  # use the setter to validate

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, str):
            print("The value must be a string.")
            return
        self._value = val

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        import re
        # split by '.', '?', '!' followed by optional spaces
        sentences = re.split(r'[.!?]+(?:\s|$)', self._value)
        # remove empty strings
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)
