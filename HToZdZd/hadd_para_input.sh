#!/bin/bash

#baseDir=/raid/raid7/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-09-06_Run
#baseZXDir=/raid/raid7/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-09-06_Run
#outputDir=/raid/raid7/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-09-06_RunII/

#baseDir=/raid/raid7/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-12-06_SR2D_Run
#baseZXDir=/raid/raid7/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-09-06_Run
#outputDir=/raid/raid7/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-12-06_SR2D_hadd_RunII/

baseDir=/raid/raid7/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-12-02_Run
baseZXDir=/raid/raid7/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-09-06_Run
outputDir=/raid/raid7/lucien/Higgs/HToZdZd/DarkPhotonSR/StatInput/2019-12-02_hadd_RunII/

#for s in Data Higgs qqZZ ggZZ HToZdZd_MZD10 HToZdZd_MZD4 HToZdZd_MZD20 HToZdZd_MZD30 HToZdZd_MZD40 HToZdZd_MZD50 HToZdZd_MZD60 ZPlusX;
#for s in HToZdZd_M10 HToZdZd_M4 HToZdZd_M20 HToZdZd_M30 HToZdZd_M40 HToZdZd_M50 HToZdZd_M60 ZPlusX;
for s in Data Higgs qqZZ ggZZ HToZdZd_M10 HToZdZd_M4 HToZdZd_M20 HToZdZd_M30 HToZdZd_M40 HToZdZd_M50 HToZdZd_M60 ZPlusX;
do
    mkdir ${outputDir}/${s}/
    hadd -f ${outputDir}/${s}/StatInput.root ${baseDir}2*/${s}/StatInput.root
done

hadd -f ${outputDir}/ZPlusX/ParaShape.root ${baseZXDir}2*/ZPlusX/ParaShape.root
