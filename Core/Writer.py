import os,ROOT

supportRootObjs = ["TH1D","TH2D",]

class Writer(object):
    def __init__(self,dataset,outputInfo):
        self.outputInfo = outputInfo
        self.dataset = dataset
        self.outputDir = self.outputInfo.outputDir+"/"+self.dataset.name+"/"
        self.TFile = None
        self.objs = {}
        self.rootObjs = {}
    
    @staticmethod
    def makedirs(outputDir):
        if not os.path.exists(os.path.abspath(outputDir)):
            os.makedirs(os.path.dirname(outputDir))

    def makeTFile(self,fileName="test.root"):        
        self.makedirs(self.outputDir)
        self.TFile = ROOT.TFile(self.outputDir+"/"+fileName,"RECREATE")

    def initObjects(self):
        if hasattr(self.outputInfo,"TFileName"):
            self.makeTFile(fileName=self.outputInfo.TFileName)

    def closeTFile(self):
        if self.TFile:
            self.TFile.Close()

    def closeAll(self):
        self.closeTFile()

    def book(self,keyName,objType,*args):
        if keyName not in self.objs:
            self.objs[keyName] = self.createObj(objType,*args)
            if objType in supportRootObjs:
                self.rootObjs[keyName] = self.objs[keyName]
        else:
            raise RuntimeError, "Object with internal name "+keyName+" exists in the writer"
            
    def createObj(self,objType,*args):
        if objType in supportRootObjs:
            obj = getattr(ROOT,objType)(*args)
            return obj 

    def write(self):
        self.TFile.Write()

