from macromaker.MacroMaker import MacroMaker
from macromaker.NoSpellException import NoSpellException
from macromaker.template.LoadCommand import LoadCommand
from macromaker.template.SaveCommand import SaveCommand
from macromaker.template.TemplateHandler import TemplateHandler
from macromaker.template.ShowCommand import ShowCommand


def main():
    print("----Macromaker program alpha version----\n\n\n\n")
    templateHandler = TemplateHandler()
    saveCommand = SaveCommand(templateHandler)
    loadCommand = LoadCommand(templateHandler)
    showCommand = ShowCommand(templateHandler)
    commands = {
        "save": saveCommand,
        "savetemplate": saveCommand,
        "load": loadCommand,
        "loadtemplate": loadCommand,
        "show": showCommand,
        "showtemplate": showCommand
    }

    macromaker = MacroMaker()
    programRunning = True
    while programRunning:

        textInput = input("\n\nPlease write a command or macro statements\n")
        splitInput = textInput.split(maxsplit=1)
        commandString = splitInput[0].strip()
        commandString = commandString.lower()
        command = commands.get(commandString)
        if command:
            command.execute(splitInput[1])
        elif textInput.lower().strip() == "exit":
            programRunning = False
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