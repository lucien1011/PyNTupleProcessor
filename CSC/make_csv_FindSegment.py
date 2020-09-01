from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from CSC.Dataset.SingleMuon_Run2017A_ZMu_v2 import SingleMuon_Run2017A_ZMu_v2
from CSC.Producer.SegmentProducer import n_channel
from CSC.Sequence.RecoSequence import MuonSequence

from Common.CSVFileProducer import CSVFileProducer,CSVFileSetting,CustomVariable 

# _____________________________________________________________________________ ||
lumi                    = 1.
nCores                  = 1
outputDir               = "/Users/lucien/CMS/HEP-ML-Tools/CMS_MuonReco/Data/2020-06-16_FindSegment/" 
nEvents                 = -1
disableProgressBar      = False
componentList           = [SingleMuon_Run2017A_ZMu_v2,]
justEndSequence         = False
sequence                = MuonSequence 

# _____________________________________________________________________________ ||
segmentVarsToWrite         = []
for i in range(n_channel):
    segmentVarsToWrite.extend([
        CustomVariable("x: int(x.segment_localX[%s])"%i,),
        ])
segmentCSVFileSetting   = CSVFileSetting("segment_localX_csv",["segment_localX.csv","w"])
localXCSVFileProducer   = CSVFileProducer("CSVFileProducer",
        segmentVarsToWrite,
        segmentCSVFileSetting,
        )
sequence.add(localXCSVFileProducer)

# _____________________________________________________________________________ ||
segmentVarsToWrite         = []
for i in range(n_channel):
    segmentVarsToWrite.extend([
        CustomVariable("x: int(x.segment_localY[%s])"%i,),
        ])
segmentCSVFileSetting   = CSVFileSetting("segment_localY_csv",["segment_localY.csv","w"])
localXCSVFileProducer   = CSVFileProducer("CSVFileProducer",
        segmentVarsToWrite,
        segmentCSVFileSetting,
        )
sequence.add(localXCSVFileProducer)

# _____________________________________________________________________________ ||
outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "TrainingInput.root"

# _____________________________________________________________________________ ||
endSequence = EndSequence(skipHadd=justEndSequence)
