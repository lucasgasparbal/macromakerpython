import unittest

from macromaker.NoSpellException import NoSpellException

from macromaker.StatementSpellExtractor import StatementSpellExtractor


class StatementSpellExtractorTest(unittest.TestCase):

    def test01StatementSpellExtractorIfNoSpellIsDetectedRaisesException(self):
        statementSpellExtractor = StatementSpellExtractor()
        self.assertRaises(NoSpellException, statementSpellExtractor.extractSpell, "")

    def test02StatementSpellExtractorRecognizesSpell(self):
        statementSpellExtractor = StatementSpellExtractor()
        extractedStrings = statementSpellExtractor.extractSpell(' "Chain Heal" ')
        self.assertEqual("Chain Heal", extractedStrings[0])

    def test03StatementSpellExtractorRecognizesSpellInALongString(self):
        statementSpellExtractor = StatementSpellExtractor()
        extractedStrings = statementSpellExtractor.extractSpell(' player alt alive "Chain Heal" enemy ')
        self.assertEqual("Chain Heal", extractedStrings[0])

    def test04StatementSpellExtractorExtractsSpellFromString(self):
        statementSpellExtractor = StatementSpellExtractor()
        string = ' player alt alive "Chain Heal" enemy '
        extractedStrings = statementSpellExtractor.extractSpell(string)
        self.assertEqual(' player alt alive enemy ', extractedStrings[1])

    def test05StatementSpellExtractorExtractsSpellAndRespectsSpellCapitalization(self):
        statementSpellExtractor = StatementSpellExtractor()
        string = ' player alt alive "ChAiN HeAL" enemy '
        extractedStrings = statementSpellExtractor.extractSpell(string)
        self.assertEqual('ChAiN HeAL', extractedStrings[0])

    def test06StatementSpellExtractorWhenMoreThanOneSpellIsPresentSelectsTheFirstOne(self):
        statementSpellExtractor = StatementSpellExtractor()
        extractedStrings = statementSpellExtractor.extractSpell(' player alt alive "Riptide" enemy "Chain Heal" ')
        self.assertEqual("Riptide", extractedStrings[0])


if __name__ == '__main__':
    unittest.main()
