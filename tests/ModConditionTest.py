import unittest
from macromaker.conditionparsing.ModCondition import ModCondition

class TestModCondition(unittest.TestCase):

    def test01ModConditionWithoutAnyKeysAddedReturnsEmptyString(self):
        modCondition = ModCondition()

        self.assertEqual("", modCondition.write())

    def test02ModConditionWithoutAnyKeysAddAltKeyReturnsCorrectString(self):
        modCondition = ModCondition()
        modCondition.addMod("alt")
        self.assertEqual("mod:alt", modCondition.write())

    def test03ModConditionWithAltKeysDoesNotAddAnotherAltKey(self):
        var = ModCondition()
        var.addMod("alt")
        var.addMod("alt")
        self.assertEqual("mod:alt", var.write())

    def test04ModConditionWithAltKeyDoesNotAddAnythingWithANonKeyInput(self):
        var = ModCondition()
        var.addMod("alt")
        var.addMod("banana")
        self.assertEqual("mod:alt", var.write())

    def test05ModConditionWithAltKeyAddsControlWithCtrlInput(self):
        var = ModCondition()
        var.addMod("alt")
        var.addMod("ctrl")
        self.assertEqual("mod:alt+ctrl", var.write())

    def test06ModConditionWithAltAndCtrlAddsShiftCorrectly(self):
        var = ModCondition()
        var.addMod("alt")
        var.addMod("ctrl")
        var.addMod("shift")
        self.assertEqual("mod:alt+ctrl+shift", var.write())

    def test06ModConditionWithAllKeysDoesntAddAnythingElse(self):
        var = ModCondition()
        var.addMod("alt")
        var.addMod("ctrl")
        var.addMod("shift")
        var.addMod("shift")
        var.addMod("shift")
        var.addMod("ctrl")
        var.addMod("alt")
        self.assertEqual("mod:alt+ctrl+shift", var.write())

    def test07ModConditionEmptyDoesntAddAnythingWithNonKeyInput(self):
        modCondition = ModCondition()
        modCondition.addMod("pineapple")
        self.assertEqual("", modCondition.write())
