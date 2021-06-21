from macromaker.template.TemplateNotFoundException import TemplateNotFoundException


class RemoveCommand:

    DESCRIPTION = "Removes the given template from the files"

    def __init__(self,templateHandler):
        self.templateHandler = templateHandler

    def execute(self,inputText):
       try:
           self.templateHandler.removeTemplate(inputText)
           print("\nremoved template succesfully\n")
       except (FileNotFoundError, TemplateNotFoundException):
           print("\nERROR.\n"
                 "There was no template found with the given title")

    def getParameters(self):
        return self.templateHandler.getFunctionParameters("remove")

    def getDescription(self):
        return self.DESCRIPTION