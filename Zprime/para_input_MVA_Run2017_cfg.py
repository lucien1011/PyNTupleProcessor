from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Core.BaseObject import BaseObject
from Utils.System import system

from Zprime.Dataset.Run2017.SkimTree_Bkg_m4l70 import * 
from Zprime.Dataset.Run2017.SkimTree_Zprime_m4l70 import * 
from Zprime.Sequence.RecoSequence import * 

from Zprime.StatTools.ParaYieldProducer import ParaYieldProducer
from Zprime.Skimmer.MVASkimmer import MVASkimmer

from Zprime.Config.MergeSampleDict import mergeSampleDict

import os

#out_path = "ParaInput/EXO-18-001-Nominal/2019-06-05/"
#out_path = "ParaInput/EXO-18-001-Nominal/2019-06-06_MVAInput_mZp10/"
#out_path = "ParaInput/EXO-18-001-Nominal/2019-06-06_MVAInput_mZp30/"
out_path = "ParaInput/EXO-18-001-Nominal/2019-06-10_MVAInput_mZp40/"

User                    = os.environ['USER']
nCores                  = 5
lumi                    = 77.3
outputDir               = system.getStoragePath()+"/lucien/Higgs/Zprime/"+out_path
nEvents                 = -1
disableProgressBar      = False
#componentList           = bkgSamples
componentList           = bkgSamples + [sigSampleDict[40]]
#componentList           = [sigSampleDict[40]]
#componentList           = sigSampleDict.values()
justEndSequence         = False
skipGitDetail           = True
mvaSkim                 = True

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

mu_ch_sel_str = 'abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 13 and abs(event.idL4[0]) == 13'

input_channel_dict      = {
        "4mu": LambdaFunc('event: '+mu_ch_sel_str),
        }

sequence                = signal_sequence
yieldProducer           = ParaYieldProducer("ParaYieldProducer",channelDict=input_channel_dict,)
if mvaSkim:
    mvaSkimmer          = MVASkimmer("MVSkimmer",
                            BaseObject(
                                "MVASetting",
                                modelPath="/raid/raid7/lucien/AnalysisCode/ML/Zprime-ML/result/2019-06-04_Run2017_qqZZ-zpToMuMu-M40_m4l-cosTheta1-cosTheta2-cosThetaStar-phi-phi1/mlp-classifier.pkl",
                                threshold=0.45,
                                varFunc=LambdaFunc("x: [(x.mass4l[0]-80.)/20.,x.cosTheta1, x.cosTheta2, x.cosThetaStar, x.phi, x.phi1,]"),
                                ),
                            )
    sequence.add(mvaSkimmer)
sequence.add(yieldProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "StatInput.root"

endSequence = EndSequence(skipHadd=justEndSequence)
