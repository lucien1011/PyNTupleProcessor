from Core.Utils.git import getGitDescribe,getGitDiff
from Core.Utils.printFunc import pyPrint

# Standard package
import imp,sys,os,time

cfgFileName             = sys.argv[1]
file                    = open( cfgFileName,'r')
cfg                     = imp.load_source( 'UFNTuple.__cfg_to_run__', cfgFileName, file)
componentList           = cfg.componentList
outputInfo              = cfg.outputInfo
endSequence             = cfg.endSequence
mergeSampleDict         = cfg.mergeSampleDict if hasattr(cfg,"mergeSampleDict") else {}
verbose                 = cfg.verbose if hasattr(cfg,"verbose") else False
skipGitDetail           = cfg.skipGitDetail if hasattr(cfg,"skipGitDetail") else False

if verbose:
    pyPrint("Starting")
start_time = time.time()

pyPrint("\nBegin Summarising\n")
pyPrint("\nInput used: "+outputInfo.outputDir+"\n")
endSequence.run(outputInfo,componentList,mergeSampleDict=mergeSampleDict)

elapsed_time = time.time() - start_time
pyPrint("Time used: "+str(elapsed_time)+"s")
