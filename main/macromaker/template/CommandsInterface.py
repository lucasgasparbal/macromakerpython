from macromaker.template.ChangeTitleCommand import ChangeTitleCommand
from macromaker.template.CommandNotFoundException import CommandNotFoundException
from macromaker.template.LoadCommand import LoadCommand
from macromaker.template.RemoveCommand import RemoveCommand
from macromaker.template.SaveCommand import SaveCommand
from macromaker.template.ShowCommand import ShowCommand
from macromaker.template.TemplateHandler import TemplateHandler


class CommandsInterface:
    commands = {}

    def __init__(self, macromaker):
        templateHandler = TemplateHandler(macromaker)
        saveCommand = SaveCommand(templateHandler)
        loadCommand = LoadCommand(templateHandler)
        showCommand = ShowCommand(templateHandler)
        removeCommand = RemoveCommand(templateHandler)
        changeTitleCommand = ChangeTitleCommand(templateHandler)
        self.commands = {
            "add": saveCommand,
            "save": saveCommand,
            "savetemplate": saveCommand,
            "load": loadCommand,
            "loadtemplate": loadCommand,
            "show": showCommand,
            "showtemplate": showCommand,
            "remove": removeCommand,
            "removetemplate": removeCommand,
            "delete": removeCommand,
            "del": removeCommand,
            "deletetemplate": removeCommand,
            "change": changeTitleCommand,
            "changetitle": changeTitleCommand

        }

    def executeCommand(self, commandKey, textInput):
        command = self.commands.get(commandKey)
        if command:
            command.execute(textInput)
        else:
            raise CommandNotFoundException

    def getCommandsAndParameters(self):
        alreadyProcessedCommands = []
        commandsAndParameters = {}

        for key in self.commands.keys():

            command = self.commands[key]
            if command in alreadyProcessedCommands:
                continue

            alreadyProcessedCommands.append(command)
            commandsAndParameters[key] = command.getParameters()

        return commandsAndParameters