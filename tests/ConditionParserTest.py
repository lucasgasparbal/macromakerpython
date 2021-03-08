import unittest
from macromaker.conditionparsing.ConditionParser import ConditionsParser


class ConditionParserTest(unittest.TestCase):
    def test01ParserWithoutInputReturnsEmptyList(self):
        parser = ConditionsParser()
        self.assertEqual([], parser.parse(""))

    def test02ParserReturnsDesiredList(self):
        parser = ConditionsParser()

        self.assertEqual(["harm", "dead"], parser.parse(["enemy", "dead"]))

    def test03ParserDoesNotRepeatConditionsIfKeywordIsRepeated(self):
        parser = ConditionsParser()
        parsedConditions = parser.parse(["enemy", "enemy", "enemy", "dead"])

        self.assertEqual(["harm", "dead"], parsedConditions)

    def test04ParserDoesNotChangeConditionIfConflictingKeywordIsInTheInputString(self):
        parser = ConditionsParser()
        parsedConditions = parser.parse(["ally", "enemy", "alive", "dead"])

        self.assertEqual(["help", "nodead"], parsedConditions)

    def test05ParserClearedRetur(self):
        parser = ConditionsParser()
        parsedConditions = parser.parse(["ally", "enemy", "alive", "dead"])

        self.assertEqual(["help", "nodead"], parsedConditions)


if __name__ == '__main__':
    unittest.main()
