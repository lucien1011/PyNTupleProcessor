#!/bin/bash

baseDir=/raid/raid7//lucien/Higgs/DarkZ/ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-09-02_m4lSR-m4lSB_HZZd-ppZZd_Run
baseZXDir=/raid/raid7//lucien/Higgs/DarkZ/ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-08-14_m4lSR-m4lSB_HZZd-ppZZd_Run
outputDir=/raid/raid7//lucien/Higgs/DarkZ/ParaInput/DarkPhotonSelection_m4l100To170_Nominal/2019-09-02_m4lSR-m4lSB_HZZd-ppZZd_RunII/

for s in Data Higgs qqZZ ggZZ HZZd_M4 HZZd_M7 HZZd_M10 HZZd_M15 HZZd_M20 HZZd_M25 HZZd_M30 ppZZd4l_M5 ppZZd4l_M15 ppZZd4l_M30 ZPlusX;
do
    mkdir ${outputDir}/${s}/
    hadd -f ${outputDir}/${s}/StatInput.root ${baseDir}2*/${s}/StatInput.root
done

hadd -f ${outputDir}/ZPlusX/ParaShape.root ${baseZXDir}2*/ZPlusX/ParaShape.root
