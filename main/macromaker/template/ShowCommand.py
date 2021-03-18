from macromaker.template.TemplateNotFoundException import TemplateNotFoundException


class ShowCommand:
    def __init__(self, templateHandler):
        self.templateHandler = templateHandler

    def execute(self, inputString):
        try:
            templateToShow = self.templateHandler.showTemplate(inputString)
            print("Template\n")
            print(templateToShow)
        except (FileNotFoundError, TemplateNotFoundException) as e:
            print("\nNo template with the given title was found, "
                  "make sure the desired template is inside the templates.txt file or save a new template with the given title")