from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from CSC.Dataset.SingleMuon_Run2017A_ZMu_v2 import SingleMuon_Run2017A_ZMu_v2
from CSC.Producer.StandAloneMuonProducer import n_max_segment
from CSC.Sequence.RecoSequence import MuonSequence

from Common.CSVFileProducer import CSVFileProducer,CSVFileSetting,CustomVariable 

# _____________________________________________________________________________ ||
lumi                    = 1.
nCores                  = 1
outputDir               = "/Users/lucien/CMS/HEP-ML-Tools/CMS_MuonReco/Data/2020-06-14/" 
nEvents                 = -1
disableProgressBar      = False
componentList           = [SingleMuon_Run2017A_ZMu_v2,]
justEndSequence         = False
sequence                = MuonSequence 

# _____________________________________________________________________________ ||
muonVarsToWrite         = [
        CustomVariable("x: x.pt"),
        CustomVariable("x: x.eta"),
        CustomVariable("x: x.phi"),
        CustomVariable("x: x.charge"),
        ]
muonCSVFileSetting      = CSVFileSetting("muon_csv",["muon.csv","w"])
muonCSVFileProducer     = CSVFileProducer("CSVFileProducer",
        muonVarsToWrite,
        muonCSVFileSetting,
        objectFunc=LambdaFunc("x: x.standAloneMuons"),
        globalSelFunc=LambdaFunc("x: x.numberOfSegments > 4"),
        )
sequence.add(muonCSVFileProducer)

# _____________________________________________________________________________ ||
segmentVarsToWrite         = []
for i in range(n_max_segment):
    segmentVarsToWrite.extend([
        CustomVariable("x: int(x.segments_hash[%s])"%i,),
        ])
segmentCSVFileSetting   = CSVFileSetting("segment_hash_csv",["segment_hash.csv","w"])
hashCSVFileProducer     = CSVFileProducer("CSVFileProducer",
        segmentVarsToWrite,
        segmentCSVFileSetting,
        objectFunc=LambdaFunc("x: x.standAloneMuons"),
        globalSelFunc=LambdaFunc("x: x.numberOfSegments > 4"),
        )
sequence.add(hashCSVFileProducer)

# _____________________________________________________________________________ ||
segmentVarsToWrite         = []
for i in range(n_max_segment):
    segmentVarsToWrite.extend([
        CustomVariable("x: int(x.segments_localX[%s])"%i,),
        ])
segmentCSVFileSetting   = CSVFileSetting("segment_localX_csv",["segment_localX.csv","w"])
localXCSVFileProducer   = CSVFileProducer("CSVFileProducer",
        segmentVarsToWrite,
        segmentCSVFileSetting,
        objectFunc=LambdaFunc("x: x.standAloneMuons"),
        globalSelFunc=LambdaFunc("x: x.numberOfSegments > 4"),
        )
sequence.add(localXCSVFileProducer)

# _____________________________________________________________________________ ||
segmentVarsToWrite         = []
for i in range(n_max_segment):
    segmentVarsToWrite.extend([
        CustomVariable("x: int(x.segments_localY[%s])"%i,),
        ])
segmentCSVFileSetting   = CSVFileSetting("segment_localY_csv",["segment_localY.csv","w"])
localYCSVFileProducer     = CSVFileProducer("CSVFileProducer",
        segmentVarsToWrite,
        segmentCSVFileSetting,
        objectFunc=LambdaFunc("x: x.standAloneMuons"),
        globalSelFunc=LambdaFunc("x: x.numberOfSegments > 4"),
        )
sequence.add(localYCSVFileProducer)

# _____________________________________________________________________________ ||
outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "TrainingInput.root"

# _____________________________________________________________________________ ||
endSequence = EndSequence(skipHadd=justEndSequence)
