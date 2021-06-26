from enum import Enum

from macromaker.template.CommandNotFoundException import CommandNotFoundException


class InstructionsHelper:
    MACROFLAGS = ["macro", "macromaker", "macrosyntax"]

    def __init__(self, macromaker, commandsInterface):
        self.macromaker = macromaker
        self.commandsInterface = commandsInterface

    def processHelp(self, parameters):

        parameter = parameters.lower().strip()

        try:
            self.printAdditionalCommandInstructions(parameter)
        except CommandNotFoundException:
            if self.isMacroFlag(parameter):
                self.printMacroHelp()
            else:
                self.printCommandsAndParameters()

    def printCommandsAndParameters(self):
        print("\navailable commands: \n")

        commandsAndParameters = self.commandsInterface.getCommandsAndParameters()

        for command in commandsAndParameters.keys():
            print("\n\n - " + command + " " + commandsAndParameters[command])

        print("\n\nFor more information on each command, type 'help' followed by the command.")
        print("\nIf you wish to know more about making macros, type 'help macro'. ")
        print("\nFor a list of available macro conditions, type 'help conditions'. ")

    def printAdditionalCommandInstructions(self, commandName):
        commandParameters = self.commandsInterface.getParameters(commandName)
        printString = "\n\n" + commandName + " " + commandParameters + "\n\n\n"
        altCalls = self.commandsInterface.getCommandAlternativeCalls(commandName)
        if altCalls:
            printString = printString + "Alternative calls:  " + altCalls.pop(0)
            for call in altCalls:
                printString = printString + ", " + call
            printString = printString + "\n\n"

        printString = printString + "Description: " + self.commandsInterface.getCommandDescription(commandName) + "\n\n"

        print(printString)

    def printMacroHelp(self):
        printString = "\n\n-SEPARATORS(use without parenthesis)-\n\n"
        separators = self.macromaker.getSeparators()
        for key in separators:
            printString = printString + key + "(" + separators[key] + ")" + "\n\n"

        printString = printString + "\nUseful information + Rules:\n"

        rules = self.macromaker.getRules()
        for rule in rules:
            printString = printString + "\n\n - " + rule

        printString = printString + '\n\n\n [ Macro example: player alt / mouseover ally "Chain Heal"; mouseover ' \
                                    'enemy "Chain Lightning"]\n' \
                                    '\n\tThis example returns a macro that casts Chain Heal on the player if the alt ' \
                                    'key is held; ' \
                                    'or it casts it on an ally, if the cursor is over them or they are the ' \
                                    'target.\n\tIf the target or the unit on cursor is an enemy it instead casts ' \
                                    'Chain Lightning.\n\n\n '

        print(printString)
        print("For a list of available macro conditions, type 'help conditions'.")
        print("\nFor a list of commands, type 'help'. ")

    def printGeneralMacroHelp(self):
        pass

    def isMacroFlag(self, parameter):
        for flag in self.MACROFLAGS:
            if parameter == flag:
                return True
        return False
