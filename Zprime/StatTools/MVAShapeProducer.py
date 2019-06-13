from Core.Module import Module
from sklearn.externals import joblib
import numpy as np

var_name = 'NNProb'

class MVAShapeProducer(Module):
    def __init__(self,name,channelDict={},binning=[],modelDict={},varFunc=None):
        self.name = name
        self.channelNames = channelDict.keys()
        self.channelDict = channelDict
        self.binning = [100,0.,1.] if not binning else binning
        self.clfDict = {}
        self.varFunc = varFunc
        self.modelDict = modelDict

    def begin(self):
        for model,modelPath in self.modelDict.iteritems():
            self.clfDict[model] = joblib.load(modelPath)

        for channelName in self.channelNames:
            for model in self.modelDict:
                histName = var_name+'_'+model+'_'+channelName 
                histSettingList = [histName,"TH1D",histName,"",]+self.binning
                self.writer.book(*histSettingList)

    def analyze(self,event):
        for channelName,selFunc in self.channelDict.iteritems():
            if selFunc(event): 
                for model,clf in self.clfDict.iteritems():
                    npArray = np.array(self.varFunc(event)).reshape(1, -1)
                    prob = clf.predict_proba(npArray)
                    histName = var_name+'_'+model+'_'+channelName 
                    self.writer.objs[histName].Fill(prob[0,1],event.weight)
        return True

    def end(self):
        self.varFunc.end()
        for channelName,selFunc in self.channelDict.iteritems():
            selFunc.end()
