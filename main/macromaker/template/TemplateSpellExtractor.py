from macromaker.SpellExtractor import SpellExtractor


class TemplateSpellExtractor(SpellExtractor):

    def __init__(self, placeholderText):
        self.spellPlaceholderText = placeholderText

    def extractSpell(self, statementText):
        return [self.spellPlaceholderText, statementText]
