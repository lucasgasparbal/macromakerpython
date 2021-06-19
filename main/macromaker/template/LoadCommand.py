from macromaker.NoSpellException import NoSpellException
from macromaker.template.TemplateNotFoundException import TemplateNotFoundException
from macromaker.template.NoTemplateTitleException import NoTemplateTitleException
from macromaker.template.NotEnoughSpellsException import NotEnoughSpellsException


class LoadCommand:
    def __init__(self, templateHandler):
        self.templateHandler = templateHandler

    def execute(self, inputString):
        try:
            macro = self.templateHandler.loadTemplate(inputString)
            print("\nYour macro:\n\n")
            print(macro + "\n\n")
        except NoSpellException:
            print('\nERROR.\n''No spell was detected in the input. '
                  'Type the spell(s) inside "" quotation marks . ')
        except NotEnoughSpellsException:
            print("\nERROR.\n"
                  "Not enough spells were found for this macro template. Make sure there is one spell for every "
                  "statement in the macro. "
                  'Remember to write every spell in between quotation marks (Ex. "Fireball" "Frostbolt")')
        except NoTemplateTitleException:
            print('\nERROR.\n'
                  'No title could be detected in the input. '
                  'Make sure you separate the title from the spells with ":"')
        except (FileNotFoundError, TemplateNotFoundException) as e:
            print("\nERROR.\n'"
                  "No template with the given title was found, "
                  "make sure the template is inside the templates.txt file or save a new template with the given title")

    def getParameters(self):
        return self.templateHandler.getFunctionParameters("load")