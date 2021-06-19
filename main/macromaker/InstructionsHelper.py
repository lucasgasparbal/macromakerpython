class InstructionsHelper:
    def __init__(self,macromaker,commandsInterface):
        self.macromaker = macromaker
        self.commandsInterface = commandsInterface

    def processHelp(self, parameters):
        if not parameters:
            self.printCommandsAndParameters()
        else:
            pass

    def printCommandsAndParameters(self):
        print("\navailable commands: \n")

        commandsAndParameters = self.commandsInterface.getCommandsAndParameters()

        for command in commandsAndParameters.keys():
            print("\n\n - "+command+" "+commandsAndParameters[command])

        print("\n\n\nfor more information on each command, type help followed by the command.\n\n")