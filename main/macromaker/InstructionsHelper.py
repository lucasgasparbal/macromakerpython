from macromaker.template.CommandNotFoundException import CommandNotFoundException


class InstructionsHelper:
    def __init__(self,macromaker,commandsInterface):
        self.macromaker = macromaker
        self.commandsInterface = commandsInterface

    def processHelp(self, parameters):
        if parameters:
            commandName = parameters.lower().strip()
        else:
            commandName = ""

        try:
            self.printAdditionalCommandInstructions(commandName)
        except CommandNotFoundException:
            self.printCommandsAndParameters()

    def printCommandsAndParameters(self):
        print("\navailable commands: \n")

        commandsAndParameters = self.commandsInterface.getCommandsAndParameters()

        for command in commandsAndParameters.keys():
            print("\n\n - "+command+" "+commandsAndParameters[command])

        print("\n\n\nfor more information on each command, type help followed by the command.\n\n")

    def printAdditionalCommandInstructions(self, commandName):
        commandParameters = self.commandsInterface.getParameters(commandName)
        printString = "\n\n"+commandName+" "+commandParameters+"\n\n\n"
        altCalls = self.commandsInterface.getCommandAlternativeCalls(commandName)
        if altCalls:
            printString = printString + "Alternative calls:  "+ altCalls.pop(0)
            for call in altCalls:
                printString = printString +", " + call
            printString = printString + "\n\n"

        printString = printString + "Description: " + self.commandsInterface.getCommandDescription(commandName) +"\n\n"

        print(printString)
