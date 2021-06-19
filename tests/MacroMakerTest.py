import unittest
from macromaker.MacroMaker import MacroMaker
from macromaker.NoSpellException import NoSpellException


class MacroMakerTest(unittest.TestCase):
    def test01MacroMakerMakeMacroWithNoInputRaisesNoSpellException(self):
        macromaker = MacroMaker()

        self.assertRaises(NoSpellException, macromaker.makeMacro,"")

    def test02MacroMakerMakeMacroWithNonDiscernibleInputRaisesNoSpellException(self):
        macromaker = MacroMaker()

        self.assertRaises(NoSpellException, macromaker.makeMacro, "apple banana candle dice emu")

    def test03MacroMakerMakeMacroWithCorrectInputButNoSpellRaisesNoSpellException(self):
        macromaker = MacroMaker()

        self.assertRaises(NoSpellException, macromaker.makeMacro, "player alt alive | mouseover dead enemy; mousever "
                                                                  "ally alive")

    def test04MacroMakerMakeMacroWithOnlySpellInputReturnsCorrectMacro(self):
        macromaker = MacroMaker()

        expectedMacro = "#showtooltip\n" \
                        "/cast Riptide"

        self.assertEqual(expectedMacro,macromaker.makeMacro('"Riptide"'))

    def test05MacroMakerMakeMacroWithASpellUsingSpacesInputReturnsCorrectMacro(self):
        macromaker = MacroMaker()

        expectedMacro = "#showtooltip\n" \
                        "/cast Chain Heal"

        self.assertEqual(expectedMacro,macromaker.makeMacro('"Chain Heal"'))

    def test06MacroMakerMakeMacroWithSpellAndConditionInputReturnsCorrectMacro(self):
        macromaker = MacroMaker()

        expectedMacro = "#showtooltip\n" \
                        "/cast [@mouseover, exists, help, nodead] Chain Heal"

        self.assertEqual(expectedMacro, macromaker.makeMacro('mouseover ally alive "Chain Heal"'))

    def test06MacroMakerMakeMacroWithSpellAndConditionInputDisregardsCapitalizationOfConditionsAndReturnsCorrectMacro(self):
        macromaker = MacroMaker()

        expectedMacro = "#showtooltip\n" \
                        "/cast [@mouseover, exists, help, nodead] Chain Heal"

        self.assertEqual(expectedMacro, macromaker.makeMacro('MouSeoVeR Ally ALIVE "Chain Heal"'))

    def test07MacroMakerMakeMacroWithSpellAndMoreThanOneConditionBlockReturnsCorrectMacro(self):
        macromaker = MacroMaker()

        expectedMacro = "#showtooltip\n" \
                        "/cast [@player, mod:alt][@mouseover, exists, help, nodead] Chain Heal"

        self.assertEqual(expectedMacro, macromaker.makeMacro(' player alt | mouseover ally alive "Chain Heal"'))

    def test08MacroMakerMakeMacroWithMoreThanOneStatementButMissingASpellRaisesException(self):
        macromaker = MacroMaker()

        self.assertRaises(NoSpellException, macromaker.makeMacro, ' player alt | mouseover ally alive "Chain Heal"; target shift banana')

    def test09MacroMakerMakeMacroWithMoreThanOneStatementReturnsCorrectMacro(self):
        macromaker = MacroMaker()

        expectedMacro = "#showtooltip\n" \
                        "/cast [@mouseover, exists, help, nodead] Chain Heal; [harm] Chain Lightning"

        self.assertEqual(expectedMacro, macromaker.makeMacro(' mouseover ally alive "Chain Heal"; enemy "Chain Lightning"'))

    def test10MacroMakerMakeMacroWithVariousStatementsAndConditionBlocksReturnsCorrectMacro(self):
        macromaker = MacroMaker()

        expectedMacro = "#showtooltip\n" \
                        "/cast [@player, mod:shift+alt][@mouseover, exists, help, nodead] Chain Heal; " \
                        "[harm][@mouseover, exists, harm, nodead] Chain Lightning"

        self.assertEqual(expectedMacro,
                         macromaker.makeMacro('player shift alt | mouseover ally alive "Chain Heal"; enemy | '
                                              'mouseover enemy alive "Chain Lightning"'))


if __name__ == '__main__':
    unittest.main()
