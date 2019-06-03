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
out_path                = "DarkPhotonSR/StatInput/2019-05-28_136p1_RunII_OptimiseMassRatio/"
lumi                    = 136.1
nCores                  = 5
outputDir               = system.getStoragePath()+User+"/Higgs/HToZdZd/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + sigSamples + dataSamples  
justEndSequence         = False
eventSelection          = LambdaFunc("x: (x.massZ1[0]-x.massZ2[0])/(x.massZ1[0]+x.massZ2[0]) < 0.10") 

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

channelDict = {}
ratios = [0.01*i for i in range(1,10)]
for ratio in ratios:
    channelDict["2mu_"+str(ratio)] = LambdaFunc('x: abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13 and (x.massZ1[0]-x.massZ2[0])/(x.massZ1[0]+x.massZ2[0]) < '+str(ratio))
    channelDict["2e_"+str(ratio)] = LambdaFunc('x: abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11 and (x.massZ1[0]-x.massZ2[0])/(x.massZ1[0]+x.massZ2[0]) < '+str(ratio))

statProducer            = ParaYieldProducer("ParaYieldProducer",

        systList        = [],
        channelDict     = channelDict,
        binning         = [1000,4.,62.5], 
        )

sequence                = darkphoton_signal_unblind_sequence
sequence.add(statProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "StatInput.root"

endSequence = EndSequence(skipHadd=justEndSequence,haddDataSamples=True)
