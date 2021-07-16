from macromaker.conditionparsing.CategoryAndConditionsInfoMaker import CategoryAndConditionsInfoMaker
from macromaker.conditionparsing.ConditionOption import ConditionOption


class TargetParser:
    def __init__(self):

        player = ConditionOption(["self","player"],"player","Makes your character the target of the spell")
        focus = ConditionOption(["focus"], "focus, exists", "Casts the spell on your focus if you have one, otherwise "
                                                            "casts it "
                                                  "on the default target")
        mouseover = ConditionOption(["mouseover", "mouse"], "mouseover, exists", "Casts the spell only if "
                                                                                        "there is a target on your "
                                                                                        "cursor")
        self.targets = [player, focus, mouseover]

    def parse(self, stringsToParse):

        for string in stringsToParse:
            for targetCondition in self.targets:
                parsedString = targetCondition.evaluate(string)
                if parsedString:
                    return parsedString

        return ""

    def getRules(self):
        return ["There can only be one target per condition block."]

    def getCategoriesAndConditions(self):
        categoryAndConditionsInfoMaker = CategoryAndConditionsInfoMaker()
        return categoryAndConditionsInfoMaker.categoryAndConditionsInfo("Cast Target", self.targets)
