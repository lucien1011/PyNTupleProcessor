#!/bin/bash

for f in $(ls *.txt) ; do  rf=$(echo ${f} | sed -e "s/.txt/.root/g") ; echo ${rf} ; xrdcp root://cmseos.fnal.gov//store/user/lpcljm/yiting/2017/Feb_addNumCounter/nominal/${rf} /raid/raid7/lucien/LJMet/B2G/Step1NTuple/ ; done
