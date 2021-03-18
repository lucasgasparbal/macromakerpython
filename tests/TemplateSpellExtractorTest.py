import unittest

from macromaker.NoSpellException import NoSpellException
from macromaker.template.TemplateSpellExtractor import TemplateSpellExtractor

class TemplateSpellExtractorTest(unittest.TestCase):

    def test01TemplateSpellExtractorReturnsTheSameInputText(self):
        templateSpellExtractor = TemplateSpellExtractor("spellplaceholder")
        extractedText = templateSpellExtractor.extractSpell("hello this is text")
        self.assertEqual("hello this is text", extractedText[1])

    def test02TemplateSpellExtractorReturnsSpellPlaceholderEvenWithEmptyImputText(self):
        templateSpellExtractor = TemplateSpellExtractor("spellplaceholder")
        extractedText = templateSpellExtractor.extractSpell("")
        self.assertEqual("spellplaceholder", extractedText[0])

    def test03TemplateSpellExtractorReturnsSpellPlaceholderEvenWithText(self):
        templateSpellExtractor = TemplateSpellExtractor("spellplaceholder")
        extractedText = templateSpellExtractor.extractSpell("hello this is text")
        self.assertEqual("spellplaceholder", extractedText[0])

    def test04TemplateSpellExtractorReturnsSpellPlaceholderEvenIfASpellIsPresentWithinTheText(self):
        templateSpellExtractor = TemplateSpellExtractor("spellplaceholder")
        extractedText = templateSpellExtractor.extractSpell('this is the "Chain Heal" spell')
        self.assertEqual("spellplaceholder", extractedText[0])

    def test05TemplateSpellExtractorExtractSpellsRaisesExceptionIfNoSpellIsDetected(self):
        templateSpellExtractor = TemplateSpellExtractor("spellplaceholder")
        self.assertRaises(NoSpellException,templateSpellExtractor.extractSpells,"")

    def test06TemplateSpellExtractorExtractSpellsExtractsOneSpell(self):
        templateSpellExtractor = TemplateSpellExtractor("spellplaceholder")
        self.assertEqual(["Chain Heal"], templateSpellExtractor.extractSpells('"Chain Heal"'))

    def test07TemplateSpellExtractorExtractSpellsExtractsOneSpellAndIgnoresNonSpells(self):
        templateSpellExtractor = TemplateSpellExtractor("spellplaceholder")
        self.assertEqual(["Chain Heal"], templateSpellExtractor.extractSpells('this is a "Chain Heal" test'))

    def test08TemplateSpellExtractorExtractSpellsExtractsEverySpell(self):
        templateSpellExtractor = TemplateSpellExtractor("spellplaceholder")
        self.assertEqual(["Chain Heal","Riptide","Chain Harvest", "Healing Surge"],
                         templateSpellExtractor.extractSpells('"Chain Heal" "Riptide" "Chain Harvest" "Healing Surge"'))

    def test09TemplateSpellExtractorExtractSpellsExtractsEverySpellAndIgnoresNonSpells(self):
        templateSpellExtractor = TemplateSpellExtractor("spellplaceholder")
        self.assertEqual(["Chain Heal","Riptide","Chain Harvest", "Healing Surge"],
                         templateSpellExtractor.extractSpells('banana "Chain Heal" apple "Riptide" pineapple peach '
                                                              'grape "Chain Harvest" "Healing Surge"'))



if __name__ == '__main__':
    unittest.main()
