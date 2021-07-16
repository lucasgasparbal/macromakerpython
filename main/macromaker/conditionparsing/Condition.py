from macromaker.conditionparsing.CategoryAndConditionsInfoMaker import CategoryAndConditionsInfoMaker


class Condition:
    def __init__(self, name, options):
        self.conditionSelected = ""
        self.options = options
        self.name = name

    def checkForCondition(self, string):
        for option in self.options:
            optionEvaluation = option.evaluate(string)
            if not self.conditionSelected and optionEvaluation:
                self.conditionSelected = optionEvaluation

    def write(self):
        return self.conditionSelected

    def clear(self):
        self.conditionSelected = ""


    def getCategoriesAndConditions(self):
        categoryAndConditionsInfoMaker = CategoryAndConditionsInfoMaker()
        return categoryAndConditionsInfoMaker.categoryAndConditionsInfo(self.name, self.options)