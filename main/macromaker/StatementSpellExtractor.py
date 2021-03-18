from macromaker.NoSpellException import NoSpellException
from macromaker.SpellExtractor import SpellExtractor


class StatementSpellExtractor(SpellExtractor):

    def extractSpell(self, statementText):
        spellName = self.extractSpells(statementText)[0]
        statementText = statementText.replace(self.SPELLQUOTATIONMARK + spellName + self.SPELLQUOTATIONMARK,
                                              "")
        statementText = statementText.replace("  ", " ")
        return [spellName, statementText]



