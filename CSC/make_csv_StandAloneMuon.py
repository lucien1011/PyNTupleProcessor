from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from CSC.Dataset.SingleMuon_Run2017A_ZMu_v2_LucienMacPro import SingleMuon_Run2017A_ZMu_v2
from CSC.Producer.StandAloneMuonProducer import n_max_segment
from CSC.Sequence.RecoSequence import MuonSequence

from Common.CSVFileProducer import CSVFileProducer,CSVFileSetting,CustomVariable 

# _____________________________________________________________________________ ||
lumi                    = 1.
nCores                  = 1
outputDir               = "/Users/lucien/CMS/HEP-ML-Tools/CMS_MuonReco/Data/2020-06-18/" 
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
for seg_var in ["globalX","globalY","endcap","chamber","station","ring",]:
    segmentVarsToWrite         = []
    for i in range(n_max_segment):
        segmentVarsToWrite.extend([
            CustomVariable("x: int(x.segments_"+seg_var+"["+str(i)+"])",),
            ])
    segmentCSVFileSetting   = CSVFileSetting("segment_"+str(seg_var)+"_csv",["segment_"+str(seg_var)+".csv","w"])
    varCSVFileProducer     = CSVFileProducer("CSVFileProducer",
            segmentVarsToWrite,
            segmentCSVFileSetting,
            objectFunc=LambdaFunc("x: x.standAloneMuons"),
            globalSelFunc=LambdaFunc("x: x.numberOfSegments > 4"),
            )
    sequence.add(varCSVFileProducer)

# _____________________________________________________________________________ ||
outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "TrainingInput.root"

# _____________________________________________________________________________ ||
endSequence = EndSequence(skipHadd=justEndSequence)
