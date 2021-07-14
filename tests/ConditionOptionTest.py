import unittest
from macromaker.conditionparsing.ConditionOption import ConditionOption


class ConditionOptionTest(unittest.TestCase):
    def test01EmptyConditionOptionWritesAnEmptyString(self):
        conditionOption = ConditionOption([], "", "")

        self.assertEqual("", conditionOption.evaluate("help"))

    def test02ConditionOptionEvaluateReturnsCorrectValue(self):
        conditionOption = ConditionOption(["ally"], "help", "")

        self.assertEqual("help", conditionOption.evaluate("ally"))

    def test03ConditionOptionEvaluateReturnsCorrectConditionWithVariousKeys(self):
        conditionOption = ConditionOption(["ally", "help"], "help", "")

        self.assertEqual("help", conditionOption.evaluate("help"))

    def test04ConditionOptionEvaluateDisregardsCapitalization(self):
        conditionOption = ConditionOption( ["enemy"], "harm", "")

        self.assertEqual("harm", conditionOption.evaluate("Enemy"))

    def test05ConditionOptionEvaluateReturnsEmptyStringIfTheParameterIsNotRecognized(self):
        conditionOption = ConditionOption(["enemy"], "harm", "")

        self.assertEqual("", conditionOption.evaluate("cocoa"))


if __name__ == '__main__':
    unittest.main()
