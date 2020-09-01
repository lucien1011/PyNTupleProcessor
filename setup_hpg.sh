export PYTHONPATH=${PYTHONPATH}:${PWD}/
export PATH=${PATH}:${PWD}/bin/

export BASE_PATH=${PWD}

cd /cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/CMSSW_9_4_4/src/ 
eval `scramv1 runtime -sh`
cd -

export NTUPLERUNNER_MODE="Remote"
export NTUPLERUNNER_STORAGE=/cmsuf/data/store/user/t2/users//klo/UFNTupleRunner_Storage/
export NTUPLERUNNER_WWW="/home/${USER}/public_html/"
