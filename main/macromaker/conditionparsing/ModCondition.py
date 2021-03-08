
class ModCondition:
    ALT = "alt"
    SHIFT = "shift"
    CTRL = "ctrl"

    def __init__(self):
        self.keyDictionary = {
            self.ALT: False,
            self.SHIFT: False,
            self.CTRL: False
        }
        self.string = ""

    def addMod(self, modString):
        comparisonString = modString.lower()
        for key in self.keyDictionary.keys():
            self.addModifierKey(comparisonString, key)

    def addModifierKey(self, comparisonString, keyString):
        if (comparisonString == keyString) and not self.keyDictionary.get(keyString):
            self.keyDictionary.update({keyString: True})
            if not self.string:
                self.string = "mod:" + keyString
            else:
                self.string = self.string + "+" + keyString

    def write(self):
        return self.string
