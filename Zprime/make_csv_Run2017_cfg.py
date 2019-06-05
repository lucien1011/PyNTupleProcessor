from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from Zprime.Dataset.Run2017.SkimTree_Bkg_m4l70 import * 
from Zprime.Dataset.Run2017.SkimTree_Zprime_m4l70 import * 
from Zprime.Sequence.RecoSequence import * 

from Zprime.Config.MergeSampleDict import mergeSampleDict

from Common.CSVFileProducer import CSVFileProducer,CSVFileSetting 

User                    = os.environ['USER']
out_path                = "MVA/Input/2019-06-03_Run2017_m4l-cosTheta1-cosTheta2-cosThetaStar-phi-phi1/"
lumi                    = 41.4
nCores                  = 5
outputDir               = system.getStoragePath()+"/"+User+"/Higgs/Zprime/"+out_path
nEvents                 = -1
disableProgressBar      = False
componentList           = bkgSamples + sigSampleDict.values()
#componentList           = [zpToMuMu_M15,qqZZTo4L] 
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

sequence                = signal_sequence

varsToWrite             = [
                            #LambdaFunc("x: x.pTL1[0]/100."),
                            #LambdaFunc("x: x.pTL2[0]/100."),
                            #LambdaFunc("x: x.pTL3[0]/100."),
                            #LambdaFunc("x: x.pTL4[0]/100."),
                            #LambdaFunc("x: x.etaL1[0]"),
                            #LambdaFunc("x: x.etaL2[0]"),
                            #LambdaFunc("x: x.etaL3[0]"),
                            #LambdaFunc("x: x.etaL4[0]"),
                            #LambdaFunc("x: x.phiL1[0]"),
                            #LambdaFunc("x: x.phiL2[0]"),
                            #LambdaFunc("x: x.phiL3[0]"),
                            #LambdaFunc("x: x.phiL4[0]"),
                            LambdaFunc("x: (x.mass4l[0]-80.)/20."),
                            #LambdaFunc("x: x.massZ1[0]"),
                            #LambdaFunc("x: x.massZ2[0]"),
                            LambdaFunc("x: x.cosTheta1"),
                            LambdaFunc("x: x.cosTheta2"),
                            LambdaFunc("x: x.cosThetaStar"),
                            LambdaFunc("x: x.phi"),
                            LambdaFunc("x: x.phi1"),
                            #cosTheta1, cosTheta2, cosThetaStar, Phi, Phi1, diMuon2_pt, diMuon2_eta, diMuon12_delta_eta, diMuon12_delta_phi, diMuon12_delta_R
                            ]
csvFileSetting          = CSVFileSetting("csv",["input.csv","w"])
csvFileProducer         = CSVFileProducer("CSVFileProducer",varsToWrite,csvFileSetting)
sequence.add(csvFileProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "TrainingInput.root"

endSequence = EndSequence(skipHadd=justEndSequence)
