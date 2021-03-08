import unittest
from macromaker.conditionparsing.ModConditionParser import ModConditionParser


class MyTestCase(unittest.TestCase):
    def test01ModConditionParserParsesEmptyListReturnAnEmptyModCondition(self):
        modConditionParser = ModConditionParser()
        modCondition = modConditionParser.parse([""])
        self.assertEqual("", modCondition.write())

    def test02ModConditionParserParsesListWithNonKeywordStringsReturnAnEmptyModCondition(self):
        modConditionParser = ModConditionParser()
        modCondition = modConditionParser.parse(["banana","pineapple","orange","strawberry"])
        self.assertEqual("", modCondition.write())

    def test03ModConditionParserParsesListWithKeyWordsReturnCorrectModCondition(self):
        modConditionParser = ModConditionParser()
        modCondition = modConditionParser.parse(["alt","ctrl","shift"])
        self.assertEqual("mod:alt+ctrl+shift", modCondition.write())

    def test04ModConditionParserParsesListWithKeywordsAndNonKeywordsReturnCorrectModCondition(self):
        modConditionParser = ModConditionParser()
        modCondition = modConditionParser.parse(["ctrl", "alt","banana", "pineapple", "shift"])
        self.assertEqual("mod:ctrl+alt+shift", modCondition.write())

    def test05ModConditionParserParsesListWithRepeatedKeywordsDoesNotRepeatThemInTheResultString(self):
        modConditionParser = ModConditionParser()
        modCondition = modConditionParser.parse(["alt", "alt", "ctrl", "control"])
        self.assertEqual("mod:alt+ctrl", modCondition.write())



if __name__ == '__main__':
    unittest.main()
