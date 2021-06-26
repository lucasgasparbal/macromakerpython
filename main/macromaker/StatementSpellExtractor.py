from macromaker.NoSpellException import NoSpellException
from macromaker.SpellExtractor import SpellExtractor


class StatementSpellExtractor(SpellExtractor):

    def extractSpell(self, statementText):
        spellName = self.extractSpells(statementText)[0]
        statementText = statementText.replace(self.SPELLQUOTATIONMARK + spellName + self.SPELLQUOTATIONMARK,
                                              "")
        statementText = statementText.replace("  ", " ")
        return [spellName, statementText]



    def getRules(self):
        return 'All Statements must have a spell, enclosed by double quotation marks(" ")\n' \
               '\tExample: "Chain Heal" '