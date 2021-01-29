from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from Delphes.Dataset.ZJetsToLL_LO_MLM.MuonTreeProducer import ZJetsToLL_LO_MLM 

from Common.CSVFileProducer import CSVFileProducer,CSVFileSetting,CustomVariable 

lumi                    = 1.
nCores                  = 1
outputDir               = "/cmsuf/data/store/user/t2/users/klo/Delphes/ZJetsToLL_LO_MLM/2020-07-09/MuonTreeProducer/csv/" 
nEvents                 = -1
disableProgressBar      = False
componentList           = [ZJetsToLL_LO_MLM,]
justEndSequence         = False

slurm_job_name          = "make_csv_ZJetsToLL_MuonTreeProducer"
slurm_email             = "kin.ho.lo@cern.ch"
slurm_ntasks            = "1"
slurm_mem               = "4gb"
slurm_time              = "24:00:00"

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
        CustomVariable("x: x.Muon_TrackVx[0]","x: len(x.Muon_TrackVx) > 0"),
        CustomVariable("x: x.Muon_TrackVy[0]","x: len(x.Muon_TrackVy) > 0"),
        CustomVariable("x: x.Muon_TrackVz[0]","x: len(x.Muon_TrackVz) > 0"),
        CustomVariable("x: x.Muon_TrackOuterx[0]","x: len(x.Muon_TrackOuterx) > 0"),
        CustomVariable("x: x.Muon_TrackOutery[0]","x: len(x.Muon_TrackOutery) > 0"),
        CustomVariable("x: x.Muon_TrackOuterz[0]","x: len(x.Muon_TrackOuterz) > 0"),
        CustomVariable("x: x.Muon_TrackOutert[0]","x: len(x.Muon_TrackOutert) > 0"),
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
