from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from Wto3l.Dataset.Run2016.Wto3l_MC_sr import * 
from Wto3l.Dataset.Run2016.Wto3l_Data  import * 
from Wto3l.Dataset.Run2016.Wto3l_MC import *

from Wto3l.Sequence.RecoSequence import * 

from Zprime.Config.MergeSampleDict import mergeSampleDict

from Common.CSVFileProducer import CSVFileProducer,CSVFileSetting 

User                    = os.environ['USER']
#out_path                = "MVA/Input/2019-10-28_Run2016_Wmto3lZpM15-ZpdR-Zpeta-ZppT-leadingLep-ZpthirdLepdR-3LepthirdLepdR/Sig/"
#out_path                = "MVA/Input/2019-10-28_Run2016_Wmto3lZpM15-ZpdR-leadingLep/Bkg/"
#out_path                = "MVA/Input/2019-11-25_Run2016_DYJetsToLL_M50-ZpdR-Zpeta-ZppT-leadingLep-ZpthirdLepdR-3LepthirdLepdR/Mass2/"
out_path                = "MVA/Input/2019-11-25_Run2016_TTJets-ZpdR-Zpeta-ZppT-leadingLep-ZpthirdLepdR-3LepthirdLepdR/Mass1/"
lumi                    = 35.9
nCores                  = 1
outputDir               = system.getStoragePath()+"/"+User+"/Higgs/Zprime/"+out_path
nEvents                 = -1
disableProgressBar      = False
#componentList           = bkgSamples + sigSampleDict.values()
#componentList           = [WmTo3munu_ZpM15] 
#componentList           = [DYJetsToLL_M50]
componentList           = [TTJets]
justEndSequence         = False

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

sequence                = Wto3l_sequence

varsToWrite             = [
                            #LambdaFunc("x: x.Zp_pt/100."),
                            #LambdaFunc("x: x.notZp_pt/100."),
                            #LambdaFunc("x: x.Zp_eta/3."),
                            #LambdaFunc("x: x.notZp_eta/3."),
                            #LambdaFunc("x: x.Zp_lep_deltaR/4.5"),
                            #LambdaFunc("x: x.notZp_lep_deltaR/4.5"),
                            #LambdaFunc("x: x.Lep_leading_fromZp.Pt()/80."),
                            #LambdaFunc("x: x.Lep_leading_notZp.Pt()/80."),
                            #LambdaFunc("x: x.Zp_lepnotfromZp_dR/4.5"),
                            #LambdaFunc("x: x.notZp_otherlep_dR/4.5"),
                            #LambdaFunc("x: x.totalLep_thirdLep_Zp_dR/4.5"),
                            #LambdaFunc("x: x.totalLep_thirdLep_notZp_dR/4.5"),
                            LambdaFunc("x: x.mass1_pt/100."),
                            #LambdaFunc("x: x.mass2_pt/100."),
                            LambdaFunc("x: x.mass1_eta/3."),
                            #LambdaFunc("x: x.mass2_eta/3."),
                            LambdaFunc("x: x.Z1_lep_deltaR/4.5"),
                            #LambdaFunc("x: x.Z2_lep_deltaR/4.5"),
                            LambdaFunc("x: x.Lep_leading_fromM1.Pt()/80."),
                            #LambdaFunc("x: x.Lep_leading_fromM2.Pt()/80."),
                            LambdaFunc("x: x.M1_lepnotfromM1_dR/4.5"),
                            #LambdaFunc("x: x.M2_lepnotfromM2_dR/4.5"),
                            LambdaFunc("x: x.totalLep_thirdLep_M1_dR/4.5"),
                            #LambdaFunc("x: x.totalLep_thirdLep_M2_dR/4.5"),
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
                            #LambdaFunc("x: (x.mass4l[0]-80.)/20."),
                            #LambdaFunc("x: x.massZ1[0]/60."),
                            #LambdaFunc("x: x.massZ2[0]/60."),
                            #LambdaFunc("x: x.cosTheta1"),
                            #LambdaFunc("x: x.cosTheta2"),
                            #LambdaFunc("x: x.cosThetaStar"),
                            #LambdaFunc("x: x.phi"),
                            #LambdaFunc("x: x.phi1"),
                            #cosTheta1, cosTheta2, cosThetaStar, Phi, Phi1, diMuon2_pt, diMuon2_eta, diMuon12_delta_eta, diMuon12_delta_phi, diMuon12_delta_R
                            ]
csvFileSetting          = CSVFileSetting("csv",["input.csv","w"])
csvFileProducer         = CSVFileProducer("CSVFileProducer",varsToWrite,csvFileSetting)
sequence.add(csvFileProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "TrainingInput.root"

endSequence = EndSequence(skipHadd=justEndSequence)
