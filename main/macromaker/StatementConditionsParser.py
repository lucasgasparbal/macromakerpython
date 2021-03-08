from macromaker.StatementCondition import StatementCondition
from macromaker.conditionparsing.ConditionParser import ConditionsParser
from macromaker.conditionparsing.ModConditionParser import ModConditionParser
from macromaker.conditionparsing.TargetParser import TargetParser


class StatementConditionsParser:
    CONDITIONSPLITFLAG = "|"

    def __init__(self):
        self.conditionsParser = ConditionsParser()
        self.modConditionParser = ModConditionParser()
        self.targetParser = TargetParser()

    def parseConditions(self, inputText):
        text = inputText.lower()
        conditionBlocks = text.split(self.CONDITIONSPLITFLAG)

        statementConditions = []
        for conditionBlock in conditionBlocks:

            if not conditionBlock and not statementConditions:
                continue

            conditions = conditionBlock.split()
            statementConditionBlock = StatementCondition()

            statementConditionBlock.setConditions(self.conditionsParser.parse(conditions))
            statementConditionBlock.setModifierConditions(self.modConditionParser.parse(conditions))
            statementConditionBlock.setTarget(self.targetParser.parse(conditions))
            statementConditions.append(statementConditionBlock)

        return statementConditions
