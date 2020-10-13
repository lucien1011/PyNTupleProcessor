
# alphatwirl
from Core.EventReader import EventLoopRunner, MPEventLoopRunner, EventLoop
from Core.ProgressBar import ProgressBar,ProgressReport,ProgressMonitor,BProgressMonitor
from Core.Concurrently import CommunicationChannel,CommunicationChannel0

from Core.BEventBuilder import BEventBuilder

from Core.ComponentLoop import ComponentLoop
from Core.UFComponentReader import UFComponentReader

from Core.Utils.git import getGitDescribe,getGitDiff
from Core.Utils.printFunc import pyPrint

# Standard package
import imp,sys,os,time
sys.path = ['', '/home/nikmenendez/.local/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/share/overrides/python', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/CMSSW_9_4_4/python', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/CMSSW_9_4_4/lib/slc6_amd64_gcc630', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/coral/CORAL_2_3_21-fmblme4/slc6_amd64_gcc630/python', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/coral/CORAL_2_3_21-fmblme4/slc6_amd64_gcc630/lib', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/professor2/2.2.1-fmblme5/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/pyqt/4.11.4-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/sherpa/2.2.4-fmblme2/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/rivet/2.5.4/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/python-ldap/2.4.10-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-matplotlib/1.5.2-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/sip/4.17-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/llvm/4.0.1/lib64/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-sqlalchemy/1.1.4-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-lint/0.25.1-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-dxr/1.0-fmblme3/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-cx-oracle/5.2.1-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-numpy/1.12.1-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/frontier_client/2.8.20-fmblme/python/lib', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/das_client/v03.01.00-fmblme/bin', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/xrootd/4.6.1-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/yoda/1.6.7/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/lcg/root/6.10.08/lib', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/pyminuit2/0.0.1-fmblme3/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-PyYAML/3.11-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-pygithub/1.23.0-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-pip/9.0.1-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-dablooms/0.9.1-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-pippkgs_depscipy/3.0-fmblme4/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-pippkgs/6.0-fmblme/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/professor/1.4.0-fmblme3/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/dbs-client/DBS_2_1_9-fmblme/lib', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/dbs-client/DBS_2_1_9-fmblme/lib/DBSAPI', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/cvs2git/5419-fmblme/lib', '/blue/avery/nikmenendez/Wto3l/Analyzer2/UF-PyNTupleRunner/Wto3l', '/blue/avery/nikmenendez/Wto3l/Analyzer2/UF-PyNTupleRunner', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-sqlalchemy/1.1.4-fmblme/lib/python2.7/site-packages/SQLAlchemy-1.1.4-py2.7-linux-x86_64.egg', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-numpy/1.12.1-fmblme/lib/python2.7/site-packages/numpy-1.12.1-py2.7-linux-x86_64.egg', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/python/2.7.11-fmblme/lib/python27.zip', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/python/2.7.11-fmblme/lib/python2.7', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/python/2.7.11-fmblme/lib/python2.7/plat-linux2', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/python/2.7.11-fmblme/lib/python2.7/lib-tk', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/python/2.7.11-fmblme/lib/python2.7/lib-old', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/python/2.7.11-fmblme/lib/python2.7/lib-dynload', '/home/nikmenendez/.local/lib/python2.7/site-packages', '/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/python/2.7.11-fmblme/lib/python2.7/site-packages']

start_import = time.time()
from tensorflow.keras.models import model_from_json, load_model
from tensorflow.keras.backend import clear_session
end_import = time.time()

print "Time to import %f s" % (end_import-start_import)

cfgFileName             = sys.argv[1]
file                    = open( cfgFileName,'r')
cfg                     = imp.load_source( 'UFNTuple.__cfg_to_run__', cfgFileName, file)

nCores                  = cfg.nCores
componentList           = cfg.componentList
nEvents                 = cfg.nEvents
disableProgressBar      = cfg.disableProgressBar
sequence                = cfg.sequence
outputInfo              = cfg.outputInfo
endSequence             = cfg.endSequence
justEndSequence         = cfg.justEndSequence if hasattr(cfg,"justEndSequence") else False
mergeSampleDict         = cfg.mergeSampleDict if hasattr(cfg,"mergeSampleDict") else {}
mergeSigSampleDict      = cfg.mergeSigSampleDict if hasattr(cfg,"mergeSigSampleDict") else {}
verbose                 = cfg.verbose if hasattr(cfg,"verbose") else False
skipGitDetail           = cfg.skipGitDetail if hasattr(cfg,"skipGitDetail") else False
eventSelection          = cfg.eventSelection if hasattr(cfg,"eventSelection") else None
checkInputFile          = cfg.checkInputFile if hasattr(cfg,"checkInputFile") else False

if verbose:
    pyPrint("Starting")
start_time = time.time()

if not justEndSequence:
    if verbose:
        pyPrint("Initiating progress bar")
    progressBar = ProgressBar()
    
    if nCores != 1:
        progressMonitor      = BProgressMonitor(progressBar)
        communicationChannel = CommunicationChannel(nCores,progressMonitor)
    else:
        progressMonitor      = ProgressMonitor(progressBar)
        communicationChannel = CommunicationChannel0(progressMonitor)
        pass
        
    if not disableProgressBar: progressMonitor.begin()
    communicationChannel.begin()
    
    eventLoopRunner = MPEventLoopRunner(communicationChannel)
    eventBuilder    = BEventBuilder()
    componentReader = UFComponentReader(eventBuilder, eventLoopRunner, sequence, outputInfo,selection=eventSelection)
    componentLoop   = ComponentLoop(componentReader)

    if checkInputFile:
        pyPrint("\nChecking samples...\n")
        try:
            for d in componentList:
                cmps = d.makeComponents()
                for cmp in cmps:
                    eventBuilder.build(cmp)
        except ReferenceError:
            pyPrint("Paths for input files are wrong, please check")
            sys.exit()
    
    pyPrint("\nLoading samples:\n")
    for cmp in componentList:
        pyPrint(cmp.name)
    
    pyPrint("\nBegin Running\n")
    componentLoop(componentList)
    
    pyPrint("\nEnd Running\n")
    pyPrint("\nOutput saved in "+outputInfo.outputDir+"\n")
   
    if not skipGitDetail:
        gitFile        = os.path.join(outputInfo.outputDir,"gitDetails.txt")
        gitVerboseFile = os.path.join(outputInfo.outputDir,"gitVerboseDetails.txt")
        with open(gitFile,'w') as f:
            f.write(getGitDescribe())
    
        with open(gitVerboseFile,'w') as f:
            f.write(getGitDiff())
    
    if verbose:
        pyPrint("Ending progress bar")
    if not disableProgressBar: progressMonitor.end()
    communicationChannel.end()

pyPrint("\nBegin Summarising\n")
pyPrint("\nInput used: "+outputInfo.outputDir+"\n")
endSequence.run(outputInfo,componentList,mergeSampleDict=mergeSampleDict,mergeSigSampleDict=mergeSigSampleDict)

elapsed_time = time.time() - start_time
pyPrint("Time used: "+str(elapsed_time)+"s")
