from Core.Module import Module
import os 
import collections

class PUWeighter(Module):

    """Carry out PU Reweighting given an input LUT"""

    def __init__(self, name, puFile, doNTrueInt=False, applySystVariation=False,):
        super(PUWeighter,self).__init__(name)

        self._weightFile  = puFile
        self._doNTrueInt = doNTrueInt
        self.applySystVariation = applySystVariation

        self._indexCentral = 1
        self._indexUp      = 2
        self._indexDown    = 3

        self._verbose = True
        
        pass
        
    def begin(self):

        fileDict = loadFile(self._weightFile,self._indexCentral)

        self.doVary = True
        try:
            fileDict_Up = loadFile(self._weightFile,self._indexUp)
            fileDict_Do = loadFile(self._weightFile,self._indexDown)
        except IndexError:
            if self._verbose: 
                print "Up and down PU weights not given - will only compute central weight"
            self.doVary = False            

        self._weightDict = makeIntegerDict(fileDict)
        if self.doVary:
            self._weightDict_Up = makeIntegerDict(fileDict_Up)
            self._weightDict_Do = makeIntegerDict(fileDict_Do)
        pass


    def analyze(self,event,key = None):

        if self.dataset.isMC:
            nVert = event.Pileup_nTrueInt

            if nVert[0] > self._weightDict.keys()[-1]:
                event.puWeight = self._weightDict.values()[-1]
                if self.doVary:
                    event.puWeight_Up   = self._weightDict_Up.values()[-1] / event.puWeight
                    event.puWeight_Down = self._weightDict_Do.values()[-1] / event.puWeight
                    pass
                pass
            
            else:
                event.puWeight = self._weightDict[nVert[0]]
                if self.doVary:
                    event.puWeight_Up   = self._weightDict_Up[nVert[0]] / event.puWeight
                    event.puWeight_Down = self._weightDict_Do[nVert[0]] / event.puWeight
                    pass
                pass
            event.weight *= event.puWeight
            pass
        return True


# --------------------------------------------------------------------------------

# Load a file with two columns into a dictionary
def loadFile( fileName, weightIndex ):

    fileDict = collections.OrderedDict()
    with open(fileName) as f:
        for line in f.readlines():
            splitLine = line.split()
            if splitLine==[]: continue
            fileDict[splitLine[0]] = splitLine[weightIndex]

    return fileDict

# Turn an input dictionary into one with an entry for every possible integer
def makeIntegerDict( inputDict ):
    
    outDict = collections.OrderedDict()

    prevKey = -1
    prevValue = -1

    for key,value in inputDict.iteritems():

        if prevKey==-1 or prevValue==-1:
            pass
        else:
            for i in range(prevKey,int(float(key))):
                outDict[i]=prevValue

        prevKey = int(float(key))
        prevValue = float(value)

    outDict[prevKey]=prevValue

    return outDict
