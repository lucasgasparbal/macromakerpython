from macromaker.conditionparsing.ConditionOptionHelpInfo import ConditionOptionHelpInfo


class ConditionOption:
    def __init__(self, keys, macroKey, description):
        self.keys = keys
        self.macroValue = macroKey
        self.description = description
        self.helpInfo = ConditionOptionHelpInfo(keys, macroKey, description)

    def evaluate(self, string):
        for key in self.keys:
            if string.lower() == key:
                return self.macroValue
        return ""

    def getConditionHelpInfo(self):
        return self.helpInfo.getHelpInfo()
