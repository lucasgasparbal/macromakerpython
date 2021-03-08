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
