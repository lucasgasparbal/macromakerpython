from macromaker.template.TemplateCommand import TemplateCommand
from macromaker.template.TemplateNotFoundException import TemplateNotFoundException
from macromaker.template.TitleOccupiedException import TitleOccupiedException


class ChangeTitleCommand(TemplateCommand):

    DESCRIPTION = "Changes the title of the first title's template with the second given title. If the second title\n " \
                  "is already in use, it won't change the title."

    def execute(self, inputText):
        try:
            self.templateHandler.changeTemplateTitle(inputText)
        except TitleOccupiedException:
            print("\nERROR\n"
                  "A template is already associated with the desired name, either remove it from the file or change "
                  "it's title.")
        except TemplateNotFoundException:
            print("\nERROR\n"
                  "The template you want to change the title of was not found.")

        print("Title changed succesfully.\n")

    def getParameters(self):
        return self.templateHandler.getFunctionParameters("change")