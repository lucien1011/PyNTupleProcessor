from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from DarkZ.Dataset.Run2017.ZXCR_MC_DarkPhoton import * 
from DarkZ.Dataset.Run2017.ZXCR_Data_DarkPhoton import * 

from DarkZ.Sequence.RecoSequence import * 

from DarkZ.StatTools.ParaYieldProducer import ParaYieldProducer
from DarkZ.StatTools.Syst import Syst
from DarkZ.Producer.VariableProducer import VariableProducer

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from DarkZ.Config.MergeSampleDict import mergeSampleDict

import copy

Data_3P1F_Run2017 = copy.deepcopy(Data_Run2017)
Data_3P1F_Run2017.name = "Data_3P1F"
Data_3P1F_Run2017.selection = LambdaFunc("x: x.nFailedLeptonsZ2[0] == 1")
Data_2P2F_Run2017 = copy.deepcopy(Data_Run2017)
Data_2P2F_Run2017.name = "Data_PredCR_2P2F"
Data_2P2F_Run2017.selection = LambdaFunc("x: x.nFailedLeptonsZ2[0] == 2")

#out_path = "ParaInput/ZXCR_m4l130To170_Nominal/2019-06-18_v1_Run2017/"
out_path = "ParaInput/ZXCR_m4l130To170_HZZ/2019-06-18_v1_Run2017/"

User                    = os.environ['USER']
nCores                  = 5
outputDir               = system.getStoragePath()+"/lucien/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = [Data_3P1F_Run2017,Data_2P2F_Run2017,WZTo3LNu,] 
justEndSequence         = False
#eventSelection          = LambdaFunc("x: x.mass4l[0] > 130.")
eventSelection          = LambdaFunc("x: x.mass4l[0] > 130. and x.massZ2[0] > 12.")

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 41.7
    for component in dataset.componentList:
        component.maxEvents = nEvents

ch_4mu_sel_str = 'abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 13 and abs(event.idL4[0]) == 13'
ch_4e_sel_str = 'abs(event.idL1[0]) == 11 and abs(event.idL2[0]) == 11 and abs(event.idL3[0]) == 11 and abs(event.idL4[0]) == 11'
ch_2e2mu_sel_str = 'abs(event.idL1[0]) == 11 and abs(event.idL2[0]) == 11 and abs(event.idL3[0]) == 13 and abs(event.idL4[0]) == 13'
ch_2mu2e_sel_str = 'abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 11 and abs(event.idL4[0]) == 11'
fs_dict = {
        "FourMu": ch_4mu_sel_str,
        "FourEl": ch_4e_sel_str,
        "TwoMuTwoEl": ch_2mu2e_sel_str,
        "TwoElTwoMu": ch_2e2mu_sel_str,
        }
pTL3_dict = {
        "0-10": "event.pTL3[0] < 10.",
        "10-20": "event.pTL3[0] > 10. and event.pTL3[0] < 20.",
        "20-30": "event.pTL3[0] > 20. and event.pTL3[0] < 30.",
        "30-45": "event.pTL3[0] > 30. and event.pTL3[0] < 45.",
        "45-Inf": "event.pTL3[0] > 45.",
        }
pTL4_dict = {
        "0-10": "event.pTL4[0] < 10.",
        "10-20": "event.pTL4[0] > 10. and event.pTL4[0] < 20.",
        "20-30": "event.pTL4[0] > 20. and event.pTL4[0] < 30.",
        "30-45": "event.pTL4[0] > 30. and event.pTL4[0] < 45.",
        "45-Inf": "event.pTL4[0] > 45.",
        }
etaL3_dict = {
        "EB": "event.etaL3[0] < 1.4",
        "EE": "event.etaL3[0] >  1.4 and event.etaL3[0] <  2.5",
        }
etaL4_dict = {
        "EB": "event.etaL4[0] < 1.4",
        "EE": "event.etaL4[0] >  1.4 and event.etaL4[0] <  2.5",
        }
input_channel_dict      = {
        "_".join([fs_key,pTL3_key,pTL4_key,etaL3_key,etaL4_key]): LambdaFunc("event: "+" and ".join([fs,pTL3,pTL4,etaL3,etaL4]))
        for fs_key,fs in fs_dict.iteritems()
        for pTL3_key,pTL3 in pTL3_dict.iteritems()
        for pTL4_key,pTL4 in pTL4_dict.iteritems()
        for etaL3_key,etaL3 in etaL3_dict.iteritems()
        for etaL4_key,etaL4 in etaL4_dict.iteritems()
        }

sequence                = darkphoton_3p1f_sequence
yieldProducer           = ParaYieldProducer("ParaYieldProducer",systList=[],channelDict=input_channel_dict,)
sequence.add(yieldProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "StatInput.root"

endSequence = EndSequence(skipHadd=False)
