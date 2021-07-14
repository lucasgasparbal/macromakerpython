class Condition:
    def __init__(self, options):
        self.conditionSelected = ""
        self.options = options

    def checkForCondition(self, string):
        for option in self.options:
            optionEvaluation = option.evaluate(string)
            if not self.conditionSelected and optionEvaluation:
                self.conditionSelected = optionEvaluation

    def write(self):
        return self.conditionSelected

    def clear(self):
        self.conditionSelected = ""
