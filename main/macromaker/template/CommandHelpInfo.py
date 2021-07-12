class CommandHelpInfo:
    altCalls = []
    parameters = ""

    def __init__(self, commandName, description):
        self.commandName = commandName
        self.description = description

    def addCall(self, call):
        self.altCalls.append(call)

    def addParameters(self, parameters):
        self.parameters = parameters

    def getTitle(self):
        return

    def getAltCalls(self):
        if self.altCalls:
            altCalls = self.altCalls.copy()
            printString = altCalls.pop(0)
            for call in altCalls:
                printString = printString + ", " + call
            return printString
        return ""

    def getDescription(self):
        return self.description

    def getHelpInfo(self):
        string = self.commandName + " " + self.parameters + \
                 "\n\n" + \
                 "Alternative calls: " + self.getAltCalls() + \
                 "\n\n\n" + "Description: " + self.description + "\n\n"
        return string
