from macromaker.template.TemplateNotFoundException import TemplateNotFoundException
from macromaker.template.NoTemplateTitleException import NoTemplateTitleException


class TemplatesFileHandler:
    TEMPLATESFILEPATH = "templates.txt"
    ENDOFTEMPLATEMARKER = "(END)"

    def saveTemplate(self, title, macroTemplate):

        templateHasToBeReplaced = False
        fileLines = []

        try:
            file = open(self.TEMPLATESFILEPATH, mode='r', encoding='utf-8')
            deletingTemplate = False
            for line in file:
                if line.strip("\n") == title:
                    templateHasToBeReplaced = True
                    deletingTemplate = True
                if not deletingTemplate:
                    fileLines.append(line)
                else:
                    if line.strip("\n") == self.ENDOFTEMPLATEMARKER:
                        deletingTemplate = False
            file.close()
        except FileNotFoundError:
            pass

        if templateHasToBeReplaced:
            file = open(self.TEMPLATESFILEPATH, mode='w', encoding='utf-8')

            for line in fileLines:
                file.write(line)
        else:
            file = open(self.TEMPLATESFILEPATH, mode='a', encoding='utf-8')

        file.write("\n" + title + "\n")
        file.write(macroTemplate + "\n")
        file.write(self.ENDOFTEMPLATEMARKER + "\n")
        file.close()

    def loadTemplate(self, title):
        file = open(self.TEMPLATESFILEPATH, mode='r', encoding='utf-8')

        templateFound = False
        macro= ""
        for line in file:
            if not templateFound:
                if line.strip("\n") == title:
                    templateFound = True
            else:
                if line.strip("\n") == self.ENDOFTEMPLATEMARKER:
                    break
                else:
                    macro = macro + line
        file.close()

        if not templateFound:
            raise TemplateNotFoundException
        return macro


