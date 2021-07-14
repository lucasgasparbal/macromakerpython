class ConditionOption:
    def __init__(self, keys,macroKey,description):
        self.keys = keys
        self.macroValue = macroKey
        self.description = description

    def evaluate(self, string):
        for key in self.keys:
            if string.lower() == key:
                return self.macroValue
        return ""

    def getConditionHelpInfo(self):
        calls = self.keys.copy()
        string = "\n" + calls.pop()
        for call in calls:
            string = string + " or " + call
        string = string + "\n\n" + "Macro value:" + self.macroValue + \
                 "\n\n" + self.description
        return string
