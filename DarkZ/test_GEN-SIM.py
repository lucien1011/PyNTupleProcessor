# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 

from Core.NanoAODResult.Component import Component

gen_cmp = Component(
        "/raid/raid7/lucien/Higgs/DarkZ-EvtGeneration/Log/2018-03-23/",
        "DarkZTo4l_v1",
        inUFTier2 = False,
        keyword = "",
        )
print gen_cmp.fileInfos()

nCores = 1 
outputDir = "/raid/raid7/lucien/Higgs/DarkZ-EvtGeneration/Log/2018-03-23/testEDM/"
nEvents = -1
disableProgressBar = False

sequence = Sequence()

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "test1.root"

componentList = [
        gen_cmp,
        ]

