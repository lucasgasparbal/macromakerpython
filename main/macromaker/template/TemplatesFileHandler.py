from macromaker.template.TemplateNotFoundException import TemplateNotFoundException
from macromaker.template.NoTemplateTitleException import NoTemplateTitleException
from macromaker.template.TitleOccupiedException import TitleOccupiedException


class TemplatesFileHandler:
    TEMPLATESFILEPATH = "templates.txt"
    ENDOFTEMPLATEMARKER = "(END)"

    def saveTemplate(self, title, macroTemplate):

        templateHasToBeReplaced = False
        newFileLines = []
        try:
            file = open(self.TEMPLATESFILEPATH, mode='r', encoding='utf-8')
            fileLines = file.readlines()
            file.close()
            newFileLines = self.excludeTemplateFromFileLines(title, fileLines)
            if newFileLines < fileLines:
                templateHasToBeReplaced = True
        except FileNotFoundError:
            pass

        if templateHasToBeReplaced:
            file = open(self.TEMPLATESFILEPATH, mode='w', encoding='utf-8')
            newFileLines = self.collapseNewLines(newFileLines)
            for line in newFileLines:
                file.write(line)
        else:
            file = open(self.TEMPLATESFILEPATH, mode='a', encoding='utf-8')

        file.write("\n" + title + "\n")
        file.write(macroTemplate + "\n")
        file.write(self.ENDOFTEMPLATEMARKER + "\n")
        file.close()

    def loadTemplate(self, title):
        file = open(self.TEMPLATESFILEPATH, mode='r', encoding='utf-8')
        macro = self.extractMacro(title, file.readlines())
        file.close()

        return macro

    def removeTemplate(self, title):
        file = open(self.TEMPLATESFILEPATH, mode='r', encoding='utf-8')
        fileLines = file.readlines()
        file.close()
        newFileLines = self.excludeTemplateFromFileLines(title, fileLines)
        if newFileLines >= fileLines:
            raise TemplateNotFoundException
        newFileLines = self.collapseNewLines(newFileLines)
        self.writeLinesIntoFile(newFileLines)

    def changeTitleOfTemplate(self, oldTitle, newTitle):
        file = open(self.TEMPLATESFILEPATH, mode='r', encoding='utf-8')
        fileLines = file.readlines()
        file.close()

        for line in fileLines:
            if line.strip("\n") == newTitle:
                raise TitleOccupiedException

        macro = self.extractMacro(oldTitle, fileLines)
        newLines = self.excludeTemplateFromFileLines(oldTitle, fileLines)
        newLines.append(newTitle + "\n")
        newLines.append(macro)
        newLines.append(self.ENDOFTEMPLATEMARKER + "\n")
        newLines = self.collapseNewLines(newLines)

        self.writeLinesIntoFile(newLines)

    def excludeTemplateFromFileLines(self, templateTitle, fileLines):
        lines = []
        deletingTemplate = False
        for line in fileLines:
            if line.strip("\n") == templateTitle:
                deletingTemplate = True

            if not deletingTemplate:
                lines.append(line)
            else:
                if line.strip("\n") == self.ENDOFTEMPLATEMARKER:
                    deletingTemplate = False

        return lines

    def extractMacro(self, macroTitle, fileLines):
        templateFound = False
        macro = ""
        for line in fileLines:
            if not templateFound:
                if line.strip("\n") == macroTitle:
                    templateFound = True
            else:
                if line.strip("\n") == self.ENDOFTEMPLATEMARKER:
                    break
                else:
                    macro = macro + line
        if macro == "":
            raise TemplateNotFoundException
        return macro

    def writeLinesIntoFile(self, newFileLines):
        file = open(self.TEMPLATESFILEPATH, mode='w', encoding='utf-8')
        for line in newFileLines:
            file.write(line)
        file.close()

    def collapseNewLines(self, fileLines):
        lastLine = ""
        cleanFileLines = []
        for line in fileLines:
            if not (lastLine == "\n" and line == "\n"):
                cleanFileLines.append(line)
                lastLine = line
        return cleanFileLines

    def getTemplateTitles(self):
        file = open(self.TEMPLATESFILEPATH, mode='r', encoding='utf-8')
        fileLines = file.readlines()
        file.close()

        templateTitles = []
        titleFound = False
        for line in fileLines:
            strippedLine = line.strip("\n")
            if strippedLine and not titleFound:
                templateTitles.append(strippedLine)
                titleFound = True
            if titleFound:
                if strippedLine == self.ENDOFTEMPLATEMARKER:
                    titleFound = False

        return templateTitles
