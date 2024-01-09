import configparser


config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL_of_Demo_QA():
        url = config.get('common info','URL')
        return url
