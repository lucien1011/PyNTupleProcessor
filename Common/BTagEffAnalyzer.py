from Core.Module import Module
from Core.Collection import Collection
from DataMC.BTagging.BTagWorkingPoints import BTagWorkingPoints
import os
import pickle
from array import array
import ROOT as r

class BTagEffAnalyzer(Module):
    """
    Calculate b-tagging efficiencies as a function of jet pt and eta
    """
    def __init__(self,name,era="2016Moriond17",tagger = "CSV",jetCollName="selJets25"):
        super(BTagEffAnalyzer,self).__init__(name)

        # hadronFlavour to csvFlavour conversion
        self.jetFlavorsDict = { 0:"2", 4:"1", 5:"0" }
        self._tagger = tagger


        self.btagDiscDict = { "0": BTagWorkingPoints["CSVv2IVFL"][1],
                              "1": BTagWorkingPoints["CSVv2IVFM"][1],
                              "2": BTagWorkingPoints["CSVv2IVFT"][1] }

        # self.btagDiscDict = { "0": BTagWorkingPoints["DeepCSVL"][1],
        #                       "1": BTagWorkingPoints["DeepCSVM"][1],
        #                       "2": BTagWorkingPoints["DeepCSVT"][1] }

        bsfFile = os.environ['BASE_PATH']+"/DataMC/BTagging/"+era+"/btagScaleFactors_CSVv2_Moriond17_B_H.p"

        self.bsfDict = pickle.load( open(bsfFile,"rb") )

        self.jetCollName = jetCollName

    
    def begin(self):

        for wp,measTypes in self.bsfDict.iteritems():
            for meas,sysTypes in measTypes.iteritems():
                for sys,jetFlavors in sysTypes.iteritems():
                    for flav,etaptBins in jetFlavors.iteritems():
    
                        etaBinsMin  = list( set( sorted( [ etaptBin[0][0] for etaptBin in etaptBins ] ) ) )
                        etaBinsMax  = list( set( sorted( [ etaptBin[0][1] for etaptBin in etaptBins ] ) ) )
                        
                        etaBins = etaBinsMin + etaBinsMax[-1:]
    
                        ptBinsMin   = sorted( [ etaptBin[1][0] for etaptBin in etaptBins ] )
                        ptBinsMax   = sorted( [ etaptBin[1][1] for etaptBin in etaptBins ] )
    
                        ptBins = ptBinsMin  + ptBinsMax[-1:]

                        effKey = "eff_WorkingPoint"+wp+"_MeasType"+meas+"_SysType"+sys+"_JetFlavour"+flav
                        self.writer.book(effKey,"TH2D",effKey,"",len(ptBins)-1,array('d',ptBins),len(etaBins)-1,array('d',etaBins))
                        numKey = "effNum_WorkingPoint"+wp+"_MeasType"+meas+"_SysType"+sys+"_JetFlavour"+flav
                        self.writer.book(numKey,"TH2D",numKey,"",len(ptBins)-1,array('d',ptBins),len(etaBins)-1,array('d',etaBins))
                        denKey = "effDen_WorkingPoint"+wp+"_MeasType"+meas+"_SysType"+sys+"_JetFlavour"+flav
                        self.writer.book(denKey,"TH2D",denKey,"",len(ptBins)-1,array('d',ptBins),len(etaBins)-1,array('d',etaBins))
  
    def analyze(self,event):
        
        jets = getattr(event,self.jetCollName)
        for jet in jets:
            
            jetPt   = jet.pt
            jetEta  = abs(jet.eta)
            jetFlav = self.jetFlavorsDict[jet.hadronFlavour]

            for wp in self.bsfDict:
                btagDisc = self.btagDiscDict[wp]

                for meas in self.bsfDict[wp]:
                    for sys in self.bsfDict[wp][meas]:

                        histToFill = "eff{}_WorkingPoint"+wp+"_MeasType"+meas+"_SysType"+sys+"_JetFlavour"+jetFlav
                        if histToFill.format('') not in self.writer.objs: continue

                        # Fill denominator
                        self.writer.objs[histToFill.format('Den')].Fill(jetPt,jetEta,event.weight)
    
                        # Fill numerator if it's tagged
                        if getattr(jet,"btag"+self._tagger) > btagDisc:
                            self.writer.objs[histToFill.format('Num')].Fill(jetPt,jetEta,event.weight)

        return True
