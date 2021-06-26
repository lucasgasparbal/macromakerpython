from macromaker.NoSpellException import NoSpellException
from macromaker.Statement import Statement
from macromaker.StatementConditionsParser import StatementConditionsParser


class StatementParser:
    STATEMENTSPLITFLAG = ";"

    def __init__(self):
        self.statementConditionsParser = StatementConditionsParser()

    def parseStatements(self, inputString, spellExtractor):
        statementStrings = inputString.split(self.STATEMENTSPLITFLAG)

        statements = []
        for statementString in statementStrings:
            extractedStrings = spellExtractor.extractSpell(statementString)
            spell = extractedStrings[0]
            statementString = extractedStrings[1]

            statement = Statement()
            statement.addSpell(spell)

            statementConditions = self.statementConditionsParser.parseConditions(statementString)
            statement.addConditions(statementConditions)
            statements.append(statement)

        return statements

    def getSeparators(self):
        separators = {"Statement separator : ": self.STATEMENTSPLITFLAG}
        separators.update(self.statementConditionsParser.getSeparators())
        return separators

    def getRules(self):
        return self.statementConditionsParser.getRules()