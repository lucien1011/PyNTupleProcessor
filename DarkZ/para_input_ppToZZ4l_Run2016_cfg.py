from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from DarkZ.Dataset.Run2016.SkimTree_DarkPhoton_m4l70 import * 
from DarkZ.Dataset.Run2016.SkimTree_DarkPhoton_m4l70_ppZZd4l import * 
#from DarkZ.Dataset.Run2017.SignalMC import * 

from DarkZ.Sequence.RecoSequence import * 

from DarkZ.StatTools.ParaYieldProducer import ParaYieldProducer
from DarkZ.StatTools.Syst import Syst
from DarkZ.Producer.VariableProducer import VariableProducer

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule
from Plotter.Plot import Plot

from DarkZ.Config.MergeSampleDict import mergeSampleDict

#out_path = "ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-05-09_DarkPhotonSR_mZ2-35_Norm_qqZZXs0p04pb/"
#out_path = "ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-05-09_m4lSR-m4lSB_HZZd-ppZZd/"
#out_path = "ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-05-15_m4lSR-m4lSB_HZZd-ppZZd/"
out_path = "ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-05-23_m4lSR-m4lSB_ppZZd/"

syst_list = [
        Syst("FRUniIso",LambdaFunc("x: x.weight_FRUniIso")),
        Syst("FRAsymIso",LambdaFunc("x: x.weight_FRAsymIso")),
        ]


User                    = os.environ['USER']
nCores                  = 5
outputDir               = system.getStoragePath()+"/lucien/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
#componentList           = bkgSamples + sigSamples + [data2016] + ppZZdSamples
componentList           = ppZZdSamples
justEndSequence         = False
skipGitDetail           = True

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 136.1
    for component in dataset.componentList:
        component.maxEvents = nEvents

mu_ch_sel_str = 'abs(event.idL3[0]) == 13 and abs(event.idL4[0]) == 13'
el_ch_sel_str = 'abs(event.idL3[0]) == 11 and abs(event.idL4[0]) == 11'
higgsSR_sel_str = 'event.mass4l[0] > 118. and event.mass4l[0] < 130.'
higgsSB_sel_str = 'not (event.mass4l[0] > 118. and event.mass4l[0] < 130.) and event.mass4l[0] > 100. and event.mass4l[0] < 170.'
higgsLowSB_sel_str = 'event.mass4l[0] > 100. and event.mass4l[0] < 118.'
higgsHighSB_sel_str = 'event.mass4l[0] > 130. and event.mass4l[0] < 170.'
input_channel_dict      = {
        "2mu_HiggsSR": LambdaFunc('event: '+' and '.join([mu_ch_sel_str,higgsSR_sel_str])),
        "2e_HiggsSR": LambdaFunc('event: '+' and '.join([el_ch_sel_str,higgsSR_sel_str])),
        
        #"2mu_HiggsSB": LambdaFunc('event: '+' and '.join([mu_ch_sel_str,higgsSB_sel_str])),
        #"2e_HiggsSB": LambdaFunc('event: '+' and '.join([el_ch_sel_str,higgsSB_sel_str])),
        
        "2mu_HiggsLowSB": LambdaFunc('event: '+' and '.join([mu_ch_sel_str,higgsLowSB_sel_str])),
        "2e_HiggsLowSB": LambdaFunc('event: '+' and '.join([el_ch_sel_str,higgsLowSB_sel_str])),
        
        "2e_HiggsHighSB": LambdaFunc('event: '+' and '.join([el_ch_sel_str,higgsHighSB_sel_str])),
        "2mu_HiggsHighSB": LambdaFunc('event: '+' and '.join([mu_ch_sel_str,higgsHighSB_sel_str])),
        }

#sequence                = darkphoton_signal_sequence
sequence                = darkphoton_fullm4l_sequence
yieldProducer           = ParaYieldProducer("ParaYieldProducer",systList=syst_list,channelDict=input_channel_dict,)

sequence.add(yieldProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "StatInput.root"

endSequence = EndSequence(skipHadd=False)
