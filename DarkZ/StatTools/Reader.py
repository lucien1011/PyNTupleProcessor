from DarkZ.StatTools.Systematic import *
from copy import deepcopy

class LogNormalSystReader(object):
    @staticmethod
    #def makeLnSyst(inputPath,skipSyst):
    def makeLnSyst(inputPath):
        textFile = open(inputPath,"r")
        lines = textFile.readlines()
        systList = []
        for line in lines:
            items = line.split()
            if line.startswith("logN"):
                processes = deepcopy(items[1:])
                continue
            if not items: continue
            if line.startswith("#"): continue
            #if items[0] in skipSyst: continue
            systDict = {}
            for i,item in enumerate(items[1:]): 
                if item == "-": continue
                systDict[processes[i]] = 1+float(item)
            lnSyst = lnNSystematic(
                        items[0],
                        [ processes[i] for i,item in enumerate(items[1:]) if item != "-"],
                        lambda syst,procName,anaBin: syst.systDict[procName],
                        )
            lnSyst.systDict = systDict
            systList.append(lnSyst)
        return systList
