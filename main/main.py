from macromaker.MacroMaker import MacroMaker
from macromaker.NoSpellException import NoSpellException


def main():
    print("----Macromaker program alpha version----\n\n\n\n")

    macromaker = MacroMaker()
    programRunning = True
    while(programRunning):

        textInput = input("\n\nPlease write the macro statements\n")
        if textInput == "exit":
            programRunning = False
        else:
            print("\nYour macro:\n\n\n")

            try: textToShow = macromaker.makeMacro(textInput)
            except NoSpellException:
                textToShow = 'There was one or more statements without a spell. Ensure every statement has one spell ' \
                             'between "" quotation marks. '

            print(textToShow)
    print("\nclosing Macromaker")
    return

if __name__ == "__main__":
    main()