from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from HToZdZd.Dataset.RunII.SkimTree_DarkPhoton_m4l70 import * 
from HToZdZd.Sequence.RecoSequence import * 

from DarkZ.StatTools.ParaYieldProducer import ParaYieldProducer # Stealing from DarkZ
from DarkZ.StatTools.Syst import Syst # Stealing from DarkZ

from HToZdZd.Config.MergeSampleDict_RunII import *

import os

User                    = os.environ['USER']
out_path                = "DarkPhotonSR/StatInput/2019-08-21_136p1_RunII_RatioCut0p05/"
lumi                    = 136.1
nCores                  = 5
outputDir               = system.getStoragePath()+User+"/Higgs/HToZdZd/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + sigSamples  
#componentList           = dataSamples  
justEndSequence         = False
eventSelection          = LambdaFunc("x: (x.massZ1[0]-x.massZ2[0])/(x.massZ1[0]+x.massZ2[0]) < 0.05") 

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

statProducer            = ParaYieldProducer("ParaYieldProducer",

        systList        = [],
        channelDict     = {
                            "MuMu": LambdaFunc('x: abs(x.idL1[0]) == 13 and abs(x.idL2[0]) == 13 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13'),
                            "ElEl": LambdaFunc('x: abs(x.idL1[0]) == 11 and abs(x.idL2[0]) == 11 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11'),
                            "ElMu": LambdaFunc('x: abs(x.idL1[0]) == 11 and abs(x.idL2[0]) == 11 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13'),
                            "MuEl": LambdaFunc('x: abs(x.idL1[0]) == 13 and abs(x.idL2[0]) == 13 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11'),
                            "Mu": LambdaFunc('x: abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13'),
                            "El": LambdaFunc('x: abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11'),
                        },
        binning         = [8000,0.,80.], 
        )

sequence                = darkphoton_signal_unblind_sequence
sequence.add(statProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "StatInput.root"

endSequence = EndSequence(skipHadd=justEndSequence,haddDataSamples=True)
