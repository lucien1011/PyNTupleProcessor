from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from DarkZ.Dataset.Run2017.SkimTree_DarkPhoton_m4l70_HZZdInterpolation import * 

from DarkZ.Sequence.RecoSequence import * 

from DarkZ.StatTools.ParaYieldProducer import ParaYieldProducer
from DarkZ.Producer.VariableProducer import VariableProducer

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework

from DarkZ.Config.MergeSampleDict import mergeSampleDict

import os

out_path = "ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-12-04_m4lSR-m4lSB_HZZd_SignalInterpolation_Run2017/"

User                    = os.environ['USER']
nCores                  = 5
outputDir               = system.getStoragePath()+'/'+User+"/Higgs/DarkZ/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = sigSamples
justEndSequence         = False
skipGitDetail           = True

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 41.7
    for component in dataset.componentList:
        component.maxEvents = nEvents

mu_Z1_ch_sel_str = 'abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13'
el_Z1_ch_sel_str = 'abs(event.idL1[0]) == 11 and abs(event.idL2[0]) == 11'
mu_Z2_ch_sel_str = 'abs(event.idL3[0]) == 13 and abs(event.idL4[0]) == 13'
el_Z2_ch_sel_str = 'abs(event.idL3[0]) == 11 and abs(event.idL4[0]) == 11'
#mu_ch_sel_str = 'abs(event.idL3[0]) == 13 and abs(event.idL4[0]) == 13'
#el_ch_sel_str = 'abs(event.idL3[0]) == 11 and abs(event.idL4[0]) == 11'
higgsSR_sel_str = 'event.mass4l[0] > 118. and event.mass4l[0] < 130.'
higgsSB_sel_str = 'not (event.mass4l[0] > 118. and event.mass4l[0] < 130.) and event.mass4l[0] > 100. and event.mass4l[0] < 170.'
higgsLowSB_sel_str = 'event.mass4l[0] > 100. and event.mass4l[0] < 118.'
higgsHighSB_sel_str = 'event.mass4l[0] > 130. and event.mass4l[0] < 170.'
input_channel_dict      = {
        "MuMu_HiggsSR": LambdaFunc('event: '+' and '.join([mu_Z1_ch_sel_str,mu_Z2_ch_sel_str,higgsSR_sel_str])),
        "MuMu_HiggsLowSB": LambdaFunc('event: '+' and '.join([mu_Z1_ch_sel_str,mu_Z2_ch_sel_str,higgsLowSB_sel_str])),
        "MuMu_HiggsHighSB": LambdaFunc('event: '+' and '.join([mu_Z1_ch_sel_str,mu_Z2_ch_sel_str,higgsHighSB_sel_str])),
        "ElMu_HiggsSR": LambdaFunc('event: '+' and '.join([el_Z1_ch_sel_str,mu_Z2_ch_sel_str,higgsSR_sel_str])),
        "ElMu_HiggsLowSB": LambdaFunc('event: '+' and '.join([el_Z1_ch_sel_str,mu_Z2_ch_sel_str,higgsLowSB_sel_str])),
        "ElMu_HiggsHighSB": LambdaFunc('event: '+' and '.join([el_Z1_ch_sel_str,mu_Z2_ch_sel_str,higgsHighSB_sel_str])),
        "MuEl_HiggsSR": LambdaFunc('event: '+' and '.join([mu_Z1_ch_sel_str,el_Z2_ch_sel_str,higgsSR_sel_str])),
        "MuEl_HiggsLowSB": LambdaFunc('event: '+' and '.join([mu_Z1_ch_sel_str,el_Z2_ch_sel_str,higgsLowSB_sel_str])),
        "MuEl_HiggsHighSB": LambdaFunc('event: '+' and '.join([mu_Z1_ch_sel_str,el_Z2_ch_sel_str,higgsHighSB_sel_str])),
        "ElEl_HiggsSR": LambdaFunc('event: '+' and '.join([el_Z1_ch_sel_str,el_Z2_ch_sel_str,higgsSR_sel_str])),
        "ElEl_HiggsLowSB": LambdaFunc('event: '+' and '.join([el_Z1_ch_sel_str,el_Z2_ch_sel_str,higgsLowSB_sel_str])),
        "ElEl_HiggsHighSB": LambdaFunc('event: '+' and '.join([el_Z1_ch_sel_str,el_Z2_ch_sel_str,higgsHighSB_sel_str])),
        }

#sequence                = darkphoton_signal_sequence
sequence                = darkphoton_fullm4l_sequence
yieldProducer           = ParaYieldProducer("ParaYieldProducer",systList=[],channelDict=input_channel_dict,)

sequence.remove(darkPhotonFullm4lSkimmer)
sequence.add(sigInterpolSkimmer)
sequence.remove(resonaceSkimmer)
sequence.add(yieldProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "StatInput.root"

endSequence = EndSequence(skipHadd=False,haddDataSamples=True)
