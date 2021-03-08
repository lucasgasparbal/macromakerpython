from macromaker.NoSpellException import NoSpellException


class Statement:
    def __init__(self):
        self.conditions = []
        self.spell = ""

    def addConditions(self, statementConditions):
        self.conditions = statementConditions

    def addSpell(self, spell):
        self.spell = spell

    def write(self):
        result = ""
        if not self.spell:
            raise NoSpellException("An Statement needs a spell")
        for condition in self.conditions:
            result = result + condition.write()

        if result:
            result = result + " "

        result = result + self.spell

        return result
