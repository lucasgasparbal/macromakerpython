from macromaker.MacroMaker import MacroMaker
from macromaker.InstructionsHelper import InstructionsHelper
from macromaker.NoSpellException import NoSpellException
from macromaker.template.CommandsInterface import CommandsInterface
from macromaker.template.CommandNotFoundException import CommandNotFoundException


def main():
    print("----Macromaker program alpha version----\n\n\n\n")
    macromaker = MacroMaker()
    commandInterface = CommandsInterface(macromaker)
    helper = InstructionsHelper(macromaker, commandInterface)

    programRunning = True
    while programRunning:

        textInput = input("\n\nPlease write a command or macro statements\n")
        splitInput = textInput.split(maxsplit=1)
        commandString = splitInput[0].strip()
        commandString = commandString.lower()
        try:
            if len(splitInput) > 1:
                commandInterface.executeCommand(commandString, splitInput[1])
            else:
                commandInterface.executeCommand(commandString,"")

        except CommandNotFoundException:
            if commandString == "exit":
                programRunning = False
            elif commandString == "help":
                if len(splitInput) > 1:
                    helper.processHelp()
                else:
                    helper.processHelp("")
            else:
                try:
                    textToShow = macromaker.makeMacro(textInput)
                    print("\nYour macro:\n\n\n")
                except NoSpellException:
                    textToShow = '\nERROR.\n' \
                                 'There was one or more statements without a spell. Ensure every statement has one spell ' \
                                 'marked by "" quotation marks. '
                print(textToShow)

    print("\nclosing Macromaker")
    return


if __name__ == "__main__":
    main()
