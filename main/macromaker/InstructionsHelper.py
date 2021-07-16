from macromaker.template.CommandNotFoundException import CommandNotFoundException


class InstructionsHelper:
    MACROFLAGS = ["macro", "macromaker", "macrosyntax"]
    CONDITIONFLAGS = ["conditions","condition","cond"]

    def __init__(self, macromaker, commandsInterface):
        self.macromaker = macromaker
        self.commandsInterface = commandsInterface

    def processHelp(self, parameters):

        parameter = parameters.lower().strip()

        try:
            self.printAdditionalCommandInstructions(parameter)
        except CommandNotFoundException:
            if self.isFlag(self.MACROFLAGS,parameter):
                self.printMacroHelp()
            elif self.isFlag(self.CONDITIONFLAGS,parameter):
                self.printConditionsHelp()
            else:
                self.printCommandsAndParameters()

    def printCommandsAndParameters(self):
        print("\navailable commands: \n")

        commandsAndParameters = self.commandsInterface.getCommandsAndParameters()

        for command in commandsAndParameters.keys():
            print("\n\n - " + command + " " + commandsAndParameters[command])

        print("\n\nFor more information on each command, type 'help' followed by the command.")
        print("If you wish to know more about making macros, type 'help macro'. ")
        print("For a list of available macro conditions, type 'help conditions'. ")

    def printAdditionalCommandInstructions(self, commandName):
        commandHelpInfo = self.commandsInterface.getCommandHelpInfo(commandName)

        print("\n\n" + commandHelpInfo.getHelpInfo())

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
        print("For a list of commands, type 'help'. ")

    def printConditionsHelp(self):
        categoriesAndConditions = self.macromaker.getCategoriesAndConditons()
        print("CONDITIONS LIST \n")
        for category in categoriesAndConditions.keys():
            print("\n------\n"+category.upper())
            for conditionInfo in categoriesAndConditions[category]:
                print("\n"+conditionInfo)
            print("\n")
        print("If you wish to know more about making macros, type 'help macro'. ")
        print("For a list of commands, type 'help'. ")

    def isFlag(self, flags, parameter):
        for flag in flags:
            if parameter == flag:
                return True
        return False

