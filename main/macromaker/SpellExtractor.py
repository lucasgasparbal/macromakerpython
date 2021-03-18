from macromaker.NoSpellException import NoSpellException


class SpellExtractor:
    SPELLQUOTATIONMARK = '"'

    def extractSpells(self, text):
        spells = []
        spellFound = False
        spell = ""
        for character in text:
            if character == self.SPELLQUOTATIONMARK:
                if not spellFound:
                    spellFound = True
                else:
                    spells.append(spell)
                    spell = ""
                    spellFound = False

            elif spellFound:
                spell = spell + character

        if len(spells) == 0:
            raise NoSpellException

        return spells