from macromaker.template.TemplateNotFoundException import TemplateNotFoundException


class ShowCommand:

    DESCRIPTION = "Shows the given title's macro template on the console, without spells."

    def __init__(self, templateHandler):
        self.templateHandler = templateHandler

    def execute(self, inputString):
        try:
            templateToShow = self.templateHandler.showTemplate(inputString)
            print("\n")
            print(templateToShow)
        except (FileNotFoundError, TemplateNotFoundException) as e:
            print("\nNo template with the given title was found, "
                  "make sure the desired template is inside the templates.txt file or save a new template with the "
                  "given title")

    def getParameters(self):
        return self.templateHandler.getFunctionParameters("show")

    def getDescription(self):
        return self.DESCRIPTION
