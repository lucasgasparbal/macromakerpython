class TargetParser:
    def __init__(self):
        self.TARGETS = {
            "self": "player",
            "player": "player",
            "focus": "focus, exists",
            "mouseover": "mouseover, exists"
        }

    def parse(self, stringsToParse):

        for string in stringsToParse:
            parsedString = self.TARGETS.get(string)
            if parsedString:
                return parsedString

        return ""
