import unittest
from macromaker.conditionparsing.Condition import Condition


class ConditionTest(unittest.TestCase):
    def test01EmptyConditionWritesAnEmptyString(self):
        condition = Condition({})

        self.assertEqual("", condition.write())

    def test02ConditionWithDictionaryWritesCorrectoCondition(self):
        condition = Condition({"help": "help"})

        condition.checkForCondition("help")

        self.assertEqual("help", condition.write())

    def test03ConditionWithDictionaryWritesCorrectoCondition(self):
        condition = Condition({"help": "help"})

        condition.checkForCondition("help")

        self.assertEqual("help", condition.write())

    def test04ConditionWithDictionaryDisregardsCapitalization(self):
        condition = Condition({"help": "help"})

        condition.checkForCondition("hElP")

        self.assertEqual("help", condition.write())

    def test05ConditionWithDictionaryDoesNotChangeTheConditionIfAnotherValidOptionIsGiven(self):
        condition = Condition({"help": "help",
                               "harm": "harm"})

        condition.checkForCondition("help")
        condition.checkForCondition("harm")

        self.assertEqual("help", condition.write())

    def test06ConditionWithDictionaryWritesEmptyStringAfterClear(self):
        condition = Condition({"help": "help",
                               "harm": "harm"})

        condition.checkForCondition("help")
        condition.clear()

        self.assertEqual("", condition.write())

    def test07ConditionWithDictionaryWritesSecondConditionIfTheFirstIsCleared(self):
        condition = Condition({"help": "help",
                               "harm": "harm"})

        condition.checkForCondition("help")
        condition.clear()
        condition.checkForCondition("harm")

        self.assertEqual("harm", condition.write())


if __name__ == '__main__':
    unittest.main()
