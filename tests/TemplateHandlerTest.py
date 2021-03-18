import unittest

from macromaker.NoSpellException import NoSpellException
from macromaker.template.NoTemplateTitleException import NoTemplateTitleException
from macromaker.template.NotEnoughSpellsException import NotEnoughSpellsException
from macromaker.template.TemplateHandler import TemplateHandler


class TemplateHandlerTEst(unittest.TestCase):

    def test1TemplateHandlerMakeMacroTemplateWithNoInputTextReturnsACastOnlyTemplate(self):
        templateHandler = TemplateHandler()

        expectedMacro = "#showtooltip\n" \
                        "/cast SPELL_PLACEHOLDER"

        self.assertEqual(expectedMacro, templateHandler.makeMacroTemplate(""))

    def test2TemplateHandlerMakeMacroTemplateWithConditionsReturnsExpectedMacro(self):
        templateHandler = TemplateHandler()

        expectedMacro = "#showtooltip\n" \
                        "/cast [@player, help, nodead] SPELL_PLACEHOLDER"

        self.assertEqual(expectedMacro, templateHandler.makeMacroTemplate("player ally alive"))

    def test3TemplateHandlerMakeMacroTemplateWithMoreThanOneConditionBlockReturnsExpectedMacro(self):
        templateHandler = TemplateHandler()

        expectedMacro = "#showtooltip\n" \
                        "/cast [@player, help, nodead][@target, harm, dead] SPELL_PLACEHOLDER"

        self.assertEqual(expectedMacro, templateHandler.makeMacroTemplate("player ally alive | target enemy dead"))

    def test4TemplateHandlerMakeMacroTemplateWithMoreThanOneConditionBlockAndMoreThanOneStatementReturnsExpectedMacro(
            self):
        templateHandler = TemplateHandler()

        expectedMacro = "#showtooltip\n" \
                        "/cast [@player, help, nodead][@target, harm, dead] SPELL_PLACEHOLDER; [@mouseover, exists, " \
                        "help, nodead][@focus, exists, harm] SPELL_PLACEHOLDER"

        self.assertEqual(expectedMacro, templateHandler.makeMacroTemplate("player ally alive | target enemy dead; "
                                                                          "mouseover ally alive | focus enemy"))

    def test5TemplateHandlerMakeMacroTemplateWithConditionsAndASpellInsideItReturnsExpectedMacroIgnoringSpell(self):
        templateHandler = TemplateHandler()

        expectedMacro = "#showtooltip\n" \
                        "/cast [@player, help, nodead] SPELL_PLACEHOLDER"

        self.assertEqual(expectedMacro, templateHandler.makeMacroTemplate('player ally alive "Chain Heal"'))

    def test6TemplateHandlerMakeMacroFromTemplateRaisesExceptionIfNoSpellIsDetected(self):
        templateHandler = TemplateHandler()
        macroTemplate = "#showtooltip\n" \
                        "/cast [@player, help, nodead] SPELL_PLACEHOLDER"

        self.assertRaises(NoSpellException,templateHandler.makeMacroFromTemplate,macroTemplate,"")

    def test7TemplateHandlerMakeMacroFromTemplateRaisesExceptionIfThereAreLessSpellsThanPlaceholders(self):
        templateHandler = TemplateHandler()
        macroTemplate = "#showtooltip\n" \
                        "/cast [@player, help, nodead][@target, harm, dead] SPELL_PLACEHOLDER; [@mouseover, exists, " \
                        "help, nodead][@focus, exists, harm] SPELL_PLACEHOLDER"

        self.assertRaises(NotEnoughSpellsException,templateHandler.makeMacroFromTemplate,macroTemplate,'"Chain Heal"')

    def test8TemplateHandlerMakeMacroFromTemplateMakesCorrectMacroWithOneSpell(self):
        templateHandler = TemplateHandler()
        macroTemplate = "#showtooltip\n" \
                        "/cast [@player, help, nodead] SPELL_PLACEHOLDER"
        expectedMacro = "#showtooltip\n" \
                        "/cast [@player, help, nodead] Chain Heal"

        self.assertEqual(expectedMacro,templateHandler.makeMacroFromTemplate(macroTemplate,'"Chain Heal"'))

    def test9TemplateHandlerMakeMacroFromTemplateMakesCorrectMacroWithMoreThanOneSpell(self):
        templateHandler = TemplateHandler()
        macroTemplate = "#showtooltip\n" \
                        "/cast [@player, help, nodead][@target, harm, dead] SPELL_PLACEHOLDER; [@mouseover, exists, " \
                        "help, nodead][@focus, exists, harm] SPELL_PLACEHOLDER"
        expectedMacro = "#showtooltip\n" \
                        "/cast [@player, help, nodead][@target, harm, dead] Chain Heal; [@mouseover, exists, " \
                        "help, nodead][@focus, exists, harm] Riptide"

        self.assertEqual(expectedMacro,templateHandler.makeMacroFromTemplate(macroTemplate,'"Chain Heal" "Riptide"'))

    def test10TemplateHandlerMakeMacroFromTemplateMakesCorrectMacroWithMoreThanOneRepeatedSpell(self):
        templateHandler = TemplateHandler()
        macroTemplate = "#showtooltip\n" \
                        "/cast [@player, help, nodead][@target, harm, dead] SPELL_PLACEHOLDER; [@mouseover, exists, " \
                        "help, nodead][@focus, exists, harm] SPELL_PLACEHOLDER"
        expectedMacro = "#showtooltip\n" \
                        "/cast [@player, help, nodead][@target, harm, dead] Chain Heal; [@mouseover, exists, " \
                        "help, nodead][@focus, exists, harm] Chain Heal"

        self.assertEqual(expectedMacro,templateHandler.makeMacroFromTemplate(macroTemplate,'"Chain Heal" "Chain Heal"'))

    def test11TemplateHandlerMakeMacroFromTemplateMakesCorrectMacroWithMoreThanOneSpellIgnoringNoSpellInput(self):
        templateHandler = TemplateHandler()
        macroTemplate = "#showtooltip\n" \
                        "/cast [@player, help, nodead][@target, harm, dead] SPELL_PLACEHOLDER; [@mouseover, exists, " \
                        "help, nodead][@focus, exists, harm] SPELL_PLACEHOLDER"
        expectedMacro = "#showtooltip\n" \
                        "/cast [@player, help, nodead][@target, harm, dead] Chain Heal; [@mouseover, exists, " \
                        "help, nodead][@focus, exists, harm] Riptide"

        self.assertEqual(expectedMacro,templateHandler.makeMacroFromTemplate(macroTemplate,'"Chain Heal" banana apple '
                                                                                           '"Riptide" pineapple'))

    def test12TemplateHandlerSeparateTitleRaisesExceptionIfNoTitleIsFound(self):
        templateHandler = TemplateHandler()

        self.assertRaises(NoTemplateTitleException, templateHandler.separateTitleAndContent,"")

    def test13TemplateHandlerSeparatesTitleFromContent(self):
        templateHandler = TemplateHandler()
        splitText = templateHandler.separateTitleAndContent("Macro Title : this is macro content")
        self.assertEquals("Macro Title", splitText[0])

    def test14TemplateHandlerSeparatesTitleFromContent(self):
        templateHandler = TemplateHandler()
        splitText = templateHandler.separateTitleAndContent("Macro Title : this is macro content")
        self.assertEquals("Macro Title", splitText[0])

    def test15TemplateHandlerSeparatesTitleFromContentKeepsContentAsIs(self):
        templateHandler = TemplateHandler()
        splitText = templateHandler.separateTitleAndContent("Macro Title : this is macro content")
        self.assertEquals("this is macro content", splitText[1])

if __name__ == '__main__':
    unittest.main()
