from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from CSC.Dataset.SingleMuon_Run2017 import sampleDict
from CSC.Producer.SegmentProducer import n_channel
from CSC.Sequence.RecoSequence import MuonSequence

from Common.CSVFileProducer import CSVFileProducer,CSVFileSetting,CustomVariable 

# _____________________________________________________________________________ ||
lumi                    = 1.
nCores                  = 4
outputDir               = "/cmsuf/data/store/user/t2/users/klo/HEP-ML-Tools/CMS_MuonReco/Data/2020-06-17_FindSegment_Run2017ABCD/" 
nEvents                 = -1
disableProgressBar      = False
componentList           = [c for c in sampleDict.values()]
justEndSequence         = False
sequence                = MuonSequence 

slurm_job_name          = "make_csv_hpg_FindSegment"
slurm_email             = "kin.ho.lo@cern.ch"
slurm_ntasks            = "1"
slurm_mem               = "4gb"
slurm_time              = "24:00:00"

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
