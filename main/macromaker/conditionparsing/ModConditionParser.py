from macromaker.conditionparsing.CategoryAndConditionsInfoMaker import CategoryAndConditionsInfoMaker
from macromaker.conditionparsing.ConditionOption import ConditionOption
from macromaker.conditionparsing.ModCondition import ModCondition


class ModConditionParser:

    def __init__(self):
        alt = ConditionOption(["alt"], "alt", "Casts the macro if the 'alt' key is held.")
        ctrl = ConditionOption(["ctrl", "control"], "ctrl", "Casts the macro if the 'control' key is held.")
        shift = ConditionOption(["shift"], "shift", "Casts the macro if the 'shift' key is held.")
        self.modConditionsOption = [alt, ctrl, shift]

    def parse(self, stringsToParse):
        parsedModCondition = ModCondition()
        parsedString = ""
        for string in stringsToParse:
            for condition in self.modConditionsOption:
                possibleString = condition.evaluate(string)
                if possibleString:
                    parsedString = possibleString
            if parsedString:
                parsedModCondition.addMod(parsedString)

        return parsedModCondition

    def getRules(self):
        return [
            "You can have more than one modifier key, up to alt+ctrl+shift."]

    def getCategoriesAndConditions(self):
        categoryAndConditionsInfoMaker = CategoryAndConditionsInfoMaker()
        return categoryAndConditionsInfoMaker.categoryAndConditionsInfo("Key Modifiers", self.modConditionsOption)
