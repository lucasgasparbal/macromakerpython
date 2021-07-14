import unittest
from unittest.mock import patch

from macromaker.MacroMaker import MacroMaker
from macromaker.NoSpellException import NoSpellException
from macromaker.template.NoTemplateTitleException import NoTemplateTitleException
from macromaker.template.NotEnoughSpellsException import NotEnoughSpellsException
from macromaker.template.TemplateHandler import TemplateHandler


class TemplateHandlerTEst(unittest.TestCase):

    def test1TemplateHandlerMakeMacroTemplateWithNoInputTextReturnsACastOnlyTemplate(self):
        macromaker = MacroMaker()
        templateHandler = TemplateHandler(macromaker)

        expectedMacro = "#showtooltip\n" \
                        "/cast SPELL_PLACEHOLDER"

        self.assertEqual(expectedMacro, templateHandler.makeMacroTemplate(""))

    def test2TemplateHandlerMakeMacroTemplateWithConditionsReturnsExpectedMacro(self):
        macromaker = MacroMaker()
        templateHandler = TemplateHandler(macromaker)

        expectedMacro = "#showtooltip\n" \
                        "/cast [@player, help, nodead] SPELL_PLACEHOLDER"

        self.assertEqual(expectedMacro, templateHandler.makeMacroTemplate("player ally alive"))

    def test3TemplateHandlerMakeMacroTemplateWithMoreThanOneConditionBlockReturnsExpectedMacro(self):
        macromaker = MacroMaker()
        templateHandler = TemplateHandler(macromaker)

        expectedMacro = "#showtooltip\n" \
                        "/cast [@player, help, nodead][harm, dead] SPELL_PLACEHOLDER"

        self.assertEqual(expectedMacro, templateHandler.makeMacroTemplate("player ally alive / enemy dead"))

    def test4TemplateHandlerMakeMacroTemplateWithMoreThanOneConditionBlockAndMoreThanOneStatementReturnsExpectedMacro(
            self):
        macromaker = MacroMaker()
        templateHandler = TemplateHandler(macromaker)

        expectedMacro = "#showtooltip\n" \
                        "/cast [@player, help, nodead][harm, dead] SPELL_PLACEHOLDER; [@mouseover, exists, " \
                        "help, nodead][@focus, exists, harm] SPELL_PLACEHOLDER"

        self.assertEqual(expectedMacro, templateHandler.makeMacroTemplate("player ally alive / enemy dead; "
                                                                          "mouseover ally alive / focus enemy"))

    def test5TemplateHandlerMakeMacroTemplateWithConditionsAndASpellInsideItReturnsExpectedMacroIgnoringSpell(self):
        macromaker = MacroMaker()
        templateHandler = TemplateHandler(macromaker)

        expectedMacro = "#showtooltip\n" \
                        "/cast [@player, help, nodead] SPELL_PLACEHOLDER"

        self.assertEqual(expectedMacro, templateHandler.makeMacroTemplate('player ally alive "Chain Heal"'))

    def test6TemplateHandlerMakeMacroFromTemplateRaisesExceptionIfNoSpellIsDetected(self):
        macromaker = MacroMaker()
        templateHandler = TemplateHandler(macromaker)
        macroTemplate = "#showtooltip\n" \
                        "/cast [@player, help, nodead] SPELL_PLACEHOLDER"

        self.assertRaises(NoSpellException,templateHandler.makeMacroFromTemplate,macroTemplate,"")

    def test7TemplateHandlerMakeMacroFromTemplateRaisesExceptionIfThereAreLessSpellsThanPlaceholders(self):
        macromaker = MacroMaker()
        templateHandler = TemplateHandler(macromaker)
        macroTemplate = "#showtooltip\n" \
                        "/cast [@player, help, nodead][@target, harm, dead] SPELL_PLACEHOLDER; [@mouseover, exists, " \
                        "help, nodead][@focus, exists, harm] SPELL_PLACEHOLDER"

        self.assertRaises(NotEnoughSpellsException,templateHandler.makeMacroFromTemplate,macroTemplate,'"Chain Heal"')

    def test8TemplateHandlerMakeMacroFromTemplateMakesCorrectMacroWithOneSpell(self):
        macromaker = MacroMaker()
        templateHandler = TemplateHandler(macromaker)
        macroTemplate = "#showtooltip\n" \
                        "/cast [@player, help, nodead] SPELL_PLACEHOLDER"
        expectedMacro = "#showtooltip\n" \
                        "/cast [@player, help, nodead] Chain Heal"

        self.assertEqual(expectedMacro,templateHandler.makeMacroFromTemplate(macroTemplate,'"Chain Heal"'))

    def test9TemplateHandlerMakeMacroFromTemplateMakesCorrectMacroWithMoreThanOneSpell(self):
        macromaker = MacroMaker()
        templateHandler = TemplateHandler(macromaker)
        macroTemplate = "#showtooltip\n" \
                        "/cast [@player, help, nodead][@target, harm, dead] SPELL_PLACEHOLDER; [@mouseover, exists, " \
                        "help, nodead][@focus, exists, harm] SPELL_PLACEHOLDER"
        expectedMacro = "#showtooltip\n" \
                        "/cast [@player, help, nodead][@target, harm, dead] Chain Heal; [@mouseover, exists, " \
                        "help, nodead][@focus, exists, harm] Riptide"

        self.assertEqual(expectedMacro,templateHandler.makeMacroFromTemplate(macroTemplate,'"Chain Heal" "Riptide"'))

    def test10TemplateHandlerMakeMacroFromTemplateMakesCorrectMacroWithMoreThanOneRepeatedSpell(self):
        macromaker = MacroMaker()
        templateHandler = TemplateHandler(macromaker)
        macroTemplate = "#showtooltip\n" \
                        "/cast [@player, help, nodead][@target, harm, dead] SPELL_PLACEHOLDER; [@mouseover, exists, " \
                        "help, nodead][@focus, exists, harm] SPELL_PLACEHOLDER"
        expectedMacro = "#showtooltip\n" \
                        "/cast [@player, help, nodead][@target, harm, dead] Chain Heal; [@mouseover, exists, " \
                        "help, nodead][@focus, exists, harm] Chain Heal"

        self.assertEqual(expectedMacro,templateHandler.makeMacroFromTemplate(macroTemplate,'"Chain Heal" "Chain Heal"'))

    def test11TemplateHandlerMakeMacroFromTemplateMakesCorrectMacroWithMoreThanOneSpellIgnoringNoSpellInput(self):
        macromaker = MacroMaker()
        templateHandler = TemplateHandler(macromaker)
        macroTemplate = "#showtooltip\n" \
                        "/cast [@player, help, nodead][@target, harm, dead] SPELL_PLACEHOLDER; [@mouseover, exists, " \
                        "help, nodead][@focus, exists, harm] SPELL_PLACEHOLDER"
        expectedMacro = "#showtooltip\n" \
                        "/cast [@player, help, nodead][@target, harm, dead] Chain Heal; [@mouseover, exists, " \
                        "help, nodead][@focus, exists, harm] Riptide"

        self.assertEqual(expectedMacro,templateHandler.makeMacroFromTemplate(macroTemplate,'"Chain Heal" banana apple '
                                                                                           '"Riptide" pineapple'))

    def test12TemplateHandlerSeparateTitleRaisesExceptionIfNoTitleIsFound(self):
        macromaker = MacroMaker()
        templateHandler = TemplateHandler(macromaker)

        self.assertRaises(NoTemplateTitleException, templateHandler.separateTitleAndContent,"")

    def test13TemplateHandlerSeparatesTitleFromContent(self):
        macromaker = MacroMaker()
        templateHandler = TemplateHandler(macromaker)
        splitText = templateHandler.separateTitleAndContent("Macro Title : this is macro content")
        self.assertEquals("Macro Title", splitText[0])

    def test14TemplateHandlerSeparatesTitleFromContent(self):
        macromaker = MacroMaker()
        templateHandler = TemplateHandler(macromaker)
        splitText = templateHandler.separateTitleAndContent("Macro Title : this is macro content")
        self.assertEquals("Macro Title", splitText[0])

    def test15TemplateHandlerSeparatesTitleFromContentKeepsContentAsIs(self):
        macromaker = MacroMaker()
        templateHandler = TemplateHandler(macromaker)
        splitText = templateHandler.separateTitleAndContent("Macro Title : this is macro content")
        self.assertEquals("this is macro content", splitText[1])

if __name__ == '__main__':
    unittest.main()
