class ConditionOptionHelpInfo:

    def __init__(self, keys, macroKey, description):
        self.keys = keys
        self.macroValue = macroKey
        self.description = description

    def getHelpInfo(self):
        calls = self.keys.copy()
        string = "\n[" + calls.pop()
        for call in calls:
            string = string + " or " + call
        string = string + "]\n" + "  Macro value:" + self.macroValue + \
                 "\n  Description: " + self.description

        return string
