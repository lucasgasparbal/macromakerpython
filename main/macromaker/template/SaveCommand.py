from macromaker.template.NoTemplateTitleException import NoTemplateTitleException


class SaveCommand:

    def __init__(self, templateHandler):
        self.templateHandler = templateHandler

    def execute(self, inputString):
        try:
            self.templateHandler.saveTemplate(inputString)
            print("saved succesfully")
        except NoTemplateTitleException:
            print('\nNo title could be detected in the input. Make sure you separate the title from the content of the ' \
                  'template with ":" ')

    def getParameters(self):
        return self.templateHandler.getFunctionParameters("save")
