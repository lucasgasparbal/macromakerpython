import unittest
from macromaker.conditionparsing.TargetParser import TargetParser


class TargetParserTest(unittest.TestCase):

    def test01TargetParserReturnsEmptyStringIfParsingEmptyList(self):
        targetParser = TargetParser()

        self.assertEqual("", targetParser.parse([]))

    def test02TargetParserReturnsEmptyStringIfParsingListWithNonKeywords(self):
        targetParser = TargetParser()

        self.assertEqual("", targetParser.parse(["banana","pineapple","strawberry","avocado"]))

    def test03TargetParserReturnsCorrectStringWhenParsingAKeyword(self):
        targetParser = TargetParser()

        self.assertEqual("player", targetParser.parse(["player"]))

    def test04TargetParserReturnsCorrectStringWhenParsingMouseover(self):
        targetParser = TargetParser()

        self.assertEqual("mouseover, exists", targetParser.parse(["mouseover"]))

    def test05TargetParserReturnsCorrectStringWhenParsingFocus(self):
        targetParser = TargetParser()

        self.assertEqual("focus, exists", targetParser.parse(["focus"]))

    def test06TargetParserDoesNotRepeatTargetIfKeywordIsRepeated(self):
        targetParser = TargetParser()

        self.assertEqual("player", targetParser.parse(["player","player"]))

    def test07TargetParserWithMoreThanOneTargetKeywordChoosesTheFirstOne(self):
        targetParser = TargetParser()

        self.assertEqual("target", targetParser.parse(["target","player","focus","mouseover"]))



if __name__ == '__main__':
    unittest.main()
