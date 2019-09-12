import json

class ConfigReader():
    configPath = ""

    def __init__(self, configPath):
        self.configPath = configPath

    def getItems(self):
        file = open(self.configPath,"r").read()
        return  json.loads(file)["items"]

    def getMailConfig(self):
        file = open(self.configPath,"r").read()
        return  json.loads(file)["mailConfig"]


