from macromaker.template.NoTemplateTitleException import NoTemplateTitleException
from macromaker.template.NotEnoughSpellsException import NotEnoughSpellsException
from macromaker.template.TemplateSpellExtractor import TemplateSpellExtractor
from macromaker.template.TemplatesFileHandler import TemplatesFileHandler


class TemplateHandler:
    SPELLPLACEHOLDER = "SPELL_PLACEHOLDER"
    TITLESEPARATOR = ":"
    PARAMETERS = {
        "save": ["Template title", "Macro syntax"],
        "load": ["Template title", "Spells"],
        "show": ["Template title"],
        "remove": ["Template title"],
        "change": ["Title to change", "New title"]
    }

    def __init__(self, macroMaker):
        self.templatesFileHandler = TemplatesFileHandler()
        self.macroMaker = macroMaker

    def makeMacroTemplate(self, inputText):

        return self.macroMaker.writeMacro(inputText, TemplateSpellExtractor(self.SPELLPLACEHOLDER))

    def saveTemplate(self, inputText):
        splitText = self.separateTitleAndContent(inputText)
        title = splitText[0]
        templateText = splitText[1]

        macroTemplate = self.makeMacroTemplate(templateText)

        self.templatesFileHandler.saveTemplate(title, macroTemplate)

    def makeMacroFromTemplate(self, macroTemplateText, spellsInput):

        templateSpellExtractor = TemplateSpellExtractor(self.SPELLPLACEHOLDER)
        spells = templateSpellExtractor.extractSpells(spellsInput)

        placeholderAmount = macroTemplateText.count(self.SPELLPLACEHOLDER)
        if len(spells) < placeholderAmount:
            raise NotEnoughSpellsException

        for spell in spells:
            macroTemplateText = macroTemplateText.replace(self.SPELLPLACEHOLDER, spell, 1)

        return macroTemplateText

    def loadTemplate(self, inputText):

        splitText = self.separateTitleAndContent(inputText)
        title = splitText[0]
        spellsText = splitText[1]

        macroTemplate = self.templatesFileHandler.loadTemplate(title)

        return self.makeMacroFromTemplate(macroTemplate, spellsText)

    def showTemplate(self, inputText):
        title = inputText.strip()
        textToShow = title + "\n\n"
        textToShow = textToShow + self.templatesFileHandler.loadTemplate(title)
        return textToShow

    def separateTitleAndContent(self, inputText):
        splitText = inputText.split(self.TITLESEPARATOR, 1)
        if len(splitText) < 2:
            raise NoTemplateTitleException

        result = []
        for text in splitText:
            result.append(text.strip())

        return result

    def removeTemplate(self, inputText):
        title = inputText.strip().lower()
        self.templatesFileHandler.removeTemplate(title)

    def changeTemplateTitle(self, inputText):
        titles = self.separateTitleAndContent(inputText)
        self.templatesFileHandler.changeTitleOfTemplate(titles[0], titles[1])

    def getFunctionParameters(self, functionName):
        try:
            functionParameters = self.PARAMETERS[functionName]
            parameterString = self.addParameterSign(functionParameters.pop(0))
            if functionParameters:
                parameterString = parameterString + " " + self.TITLESEPARATOR + " " + self.addParameterSign(
                    functionParameters.pop(0))
            return parameterString
        except KeyError:
            return ""

    def addParameterSign(self, parameter):
        return "<" + parameter + ">"
