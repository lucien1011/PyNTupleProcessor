from DYJetsToLL_M10to50 import DYJetsToLL_M10to50
#from DYJetsToLL_M50 import DYJetsToLL_M50
#from DYJetsToLL_M50_LO import DYJetsToLL_M50_LO
from DYJetsToLL_M50_NLO import DYJetsToLL_M50_NLO 
#from TGJets import TGJets
from TT_Powheg import TT_Powheg
from ttWJets import ttWJets
from ttZJets import ttZJets
from WJetsToLNu import WJetsToLNu
from WWW_4f import WWW_4f
from WWZ import WWZ
from WZTo3LNu import WZTo3LNu
from WZZ import WZZ
from ZGTo2LG import ZGTo2LG
from ZZZ import ZZZ
from TToLeptons_sch import TToLeptons_sch
from T_tch import T_tch
from T_tWch import T_tWch
from TBar_tWch import TBar_tWch

from LQToBL import LQToBL_mLQ500

from SingleMuon2016B import SingleMuon2016B
from SingleMuon2016C import SingleMuon2016C
from SingleMuon2016D import SingleMuon2016D
from SingleMuon2016E import SingleMuon2016E
from SingleMuon2016F import SingleMuon2016F
from SingleMuon2016G import SingleMuon2016G
from SingleMuon2016H import SingleMuon2016H
from SingleMuon2016H2 import SingleMuon2016H2
from SingleElectron2016B1 import SingleElectron2016B1
from SingleElectron2016B2 import SingleElectron2016B2
from SingleElectron2016C import SingleElectron2016C
from SingleElectron2016D import SingleElectron2016D
from SingleElectron2016E import SingleElectron2016E
from SingleElectron2016F import SingleElectron2016F
from SingleElectron2016G import SingleElectron2016G
from SingleElectron2016H1 import SingleElectron2016H1
from SingleElectron2016H2 import SingleElectron2016H2

allMCSamples = [
    DYJetsToLL_M10to50,
#    DYJetsToLL_M50,
#    DYJetsToLL_M50_LO,
    DYJetsToLL_M50_NLO,
    #TGJets,
    TT_Powheg,
    ttWJets,
    ttZJets,
    WJetsToLNu,
    WWW_4f,
    WWZ,
    WZTo3LNu,
    WZZ,
    ZGTo2LG,
    ZZZ,
    TToLeptons_sch,
    T_tch,
    T_tWch,
    TBar_tWch,
    ]

allSigSamples = [
    LQToBL_mLQ500,
    ]

allDataSamples = [
#    SingleMuon2016B,
#    SingleMuon2016C,
#    SingleMuon2016D,
#    SingleMuon2016E,
#    SingleMuon2016F,
#    SingleMuon2016G,
#    SingleMuon2016H,
#    SingleMuon2016H2,
    SingleElectron2016B1,
    SingleElectron2016B2,
    SingleElectron2016C,
    SingleElectron2016D,
    SingleElectron2016E,
    SingleElectron2016F,
    SingleElectron2016G,
    SingleElectron2016H1,
    SingleElectron2016H2,
    ]
