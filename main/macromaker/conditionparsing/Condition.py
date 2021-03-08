class Condition:
    def __init__(self, optionsDictionary):
        self.conditionSelected = ""
        self.optionsDictionary = optionsDictionary

    def checkForCondition(self, string):
        conditionOption = self.optionsDictionary.get(string.lower())
        if not self.conditionSelected and conditionOption:
            self.conditionSelected = conditionOption

    def write(self):
        return self.conditionSelected

    def clear(self):
        self.conditionSelected = ""
