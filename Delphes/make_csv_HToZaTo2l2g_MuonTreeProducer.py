from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from Delphes.Dataset.HToZaTo2l2g.MuonTreeProducer import * 

from Common.CSVFileProducer import CSVFileProducer,CSVFileSetting,CustomVariable 

lumi                    = 1.
nCores                  = 1
outputDir               = "/Users/lucien/CMS/HEP-ML-Tools/Delphes/Data/2020-06-08/" 
nEvents                 = -1
disableProgressBar      = False
componentList           = [HToZaTo2l2g_M1,]
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

sequence                = Sequence() 

varsToWrite             = [
        CustomVariable("x: x.Muon_Pt[0]","x: len(x.Muon_Pt) > 0"),
        CustomVariable("x: x.Muon_Eta[0]","x: len(x.Muon_Pt) > 0"),
        CustomVariable("x: x.Muon_Phi[0]","x: len(x.Muon_Pt) > 0"),
        CustomVariable("x: x.Muon_T[0]","x: len(x.Muon_T) > 0"),
        CustomVariable("x: x.Muon_IsolationVar[0]","x: len(x.Muon_IsolationVar) > 0"),
        CustomVariable("x: x.Muon_SumPtCharged[0]","x: len(x.Muon_SumPtCharged) > 0"),
        CustomVariable("x: x.Muon_SumPtNeutral[0]","x: len(x.Muon_SumPtNeutral) > 0"),
        CustomVariable("x: x.Muon_SumPtChargedPU[0]","x: len(x.Muon_SumPtChargedPU) > 0"),
        CustomVariable("x: x.Muon_TrackD0[0]","x: len(x.Muon_TrackD0) > 0"),
        CustomVariable("x: x.Muon_TrackDZ[0]","x: len(x.Muon_TrackDZ) > 0"),
        CustomVariable("x: x.Muon_GenPt[0]","x: len(x.Muon_GenPt) > 0"),
        CustomVariable("x: x.Muon_GenEta[0]","x: len(x.Muon_GenPt) > 0"),
        CustomVariable("x: x.Muon_GenPhi[0]","x: len(x.Muon_GenPt) > 0"),
        CustomVariable("x: x.Muon_GenCharge[0]","x: len(x.Muon_GenCharge) > 0"),
        ]
csvFileSetting          = CSVFileSetting("csv",["input.csv","w"])
csvFileProducer         = CSVFileProducer("CSVFileProducer",varsToWrite,csvFileSetting)
sequence.add(csvFileProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "TrainingInput.root"

endSequence = EndSequence(skipHadd=justEndSequence)
