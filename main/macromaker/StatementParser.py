from macromaker.NoSpellException import NoSpellException
from macromaker.Statement import Statement
from macromaker.StatementConditionsParser import StatementConditionsParser


class StatementParser:
    STATEMENTSPLITFLAG = ";"
    SPELLQUOTATIONMARK = '"'

    def __init__(self):
        self.statementConditionsParser = StatementConditionsParser()

    def parseStatements(self, inputString):
        statementStrings = inputString.split(self.STATEMENTSPLITFLAG)

        statements = []
        for statementString in statementStrings:
            statement = Statement()

            spell = self.searchSpell(statementString)
            statementString = statementString.replace(self.SPELLQUOTATIONMARK+spell+self.SPELLQUOTATIONMARK, "")
            statement.addSpell(spell)

            statementConditions = self.statementConditionsParser.parseConditions(statementString)
            statement.addConditions(statementConditions)

            statements.append(statement)

        return statements



    def searchSpell(self, text):
        spellFound = False
        spellName = ""
        for character in text:
            if character == self.SPELLQUOTATIONMARK:

                if not spellFound:
                    spellFound = True
                else:

                    return spellName

            elif spellFound:
                spellName = spellName + character

        raise NoSpellException
