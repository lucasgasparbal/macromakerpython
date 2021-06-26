from macromaker.conditionparsing.Condition import Condition


class ConditionsParser:

    def __init__(self):

        self.allegianceCondition = Condition({
            "ally": "help",
            "help": "help",
            "enemy": "harm",
            "harm": "harm"
        })

        self.statusCondition = Condition(
            {
                "alive": "nodead",
                "nodead": "nodead",
                "dead": "dead",
            }
        )

        self.conditions = [self.allegianceCondition, self.statusCondition]

    def parse(self, stringList):
        parsedConditions = []

        for condition in self.conditions:
            for string in stringList:
                string.lower()
                condition.checkForCondition(string)

            parsedCondition = condition.write()
            if parsedCondition:
                parsedConditions.append(parsedCondition)
            condition.clear()

        return parsedConditions

    def getRules(self):
        return [("If one or more given conditions conflict with each other "
                "(for example, both mouseover and player are passed as targets in the same condition block) "
                "then the first one is selected."), "If more than one of the same condition are given the repeats are "
                                                   "ignored."]
