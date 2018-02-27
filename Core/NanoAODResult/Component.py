# Lucien Lo <lucienlo@cern.ch>

##____________________________________________________________________________||
import os
from UFTier2Utils import listdir_uberftp
from FileInfo import FileInfo

##____________________________________________________________________________||
class Component(object):
    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.fileNames = [n for n in listdir_uberftp(self.path) if n.endswith(".root") and "tree" in n]

        self._fileDict = { }
        self._cfg = None

    def __getattr__(self, name):
        if name not in self._fileDict:
            if name not in self.fileNames:
                raise AttributeError("'%s' object has no attribute '%s'" % (self.__class__.__name__, name))
            path = os.path.join(self.path, name)
            self._fileDict[name] = FileInfo(path)
        return self._fileDict[name]

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, dict):
        self.__dict__ = dict

    def fileInfos(self):
        return [getattr(self, n) for n in self.fileNames]

##____________________________________________________________________________||
