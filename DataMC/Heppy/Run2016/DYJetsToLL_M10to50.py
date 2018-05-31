from DataMC.Heppy.Run2016.common import * 

sampleName  = "DYJetsToLL_M10to50"
dir_path    = bkg_dir+sampleName+".root"
inUFTier2   = True
treeName    = "tree"

cmpList = ComponentList(
        [Component(sampleName,dir_path,treeName,inUFTier2)]
        )

DYJetsToLL_M10to50 = Dataset(
        "DYJetsToLL_M10to50",
        cmpList,
        xs                  = 18610. #pb,
        )
DYJetsToLL_M10to50.setSumWeight("/raid/raid7/lucien/SUSY/RA5/SumGenWeight/NanoAOD_InclusiveSelection_v1/Run2016/DYJetsToLL_M10to50/EventWeight.root")
