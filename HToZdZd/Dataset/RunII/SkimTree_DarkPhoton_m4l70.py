import HToZdZd.Dataset.Run2016.SkimTree_DarkPhoton_m4l70 as sample2016
import HToZdZd.Dataset.Run2017.SkimTree_DarkPhoton_m4l70 as sample2017
import HToZdZd.Dataset.Run2018.SkimTree_DarkPhoton_m4l70 as sample2018
import HToZdZd.Dataset.Run2016.SkimTree_RareBkg_m4l70 as rareBkgSample2016
import HToZdZd.Dataset.Run2017.SkimTree_RareBkg_m4l70 as rareBkgSample2017
import HToZdZd.Dataset.Run2018.SkimTree_RareBkg_m4l70 as rareBkgSample2018
import HToZdZd.Dataset.Run2016.SkimTree_DarkPhoton_m4l70_HZdZd as sigSample2016
import HToZdZd.Dataset.Run2017.SkimTree_DarkPhoton_m4l70_HZdZd as sigSample2017
import HToZdZd.Dataset.Run2018.SkimTree_DarkPhoton_m4l70_HZdZd as sigSample2018

for sample in sample2016.bkgSamples+rareBkgSample2016.rareBkgSamples+sigSample2016.sigSamples :
    sample.name += "_Run2016"
    sample.lumi = 35.9
for sample in sample2017.bkgSamples+rareBkgSample2017.rareBkgSamples+sigSample2017.sigSamples :
    sample.name += "_Run2017"
    sample.lumi = 41.4
for sample in sample2018.bkgSamples+rareBkgSample2018.rareBkgSamples+sigSample2018.sigSamples :
    sample.name += "_Run2018"
    sample.lumi = 59.7

bkgSamples = sample2016.bkgSamples + sample2017.bkgSamples + sample2018.bkgSamples

rareBkgSamples = rareBkgSample2016.rareBkgSamples + rareBkgSample2017.rareBkgSamples + rareBkgSample2018.rareBkgSamples

dataSamples = [sample2016.data2016,sample2017.data2017,sample2018.data2018,]

sigSamples = sigSample2016.sigSamples + sigSample2017.sigSamples + sigSample2018.sigSamples 
