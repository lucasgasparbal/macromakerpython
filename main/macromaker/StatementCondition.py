from macromaker.conditionparsing.ModCondition import ModCondition


class StatementCondition:

    def __init__(self):
        self.target = ""
        self.conditions = []
        self.modifiers = ModCondition()

    def setTarget(self, target):
        if not self.target:
            self.target = target

    def setConditions(self, conditions):
        for condition in conditions:
            if not (condition in self.conditions):
                self.conditions.append(condition)

    def setModifierConditions(self, modifiers):
        self.modifiers = modifiers

    def write(self):
        result = "["
        if self.target:
            result = result + "@" + self.target
        for i, condition in enumerate(self.conditions):
            if i > 0 or self.target:
                result = result + ", "
            result = result + condition

        modifiers = self.modifiers.write()
        if modifiers:
            result = result + ", " + modifiers
        result = result + "]"

        return result
