# Tai Sakuma <tai.sakuma@cern.ch>
import os
import ROOT
from ..Events import BEvents

##____________________________________________________________________________||
class BEventBuilder(object):
    def __init__(self, analyzerName, fileName, treeName, maxEvents = -1):
        self._analyzerName = analyzerName
        self._fileName = fileName
        self._treeName = treeName
        self._maxEvents = maxEvents

    def build(self, component):
        inputPath = os.path.join(getattr(component, self._analyzerName).path, self._fileName)
        file = ROOT.TFile.Open(inputPath)
        tree = file.Get(self._treeName)
        return BEvents(tree, self._maxEvents)

##____________________________________________________________________________||
