from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from CSC.Dataset.SingleMuon_Run2017A_ZMu_v2 import SingleMuon_Run2017A_ZMu_v2

from Common.CSVFileProducer import CSVFileProducer,CSVFileSetting,CustomVariable 

lumi                    = 1.
nCores                  = 1
outputDir               = "/Users/lucien/CMS/HEP-ML-Tools/CMS_MuonReco/Data/2020-06-12/" 
nEvents                 = -1
disableProgressBar      = False
componentList           = [SingleMuon_Run2017A_ZMu_v2,]
justEndSequence         = False

sequence                = MuonSequence 

varsToWrite             = [
        CustomVariable("x: x.StandAloneMuons.pt","x: len(x.Muon_Pt) > 0"),
        ]
csvFileSetting          = CSVFileSetting("csv",["input.csv","w"])
csvFileProducer         = CSVFileProducer("CSVFileProducer",varsToWrite,csvFileSetting,lengthFunc=LambdaFunc("x: len(x.standAloneMuons)"),)
sequence.add(csvFileProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "TrainingInput.root"

endSequence = EndSequence(skipHadd=justEndSequence)
