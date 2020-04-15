from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from Zprime.Dataset.Run2017.SkimTree_Bkg_m4l70 import * 
from Zprime.Dataset.Run2017.SkimTree_Zprime_m4l70 import * 
from Zprime.Sequence.RecoSequence import * 
from Zprime.Producer.ZCandProducer import ZCandProducer

from Zprime.Config.MergeSampleDict import mergeSampleDict

from Common.CSVFileProducer import CSVFileProducer,CSVFileSetting 

User                    = os.environ['USER']
#out_path                = "MVA/Input/2019-06-10_Run2017_m4l-mZ1-mZ2-cosTheta1-cosTheta2-cosThetaStar-phi-phi1/"
out_path                = "ZCand_Classification/2020-04-15_Run2017/"
lumi                    = 41.4
nCores                  = 5
outputDir               = system.getStoragePath()+"/"+User+"/Higgs/Zprime/"+out_path
nEvents                 = -1
disableProgressBar      = False
#componentList           = sigSampleDict.values() 
componentList           = [sigSampleDict[15],]
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

sequence                = signal_sequence
zcandProducer           = ZCandProducer("ZCandProducer")

sequence.add(zcandProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "TrainingInput.root"

endSequence = EndSequence(skipHadd=justEndSequence)
