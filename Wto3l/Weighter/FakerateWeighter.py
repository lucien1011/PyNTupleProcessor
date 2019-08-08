from Core.Module import Module
import ROOT

class FakerateWeighter(Module):
    def __init__(self,name):
        super(FakerateWeighter,self).__init__(name)
        self.inputPath       = "/raid/raid7/kshi/Zprime/Wto3l/FakeRate/Run2016/2019-08-06/finalstate_eem/fr_ratio_WOZpeak/ratioPlot.root"
        #self.inputPath       = "/raid/raid7/kshi/Zprime/Wto3l/FakeRate/Run2016/2019-08-06/finalstate_eem/fr_ratio/ratioPlot.root"
        #self.inputPath       = "/raid/raid7/kshi/Zprime/Wto3l/FakeRate/Run2016/2019-07-31/finalstate_mem/fr_ratio_MET100/ratioPlot.root"
        #inputFileName   = "ratioPlot.root"
        self.histName_endcap = "fr_endcap"
        self.histName_barrel = "fr_barrel"

    def analyze(self,event):
        inputFile   = ROOT.TFile(self.inputPath,"READ")
        endcap_hist = inputFile.Get(self.histName_endcap)
        barrel_hist = inputFile.Get(self.histName_barrel)      
        if ("Data_Run2016" in self.dataset.name) or ("Data_memCR_Run2016" in self.dataset.name):
        #if "Data_memCR_Run2016" in self.dataset.name:
            if event.etaL3[0] <= 1.4:
                if event.pTL3[0] < 2:
                    tmp_fr = barrel_hist.GetBinContent(1)
                    event.weight *= tmp_fr
                if 2 <= event.pTL3[0] < 4:
                    tmp_fr = barrel_hist.GetBinContent(2)
                    event.weight *= tmp_fr
                if 4 <= event.pTL3[0] < 6:
                    tmp_fr = barrel_hist.GetBinContent(3)
                    event.weight *= tmp_fr
                if 6 <= event.pTL3[0] < 8:
                    tmp_fr = barrel_hist.GetBinContent(4)
                    event.weight *= tmp_fr
                if 8 <= event.pTL3[0] < 10:
                    tmp_fr = barrel_hist.GetBinContent(5)
                    event.weight *= tmp_fr
                if 10 <= event.pTL3[0] < 13:
                    tmp_fr = barrel_hist.GetBinContent(6)
                    event.weight *= tmp_fr
                if 13 <= event.pTL3[0] < 17:
                    tmp_fr = barrel_hist.GetBinContent(7)
                    event.weight *= tmp_fr
                if 17 <= event.pTL3[0] < 20:
                    tmp_fr = barrel_hist.GetBinContent(8)
                    event.weight *= tmp_fr
                if 20 <= event.pTL3[0] < 25:
                    tmp_fr = barrel_hist.GetBinContent(9)
                    event.weight *= tmp_fr
                if 25 <= event.pTL3[0] < 35:
                    tmp_fr = barrel_hist.GetBinContent(10)
                    event.weight *= tmp_fr
                if event.pTL3[0] >= 35:
                    tmp_fr = barrel_hist.GetBinContent(11)
                    event.weight *= tmp_fr
            if 1.4 < event.etaL3[0] < 2.5:
                if event.pTL3[0] < 2:
                    tmp_fr = endcap_hist.GetBinContent(1)
                    event.weight *= tmp_fr
                if 2 <= event.pTL3[0] < 4:
                    tmp_fr = endcap_hist.GetBinContent(2)
                    event.weight *= tmp_fr
                if 4 <= event.pTL3[0] < 6:
                    tmp_fr = endcap_hist.GetBinContent(3)
                    event.weight *= tmp_fr
                if 6 <= event.pTL3[0] < 8:
                    tmp_fr = endcap_hist.GetBinContent(4)
                    event.weight *= tmp_fr
                if 8 <= event.pTL3[0] < 10:
                    tmp_fr = barrel_hist.GetBinContent(5)
                    event.weight *= tmp_fr
                if 10 <= event.pTL3[0] < 13:
                    tmp_fr = barrel_hist.GetBinContent(6)
                    event.weight *= tmp_fr
                if 13 <= event.pTL3[0] < 17:
                    tmp_fr = barrel_hist.GetBinContent(7)
                    event.weight *= tmp_fr
                if 17 <= event.pTL3[0] < 20:
                    tmp_fr = barrel_hist.GetBinContent(8)
                    event.weight *= tmp_fr
                if 20 <= event.pTL3[0] < 25:
                    tmp_fr = barrel_hist.GetBinContent(9)
                    event.weight *= tmp_fr
                if 25 <= event.pTL3[0] < 35:
                    tmp_fr = barrel_hist.GetBinContent(10)
                    event.weight *= tmp_fr
                if event.pTL3[0] >= 35:
                    tmp_fr = endcap_hist.GetBinContent(11)
                    event.weight *= tmp_fr
        return True

