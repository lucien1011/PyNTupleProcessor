import os

local_str = "Local"
remote_str = "Remote"

class System(object):
    def __init__(self):
        self.local_str = local_str
        self.remote_str = remote_str

    def getSystemMode(self):
        return os.environ["NTUPLERUNNER_MODE"]

    def getStoragePath(self):
        return os.environ["NTUPLERUNNER_STORAGE"]
    
    def getPublicHtmlPath(self):
        return os.environ["NTUPLERUNNER_WWW"]

system = System()
