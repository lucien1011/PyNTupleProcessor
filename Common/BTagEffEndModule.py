from Core.EndModule import EndModule
import ROOT as r
import os
import pickle

r.gROOT.SetBatch(r.kTRUE)

class BTagEffEndModule(EndModule):

    def __init__(self,outputDir,dictPerSample=False,era="2016Moriond17",cutflow="SR"):
           
        self.outputDir = outputDir
        self.cutflow = cutflow
        
        bsfFile = os.environ['BASE_PATH']+"/DataMC/BTagging/"+era+"/btagScaleFactors_CSVv2_Moriond17_B_H.p"
        self.bsfDict = pickle.load( open(bsfFile,"rb") )

        self.dictPerSample = dictPerSample

    def __call__(self,collector):

        if not os.path.exists(self.outputDir):
            os.makedirs(os.path.abspath(self.outputDir))

        outFile = r.TFile(os.path.join(self.outputDir,"bTagEfficiency.root"),"RECREATE")

        if not self.dictPerSample:
            effDict = {}
            samples = ["AllSample",] 
        else:
            samples = collector.mcSamples if not collector.mergeSamples else collector.mergeSamples
        
        for isample,sample in enumerate(samples):
            if self.dictPerSample: effDict = {}
            effDict[sample] = {}
            for wp,measTypes in self.bsfDict.iteritems():
                effDict[sample][wp] = {}
                for meas,sysTypes in measTypes.iteritems():
                    effDict[sample][wp][meas] = {}
                    for sys,jetFlavors in sysTypes.iteritems():
                        effDict[sample][wp][meas][sys] = {}
                        for flav,etaptBins in jetFlavors.iteritems():
                            effDict[sample][wp][meas][sys][flav] = {}
                            
                            histName    = "eff{}_WorkingPoint"+wp+"_MeasType"+meas+"_SysType"+sys+"_JetFlavour"+flav
                            hEff        = collector.getObj(sample,histName.format(''))
                            hEffNum     = collector.getObj(sample,histName.format('Num'))
                            hEffDen     = collector.getObj(sample,histName.format('Den'))

                            hEff.Divide(hEffNum,hEffDen)

                            hEff.Write()

                            for etaptBin in etaptBins:


                                thisEta = etaptBin[0][0]
                                thisPt  = etaptBin[1][0]

                                thisEff = hEff.GetBinContent(hEff.FindBin(thisPt,thisEta))

                                # if eff is zero because of low stats, take eff from previous pt bin
                                if thisEff == 0:
                                    thisPtBin = hEff.GetXaxis().FindBin(thisPt)
                                    thisEtaBin = hEff.GetYaxis().FindBin(thisEta)
                                    while thisEff == 0 and thisPtBin >= 0:
                                        thisPtBin -= 1
                                        thisEff = hEff.GetBinContent(thisPtBin,thisEtaBin)

                                effDict[sample][wp][meas][sys][flav][etaptBin] = thisEff

            if self.dictPerSample:
                self.writePickle(effDict,sample)

        if not self.dictPerSample:
            self.writePickle(effDict,self.cutflow)

        outFile.Close()

    def writePickle(self,dick,name):
        outFileName = self.outputDir+"/btagEfficiencies_"+name+".p"
        pickle.dump(dick, open(outFileName,"wb"))
        print "Written efficiency file:", outFileName
