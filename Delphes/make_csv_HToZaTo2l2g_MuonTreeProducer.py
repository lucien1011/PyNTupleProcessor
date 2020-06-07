from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from Delphes.Dataset.HToZaTo2l2g.MuonTreeProducer import * 

from Common.CSVFileProducer import CSVFileProducer,CSVFileSetting 

lumi                    = 1.
nCores                  = 1
outputDir               = "/Users/lucien/CMS/HEP-ML-Tools/Delphes/Data/2020-06-07/" 
nEvents                 = -1
disableProgressBar      = False
componentList           = [HToZaTo2l2g_M1,]
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

sequence                = signal_sequence

varsToWrite             = [
                            LambdaFunc("x: x.Muon_Pt[0]"),
                            LambdaFunc("x: x.Muon_GenPt[0]"),
                            ]
csvFileSetting          = CSVFileSetting("csv",["input.csv","w"])
csvFileProducer         = CSVFileProducer("CSVFileProducer",varsToWrite,csvFileSetting)
sequence.add(csvFileProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "TrainingInput.root"

endSequence = EndSequence(skipHadd=justEndSequence)
