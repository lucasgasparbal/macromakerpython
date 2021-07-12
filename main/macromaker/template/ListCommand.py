from macromaker.template.TemplateCommand import TemplateCommand


class ListCommand(TemplateCommand):

    DESCRIPTION = "Lists the titles of the currently saved templates."

    def execute(self, inputString):
        try:
            titlesList = self.templateHandler.getTemplateTitles()
            if titlesList:
                print("\n")
                for title in titlesList:
                    print("\n - "+title)
        except FileNotFoundError:
            print("\n\nThere are currently no saved templates.")

    def getParameters(self):
        return self.templateHandler.getFunctionParameters("list")

    def getDescription(self):
        return self.DESCRIPTION
