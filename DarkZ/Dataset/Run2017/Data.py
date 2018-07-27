from Core.ComponentList import *
from Core.Dataset import Dataset

inUFTier2       = False

# ____________________________________________________________________________________________________________________________________________ ||
# ggH
data2017_cmpList = ComponentList(
        [ 
            Component("Data","/raid/raid9/ahmad/RUN2_Analyzer/v2/CMSSW_8_0_26_patch1/src/liteUFHZZ4LAnalyzer/Ntuples_Input/2017/SingleDoubleMuon_Run2017-17Nov2017-v1_NoDuplicates.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

data2017 = Dataset(
        "Data2017",
        data2017_cmpList,
        isMC                = False,
        )
