# Tai Sakuma <tai.sakuma@cern.ch>

##____________________________________________________________________________||
import os
import re
from Component import Component
from ReadVersionInfo import ReadVersionInfo

##____________________________________________________________________________||
defaultExcludeList = ['Chunks', 'failed']
componentHasTheseFiles = ['log.txt']

##____________________________________________________________________________||
class HeppyResult(object):
    def __init__(self, path, componentNames = None, excludeList = defaultExcludeList):
        self.path = os.path.normpath(path)
        allComponentNames = [n for n in os.listdir(self.path) if self._isComponent(n, excludeList)]
        allComponentNames = sorted(allComponentNames, key = lambda n: [float(c) if c.isdigit() else c for c in re.findall('\d+|\D+', n)])
        if componentNames is not None:
            nonexistentComponent =  [c for c in componentNames if c not in allComponentNames]
            if len(nonexistentComponent) > 0:
                raise ValueError("No such components: " + ", ".join(nonexistentComponent))
            self.componentNames = componentNames
        else:
            self.componentNames = allComponentNames

        self._compDict = { }
        self._versionInfo = None
        self._readVersionInfo = ReadVersionInfo()

    def __getattr__(self, name):
        if name not in self._compDict:
            if name not in self.componentNames:
                raise AttributeError("'%s' object has no attribute '%s'" % (self.__class__.__name__, name))
            path = os.path.join(self.path, name)
            self._compDict[name] = Component(path)
        return self._compDict[name]

    def components(self):
        return [getattr(self, n) for n in self.componentNames]

    def _isComponent(self, name, excludeList):
        if name in excludeList: return False
        path = os.path.join(self.path, name)
        if not os.path.isdir(path): return False
        if not set(componentHasTheseFiles).issubset(set(os.listdir(path))): return False
        return True

    def versionInfo(self):
        if self._versionInfo is None:
            path = os.path.join(self.path, 'versionInfo.txt')
            self._versionInfo = self._readVersionInfo(path)
        return self._versionInfo

##____________________________________________________________________________||
