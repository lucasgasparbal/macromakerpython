from macromaker.conditionparsing.ModCondition import ModCondition

class ModConditionParser:

    def __init__(self):
        self.MODCONDITIONS = {
            "alt": "alt",
            "control": "ctrl",
            "ctrl": "ctrl",
            "shift": "shift"
        }

    def parse(self, stringsToParse):
        parsedModCondition = ModCondition()
        for string in stringsToParse:
            string.lower()
            parsedString = self.MODCONDITIONS.get(string)
            if parsedString:
                parsedModCondition.addMod(parsedString)

        return parsedModCondition

    def getRules(self):
        return [
            "You can have more than one modifier applied, up to alt+ctrl+shift. Repeats of the same key are ignored."]