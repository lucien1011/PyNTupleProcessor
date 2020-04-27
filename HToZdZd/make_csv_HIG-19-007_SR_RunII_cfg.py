from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from HToZdZd.Dataset.RunII.SkimTree_DarkPhoton_m4l70 import * 
from HToZdZd.Sequence.RecoSequence import * 
from HToZdZd.Config.MergeSampleDict_RunII import *

from Common.CSVFileProducer import CSVFileProducer,CSVFileSetting 

import os,ROOT

#out_path                = "DarkPhotonSR/DataMCDistributions/2020-03-18_RunII/"
#out_path                = "DarkPhotonSR/DataMCDistributions/2020-03-19_RunII/"
#out_path                = "ML/CSV/2020-04-19_RunII/"
#out_path                = "ML/CSV/2020-04-20_RunII/"
#out_path                = "ML/CSV/2020-04-21_RunII/"
out_path                = "ML/CSV/2020-04-27_RunII/"
User                    = os.environ['USER']
nCores                  = 1
outputDir               = system.getStoragePath()+User+"/Higgs/HToZdZd/"+out_path
nEvents                 = -1
disableProgressBar      = False
#componentList           = [c for c in bkgSamples if any([key in c.name for key in ["ggH","VBF","WHplus","WHminus","ZH",]]) ]
componentList           = [c for c in bkgSamples if any([key in c.name for key in ["ggH",]]) ]
justEndSequence         = False
skipHadd                = False  

for dataset in componentList:
    for component in dataset.componentList:
        component.maxEvents = nEvents

sequence                = darkphoton_signal_unblind_sequence
varsToWrite             = [
                            LambdaFunc("x: x.pTL1[0]"),
                            LambdaFunc("x: x.pTL2[0]"),
                            LambdaFunc("x: x.pTL3[0]"),
                            LambdaFunc("x: x.pTL4[0]"),
                            LambdaFunc("x: x.etaL1[0]"),
                            LambdaFunc("x: x.etaL2[0]"),
                            LambdaFunc("x: x.etaL3[0]"),
                            LambdaFunc("x: x.etaL4[0]"),
                            LambdaFunc("x: x.phiL1[0]"),
                            LambdaFunc("x: x.phiL2[0]"),
                            LambdaFunc("x: x.phiL3[0]"),
                            LambdaFunc("x: x.phiL4[0]"),
                            LambdaFunc("x: x.phiL21"),
                            LambdaFunc("x: x.phiL31"),
                            LambdaFunc("x: x.phiL41"),
                            LambdaFunc("x: x.mass4l[0]"),
                            LambdaFunc("x: x.massZ1[0]"),
                            LambdaFunc("x: x.massZ2[0]"),
                            #LambdaFunc("x: x.cosTheta1"),
                            #LambdaFunc("x: x.cosTheta2"),
                            #LambdaFunc("x: x.cosThetaStar"),
                            #LambdaFunc("x: x.phi"),
                            #LambdaFunc("x: x.phi1"),
                            #cosTheta1, cosTheta2, cosThetaStar, Phi, Phi1, diMuon2_pt, diMuon2_eta, diMuon12_delta_eta, diMuon12_delta_phi, diMuon12_delta_R
                            ]
csvFileSetting          = CSVFileSetting("csv",["input.csv","w"])
csvFileProducer         = CSVFileProducer("CSVFileProducer",varsToWrite,csvFileSetting)
sequence.add(csvFileProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "TrainingInput.root"

endSequence = EndSequence(skipHadd=False,haddDataSamples=True,)
