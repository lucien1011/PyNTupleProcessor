from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Core.BaseObject import BaseObject
from Utils.System import system

from Zprime.Dataset.Run2017.SkimTree_Bkg_m4l70 import * 
from Zprime.Dataset.Run2017.SkimTree_Zprime_m4l70 import * 
from Zprime.Sequence.RecoSequence import * 

from Zprime.StatTools.MVAShapeProducer import MVAShapeProducer

from Zprime.Config.MergeSampleDict import mergeSampleDict

import os

out_path = "ParaInput/EXO-18-008-MVAShape/2019-06-10_MVAInput/"

User                    = os.environ['USER']
nCores                  = 5
lumi                    = 77.3
outputDir               = system.getStoragePath()+"/"+User+"/Higgs/Zprime/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + sigSampleDict.values()
justEndSequence         = False
skipGitDetail           = False

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

mu_ch_sel_str = 'abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 13 and abs(event.idL4[0]) == 13'

eventSelection          = LambdaFunc("event: "+mu_ch_sel_str)

input_channel_dict      = {
        "4mu": LambdaFunc('event: '+mu_ch_sel_str),
        }
model_dict              = {
        "M%s"%m: "/raid/raid7/lucien/AnalysisCode/ML/Zprime-ML/result/2019-06-10_Run2017_qqZZ-zpToMuMu-M%s_m4l-mZ1-mZ2-cosTheta1-cosTheta2-cosThetaStar-phi-phi1/mlp-classifier.pkl"%m for m in [5,10,15,20,30,40,50,60,70]
        }
sequence                = signal_sequence
yieldProducer           = MVAShapeProducer(
                                "MVAShapeProducer",
                                channelDict=input_channel_dict,
                                modelDict=model_dict,
                                varFunc=LambdaFunc("x: [(x.mass4l[0]-80.)/20.,x.massZ1[0]/60.,x.massZ2[0]/60.,x.cosTheta1, x.cosTheta2, x.cosThetaStar, x.phi, x.phi1,]"),
                                )
sequence.add(yieldProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "StatInput.root"

endSequence = EndSequence(skipHadd=False)
