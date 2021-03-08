import unittest
from macromaker.Statement import Statement
from macromaker.StatementCondition import StatementCondition
from macromaker.NoSpellException import NoSpellException



class MyTestCase(unittest.TestCase):

    def test01EmptyStatementWithoutSpellRaisesException(self):
        statement = Statement()
        self.assertRaises(NoSpellException, statement.write)

    def test02StatementWithOnlySpellWritesSpellOnly(self):
        statement = Statement()
        statement.addSpell("Riptide")

        self.assertEqual("Riptide", statement.write())

    def test03StatementWithConditionsButNoSpellRaisesException(self):
        statement = Statement()
        statementCondition = StatementCondition()
        statementCondition.setConditions(["help", "nodead"])
        statement.addConditions(statementCondition)

        self.assertRaises(NoSpellException,statement.write)

    def test04StatementWithConditionsAndSpellWritesCorrectly(self):
        statement = Statement()
        statementCondition = StatementCondition()
        statementCondition.setTarget("mouseover")
        statementCondition.setConditions(["help", "nodead"])
        statement.addConditions([statementCondition])
        statement.addSpell("Riptide")

        self.assertEqual("[@mouseover, help, nodead] Riptide", statement.write())

    def test05StatementWithMoreThanOneConditionsAndSpellWritesCorrectly(self):
        statement = Statement()

        statementConditionA = StatementCondition()
        statementConditionA.setTarget("mouseover")
        statementConditionA.setConditions(["help", "nodead"])

        statementConditionB = StatementCondition()
        statementConditionB.setTarget("target")
        statementConditionB.setConditions(["harm","nodead"])

        statement.addConditions([statementConditionA,statementConditionB])
        statement.addSpell("Riptide")

        self.assertEqual("[@mouseover, help, nodead][@target, harm, nodead] Riptide", statement.write())

    def test06StatementWithMoreThanOneConditionsAndOneEmptyConditionAndSpellWritesCorrectly(self):
        statement = Statement()

        statementConditionA = StatementCondition()
        statementConditionA.setTarget("mouseover")
        statementConditionA.setConditions(["help", "nodead"])
        statement.addConditions(statementConditionA)

        statementConditionB = StatementCondition()
        statementConditionB.setTarget("target")
        statementConditionB.setConditions(["harm","nodead"])
        statement.addConditions(statementConditionB)

        statementConditionC = StatementCondition()

        statement.addConditions([statementConditionA, statementConditionB, statementConditionC])
        statement.addSpell("Riptide")

        self.assertEqual("[@mouseover, help, nodead][@target, harm, nodead][] Riptide", statement.write())
