import ROOT
from Core.Module import Module
import bisect
import pickle
import os,copy
from math import sqrt

class Triggereff(Module):

    def __init__(self, name, filenameTrigeff = [(20.2,'EfficienciesAndSF_RunBtoF.root'),(16.6,'EfficienciesAndSF_Period4.root')], Trigeffhistpath2 = "IsoMu24_OR_IsoTkMu24_PtEtaBins/pt_abseta_ratio", Trigeffhistpath = "IsoMu24_OR_IsoTkMu24_PtEtaBins/efficienciesDATA/pt_abseta_DATA", flatTrigSyst = 0.):
        self.filenameTrigeff = [(weight, "/home/kshi/SUSY/CMSSW_8_0_25/src/UF-PyNTupleRunner/DataMC/Trigger_Eff/Run2016/"+filename) for (weight, filename) in filenameTrigeff]
        self.flatTrigSyst = flatTrigSyst
        self.Trigeffhistpath = Trigeffhistpath
        
    #def beginJob(self):
        self.fileTrigeff = [(weight, ROOT.TFile(filepath)) for (weight, filepath) in self.filenameTrigeff]
        for (_, rootfile) in self.fileTrigeff:
            recursiveHistCheck(rootfile, self.Trigeffhistpath)

        self.TrigeffHist = [(weight, rootfile.Get(self.Trigeffhistpath)) for (weight, rootfile) in self.fileTrigeff]

        self.TrigeffHistTuple = [(weight, self.histToPickle(hist)) for (weight, hist) in self.TrigeffHist]

        #self.muon_pt = event.muons[0].pt
        #self.muon_eta = event.muons[0].eta

    def histToPickle(self, hist):
        xs = [hist.GetXaxis().GetBinLowEdge(iX) for iX in range(hist.GetNbinsX()+2)]
        ys = [hist.GetYaxis().GetBinLowEdge(iY) for iY in range(hist.GetNbinsY()+2)]
        sf = {}
        for iX in range(len(xs)):
            if len(ys) > 3: # 2D hist
                for iY in range(len(ys)):
                    sf[iX, iY] = (hist.GetBinContent(iX, iY), hist.GetBinError(iX, iY))
            else: # 1D hist
                sf[iX] = (hist.GetBinContent(iX), hist.GetBinError(iX))
        if len(ys) > 3: return xs, ys, sf
        else:           return xs, sf

    def analyze(self,event):

        self.muon_pt = event.muons[0].pt
        #print(self.muon_pt)
        self.muon_eta = event.muons[0].eta
        #print(abs(self.muon_eta))
        if self.dataset.isData: return True
        if self.muon_pt == 0: return True
        statErrSq = 0.0
        systErr = 0.0
        event.muonSfWeight_Up = 1.0
        event.muonSfWeight_Down = 1.0

        eff = 1.0

        TrigeffMax = self.TrigeffHist[0][1].GetXaxis().GetBinLowEdge(self.TrigeffHist[0][1].GetNbinsX()+1)
        Trigeff, Trigerr = self.getLeptonEfficiencyFromDict(self.TrigeffHistTuple, [self.muon_pt, abs(self.muon_eta)], TrigeffMax)
        #print(Trigeff)
        
        if Trigeff: statErrSq += (Trigerr/Trigeff)**2
        systErr += abs(self.flatTrigSyst)
        
        eff *= Trigeff

        event.weight *= eff
        #print(event.weight)

        if eff:
            errSq = statErrSq + (systErr)**2
            event.muonSfWeight_Up = 1 + sqrt(errSq)
            event.muonSfWeight_Down = 1 - sqrt(errSq)
        else:
            event.muonSfWeight_Up = 0.
            event.muonSfWeight_Down = 0.

        return True
    
    @staticmethod
    def getLeptonEfficiency(hist,pt,eta,maxpt = 120.0):
        if pt > maxpt: pt = maxpt - 1.0
        eff = hist.GetBinContent(hist.GetXaxis().FindBin(pt),hist.GetYaxis().FindBin(abs(eta)))
        err = hist.GetBinError(hist.GetXaxis().FindBin(pt),hist.GetYaxis().FindBin(abs(eta)))
        return eff,err

    @staticmethod
    def getLeptonEfficiencyFromDict(weightTupleList, params, maxX = 120.0):
        weightedAvg = [0., 0., 0.]
        for (weight, dictTuple) in weightTupleList:
            if params[0] > maxX: params[0] = maxX - 1.0
            iX = max(0, bisect.bisect(dictTuple[0], params[0])-1)
            if len(params)==1: # 1D
                sf = dictTuple[1][iX]
            elif len(params)==2: # 2D
                iY = max(0, bisect.bisect(dictTuple[1], params[1])-1)
                sf = dictTuple[2][iX, iY]
            else:
                raise IndexError("{0} should be length 1 or 2".format(params))
            weightedAvg[0] +=  weight*1.
            weightedAvg[1] +=  weight*sf[0]
            weightedAvg[2] += (weight*sf[1])**2
        return weightedAvg[1]/weightedAvg[0], sqrt(weightedAvg[2])/weightedAvg[0]

def recursiveHistCheck(rootfile, histpath):
    histpaths = histpath.split('/')
    rdir = rootfile
    for i in range(len(histpaths)-1):
        if not rdir.GetListOfKeys().Contains(histpaths[i]):
            raise RuntimeError("{0} not in {1}".format(histpaths[i], rootfile))
        rdir = rdir.Get(histpaths[i])
    return True

