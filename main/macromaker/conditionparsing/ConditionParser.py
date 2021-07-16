from macromaker.conditionparsing.Condition import Condition
from macromaker.conditionparsing.ConditionOption import ConditionOption


class ConditionsParser:

    def __init__(self):
        allyOption = ConditionOption(["ally", "help"], "help", "Casts the macro if its target is an ally.")
        enemyOption = ConditionOption(["enemy", "harm"], "harm", "Casts the macro if its target is an enemy.")
        allegianceCondition = Condition("Target Allegiance", [allyOption, enemyOption])

        aliveOption = ConditionOption(["alive", "nodead"], "nodead", "Casts the macro if its target is alive.")
        deadOption = ConditionOption(["dead"], "dead", "Casts the macro if its target is dead.")
        statusCondition = Condition("Target Status", [aliveOption, deadOption])

        self.conditions = [allegianceCondition, statusCondition]

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
                 "then the first one is selected.")]

    def getCategoriesAndConditions(self):
        categoriesAndConditions = {}

        for condition in self.conditions:
            categoriesAndConditions.update(condition.getCategoriesAndConditions())

        return categoriesAndConditions
