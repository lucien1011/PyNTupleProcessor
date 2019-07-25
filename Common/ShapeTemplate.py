from Core.EndModule import EndModule
from Core.Utils.printFunc import pyPrint

import os,ROOT,math

ROOT.gROOT.SetBatch(ROOT.kTRUE)

class ShapeTemplateMaker(EndModule):
    def __init__(self,config,):
        self.config = config
        self.attrNames = [
                "samples",
                "inputHistNames",
                "fitFunc",
                "outFileName",
                "objName",
                ]
        self.check_config_attr()

    def __call__(self,collector):
        for isample,sample in enumerate(self.config.samples):
            for inputHistName in self.config.inputHistNames:
                h = collector.getObj(sample,inputHistName)
                h.Fit(self.config.fitFunc,self.config.fitOption)
                funcName = "_".join([sample,inputHistName,self.config.objName])
                func = h.GetFunction(funcName)
                ROOT.gDirectory.Add(func)
                collector.addObj(funcName,func)
            collector.saveFile(self.config.inputInfo,sample,self.config.outFileName)

    def check_config_attr(self):
        for attrName in self.attrNames:
            if not hasattr(self.config,attrName): raise AttributeError,"Missing attribute "+attrName
