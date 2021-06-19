from macromaker.StatementParser import StatementParser
from macromaker.StatementSpellExtractor import StatementSpellExtractor
from macromaker.template.TemplateSpellExtractor import TemplateSpellExtractor


class MacroMaker:
    TOOLTIPSTRING = "#showtooltip\n"
    CASTSTRING = "/cast "

    def __init__(self):
        self.statementParser = StatementParser()

    def makeMacro(self, inputText):

        return self.writeMacro(inputText, StatementSpellExtractor())

    def makeMacroTemplate(self, inputText, spellPlaceholder):

        return self.writeMacro(inputText, TemplateSpellExtractor(spellPlaceholder))

    def writeMacro(self, inputText, spellExtractor):

        statements = self.statementParser.parseStatements(inputText, spellExtractor)
        macro = self.TOOLTIPSTRING + self.CASTSTRING

        for i, statement in enumerate(statements):

            if i > 0:
                macro = macro + "; "

            macro = macro + statement.write()

        return macro
