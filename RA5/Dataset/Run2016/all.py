from DYJetsToLL_M10to50_LO import DYJetsToLL_M10to50_LO
from DYJetsToLL_M50_LO_ext import DYJetsToLL_M50_LO_ext
from TGJets import TGJets
from TTGJets import TTGJets
from TTHnobb_pow import TTHnobb_pow
from TTWToLNu_ext import TTWToLNu_ext
from TTZToLLNuNu import TTZToLLNuNu
from TTZToLLNuNu_m1to10 import TTZToLLNuNu_m1to10
from VHToNonbb import VHToNonbb
from WGToLNuG import WGToLNuG
from WJetsToLNu_LO import WJetsToLNu_LO
from WWDoubleTo2L import WWDoubleTo2L
from WZTo3LNu import WZTo3LNu
from TT_pow import TT_pow

from T1qqqqL import T1qqqqL_1000,T1qqqqL_1500
from T1tbs import T1tbs_1000,T1tbs_1500

from Data import Data_Run2016B

#from SyncMC import SyncMC,SkimSyncMC

allMCSamples = [
   DYJetsToLL_M10to50_LO,
   DYJetsToLL_M50_LO_ext,
   TGJets,
   TTGJets,
   TTHnobb_pow,
   TTWToLNu_ext,
   TTZToLLNuNu,
   TTZToLLNuNu_m1to10,
   VHToNonbb,
   WGToLNuG,
   WJetsToLNu_LO,
   WWDoubleTo2L,
   WZTo3LNu,
   TT_pow,
   ]

allSignalSamples = [
        T1qqqqL_1000,
        T1qqqqL_1500,
        T1tbs_1000,
        #T1tbs_1500,
        ]
