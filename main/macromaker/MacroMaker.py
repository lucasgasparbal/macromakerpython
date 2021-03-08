from macromaker.StatementParser import StatementParser


class MacroMaker:

    TOOLTIPSTRING = "#showtooltip\n"
    CASTSTRING = "/cast "

    def __init__(self):
        self.statementParser = StatementParser()

    def makeMacro(self, inputText):

        statements = self.statementParser.parseStatements(inputText)

        macro = self.TOOLTIPSTRING + self.CASTSTRING

        for i, statement in enumerate(statements):

            if i > 0:
                macro = macro + "; "

            macro = macro + statement.write()

        return macro
