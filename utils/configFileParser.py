import configparser
from pathlib import Path

class ConfigFileParser():
    def  __init__(self, configFile="qa.ini"):
        self.configFile = configFile
        self.configFileDir = 'config'
        self.Base_dir = Path(__file__).resolve().parent.parent
        self.filePath = self.Base_dir.joinpath(self.configFileDir).joinpath(self.configFile)
        self.config = configparser.ConfigParser()
        self.config.read(self.filePath)

    def getGmailURL(self):
        return self.config['gmail']['url']
    
    def getGmailUserName(self):
        return self.config['gmail']['username']
    
    def getGmailUserPassword(self):
        return self.config['gmail']['password']
    
    def getOutlookURL(self):
        return self.config['outlook']['url']
    
    def getOutlookUserName(self):
        return self.config['outlook']['username']
    
    def getOutlookUserPassword(self):
        return self.config['outlook']['password']
    

if __name__ == '__main__':
    obj = ConfigFileParser('prod.ini')
    print(obj.getGmailURL())