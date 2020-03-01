import DarkZ.Dataset.Run2016.SkimTree_DarkPhoton_m4l70 as sample2016
import DarkZ.Dataset.Run2016.SkimTree_DarkPhoton_m4l70_HZZd as sampleSig2016
import DarkZ.Dataset.Run2017.SkimTree_DarkPhoton_m4l70 as sample2017
import DarkZ.Dataset.Run2017.SkimTree_DarkPhoton_m4l70_HZZd as sampleSig2017
import DarkZ.Dataset.Run2018.SkimTree_DarkPhoton_m4l70 as sample2018
import DarkZ.Dataset.Run2018.SkimTree_DarkPhoton_m4l70_HZZd as sampleSig2018
import DarkZ.Dataset.Run2016.SkimTree_DarkPhoton_m4l70_ppZZd4l as sample_ppZZd 

for sample in sample2016.bkgSamples+sampleSig2016.sigSamples:
    sample.name += "_Run2016"
    sample.lumi = 35.9
for sample in sample2017.bkgSamples+sampleSig2017.sigSamples:
    sample.name += "_Run2017"
    sample.lumi = 41.4
for sample in sample2018.bkgSamples+sampleSig2018.sigSamples:
    sample.name += "_Run2018"
    sample.lumi = 59.7

bkgSamples = sample2016.bkgSamples + sample2017.bkgSamples + sample2018.bkgSamples

sigSamples = sampleSig2016.sigSamples + sampleSig2017.sigSamples + sampleSig2018.sigSamples

ppZZdSamples = sample_ppZZd.ppZZdSamples
for sample in ppZZdSamples: sample.lumi = 136.1

dataSamples = [sample2016.data2016,sample2017.data2017,sample2018.data2018,]
