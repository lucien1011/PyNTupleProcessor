from Core.ComponentList import *
from Core.Dataset import Dataset

dir_prefix	= "root://cmseos.fnal.gov//store/user/lpcljm/2018/LJMet94X_1lepTT_101118newB_step1hadds/nominal/"
treeName	= "ljmet"

# ____________________________________________________________________________________________________________________________________________ ||
# TTToSemiLep_Mtt1000ToInf
TTToSemiLep_Mtt1000ToInf_cmpList = ComponentList(
        [
            Component("ZPlusX",
                dir_prefix+"TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt1000toInf_hadd.root",
				treeName,
				False,
				)
        ]
        )
TTToSemiLep_Mtt1000ToInf = Dataset(
        "TTToSemiLep_Mtt1000ToInf",
        TTToSemiLep_Mtt1000ToInf_cmpList,
        isMC                = True,
        xs					= 831.76*0.02474*0.405,
		sumw				= 111325048*0.02474 + 14970062*0.405,
		)

