from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc

from HToZdZd.Dataset.Run2017.SkimTree_DarkPhoton_m4l70 import * 
from HToZdZd.Dataset.Run2017.SkimTree_RareBkg_m4l70 import * 
from HToZdZd.Dataset.Run2017.SkimTree_DarkPhoton_m4l70_HZdZd import * 
from HToZdZd.Sequence.RecoSequence import * 

from HToZdZd.StatTools.StatInputProducer import StatInputProducer # Stealing from DarkZ
from DarkZ.StatTools.Syst import Syst # Stealing from DarkZ

from HToZdZd.Config.MergeSampleDict import *

import os

User                    = os.environ['USER']
#out_path                = "DarkPhotonSR/StatInput/2019-12-06_SR2D_Run2017/"
out_path                = "DarkPhotonSR/StatInput/2020-02-29_SR2D_Run2017/"
#out_path                = "DarkPhotonSR/StatInput/2020-02-29_SR2D_Run2017_OptimiseWindow/"
lumi                    = 41.7
nCores                  = 5
outputDir               = system.getStoragePath()+User+"/Higgs/HToZdZd/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + rareBkgSamples + [data2017,] + sigSamples 
componentList           = rareBkgSamples 
justEndSequence         = False
skipHadd                = False

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

statProducer            = StatInputProducer("StatInputProducer",
        systList        = [],
        channelDict     = {
                            "MuMu": BaseObject(
                                        "MuMu",
                                        histKey = "MuMu",
                                        setting = ["TH2D","MuMu","",800,0.,80.,800,0.,80.,],
                                        selFunc = LambdaFunc('x: abs(x.idL1[0]) == 13 and abs(x.idL2[0]) == 13 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13'),
                                        fillFunc = LambdaFunc('x: [x.massZ1[0],x.massZ2[0],x.weight,]'),
                                        ),
                            "ElEl": BaseObject(
                                        "ElEl",
                                        histKey = "ElEl",
                                        setting = ["TH2D","ElEl","",800,0.,80.,800,0.,80.,],
                                        selFunc = LambdaFunc('x: abs(x.idL1[0]) == 11 and abs(x.idL2[0]) == 11 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11'),
                                        fillFunc = LambdaFunc('x: [x.massZ1[0],x.massZ2[0],x.weight,]'),
                                        ),
                            "ElMu": BaseObject(
                                        "ElMu",
                                        histKey = "ElMu",
                                        setting = ["TH2D","ElMu","",800,0.,80.,800,0.,80.,],
                                        selFunc = LambdaFunc('x: abs(x.idL1[0]) == 11 and abs(x.idL2[0]) == 11 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13'),
                                        fillFunc = LambdaFunc('x: [x.massZ1[0],x.massZ2[0],x.weight,]'),
                                        ),
                            "MuEl": BaseObject(
                                        "MuEl",
                                        histKey = "MuEl",
                                        setting = ["TH2D","MuEl","",800,0.,80.,800,0.,80.,],
                                        selFunc = LambdaFunc('x: abs(x.idL1[0]) == 13 and abs(x.idL2[0]) == 13 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11'),
                                        fillFunc = LambdaFunc('x: [x.massZ1[0],x.massZ2[0],x.weight,]'),
                                        ),
                            "MuEl-ElMu": BaseObject(
                                        "MuEl-ElMu",
                                        histKey = "MuEl-ElMu",
                                        setting = ["TH2D","MuEl-ElMu","",800,0.,80.,800,0.,80.,],
                                        selFunc = LambdaFunc('x: (abs(x.idL1[0]) == 13 and abs(x.idL2[0]) == 13 and abs(x.idL3[0]) == 11 and abs(x.idL4[0]) == 11) or (abs(x.idL1[0]) == 11 and abs(x.idL2[0]) == 11 and abs(x.idL3[0]) == 13 and abs(x.idL4[0]) == 13)'),
                                        fillFunc = LambdaFunc('x: [x.massZ1[0],x.massZ2[0],x.weight,]'),
                                        ),
                            },
        )

sequence                = darkphoton_signal_unblind_sequence
sequence.add(statProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "StatInput.root"

endSequence = EndSequence(skipHadd=skipHadd,haddDataSamples=True)
