import unittest
from unittest.mock import MagicMock

from macromaker.conditionparsing.Condition import Condition


class ConditionTest(unittest.TestCase):
    def test05ConditionWithDictionaryDoesNotChangeTheConditionIfAnotherValidOptionIsGiven(self):
        mockOne = MagicMock()
        mockTwo = MagicMock()
        mockOne.evaluate.return_value = "help"
        mockTwo.evaluate.return_value = "harm"
        condition = Condition([mockOne,mockTwo])

        condition.checkForCondition("help")
        condition.checkForCondition("harm")

        self.assertEqual("help", condition.write())

    def test06ConditionWithDictionaryWritesEmptyStringAfterClear(self):
        mockOne = MagicMock()
        mockOne.evaluate.return_value = "help"
        condition = Condition([mockOne])

        condition.checkForCondition("help")
        condition.clear()

        self.assertEqual("", condition.write())

    def test07ConditionWithDictionaryWritesSecondConditionIfTheFirstIsCleared(self):
        mockOne = MagicMock()
        mockTwo = MagicMock()
        mockOne.evaluate.return_value = "help"
        mockTwo.evaluate.return_value = "harm"

        condition = Condition([mockOne, mockTwo])
        condition.checkForCondition("help")
        condition.clear()
        mockOne.evaluate.return_value = ""
        condition.checkForCondition("harm")

        self.assertEqual("harm", condition.write())


if __name__ == '__main__':
    unittest.main()
