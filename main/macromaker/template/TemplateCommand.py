class TemplateCommand:
    DESCRIPTION = ""

    def __init__(self, templateHandler):
        self.templateHandler = templateHandler

    def getDescription(self):
        return self.DESCRIPTION
