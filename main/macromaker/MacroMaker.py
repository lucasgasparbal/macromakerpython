from macromaker.StatementParser import StatementParser
from macromaker.StatementSpellExtractor import StatementSpellExtractor
from macromaker.template.TemplateSpellExtractor import TemplateSpellExtractor


class MacroMaker:
    TOOLTIPSTRING = "#showtooltip\n"
    CASTSTRING = "/cast "

    def __init__(self):
        self.statementParser = StatementParser()
        self.statementSpellExtractor = StatementSpellExtractor()

    def makeMacro(self, inputText):

        return self.writeMacro(inputText, self.statementSpellExtractor)

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

    def getSeparators(self):
        return self.statementParser.getSeparators()

    def getRules(self):
        rules = []
        macroRules = "A cast macro is composed of 1 or more statements. statements are composed by one spell and " + \
                     "one or more condition blocks.A condition block is a group of conditions that have to be met " \
                     "to " \
                     "execute an statement "

        rules.append(macroRules)
        rules.append(self.statementSpellExtractor.getRules())
        rules.extend(self.statementParser.getRules())
        return rules

    def getCategoriesAndConditons(self):
        return self.statementParser.getCategoriesAndConditions()
