import unittest
from macromaker.StatementCondition import StatementCondition
from macromaker.conditionparsing.ModCondition import ModCondition


class TestStatement(unittest.TestCase):

    def test01StatementConditionWithoutConditionsOrTargetReturnsEmptyBrackets(self):
        statementCondition = StatementCondition()

        self.assertEqual("[]", statementCondition.write())

    def test02StatementConditionAddingTargetAddsTargetToTheString(self):
        statementCondition = StatementCondition()
        statementCondition.setTarget("player")
        self.assertEqual("[@player]", statementCondition.write())

    def test03StatementConditionAddingTargetWithATargetAlreadyAddedDoesntReplaceTheFirstOne(self):
        statementCondition = StatementCondition()
        statementCondition.setTarget("player")
        statementCondition.setTarget("target")
        self.assertEqual("[@player]", statementCondition.write())

    def test04StatementWithoutTargetDisplaysAssignedConditionsCorrectly(self):
        statementCondition = StatementCondition()
        statementCondition.setConditions(["help","nodead"])

        self.assertEqual("[help, nodead]",statementCondition.write())

    def test05StatementWithoutTargetDisplaysASingleConditionCorrectly(self):
        statementCondition = StatementCondition()
        statementCondition.setConditions(["help"])

        self.assertEqual("[help]",statementCondition.write())

    def test06StatementWithoutTargetDoesntRepeatAnAlreadyAddedCondition(self):
        statementCondition = StatementCondition()
        statementCondition.setConditions(["help","help"])

        self.assertEqual("[help]",statementCondition.write())

    def test07StatementWithoutTargetDoesntRepeatAnAlreadyAddedCondition(self):
        statementCondition = StatementCondition()
        statementCondition.setConditions(["help","help"])

        self.assertEqual("[help]",statementCondition.write())

    def test08StatementWithTargetAndConditionsDisplaysCorrectly(self):
        statementCondition = StatementCondition()
        statementCondition.setTarget("target")
        statementCondition.setConditions(["help","nodead","exists"])

        self.assertEqual("[@target, help, nodead, exists]",statementCondition.write())

    def test09StatementWithTargetConditionsAndModifiersDisplaysCorrectly(self):
        statementCondition = StatementCondition()
        statementCondition.setTarget("target")
        statementCondition.setConditions(["help","nodead","exists"])
        modifiers = ModCondition()
        modifiers.addMod("alt")
        statementCondition.setModifierConditions(modifiers)

        self.assertEqual("[@target, help, nodead, exists, mod:alt]",statementCondition.write())