from Core.Module import Module
from Core.Collection import Collection
from DataMC.BTagging.BTagWorkingPoints import BTagWorkingPoints
import os
import csv
import pickle
import re
from math import *
from Core.Utils.LambdaFunc import LambdaFunc

supportedTaggers            = ["CSV","DeepCSV"]
jetFlavoursDict             = { 0:"2", 4:"1", 5:"0" }
jetFlavourHeavy             = ("0","1")
jetFlavourLight             = ("2")
measTypeDict                = { "0":"comb", "1":"comb", "2":"incl" }
bcfEtaPhiBin                = ( (-2.4, 2.4), (20.0, 1000.0) )
bcfPtBins                   = [0,20,30,40,50,60,70,80,100,120,160,210,260,320,400,500,670,800,1000,999999]

class BTagSFWeighter(Module):
    """
    Carry out b-tag efficiency SF reweighting from SF and Eff pickle files
    following Method 1(a) in https://twiki.cern.ch/twiki/bin/view/CMS/BTagSFMethods
    Also fullsim/fastsim corrections according to:
    https://twiki.cern.ch/twiki/bin/viewauth/CMS/Btag2015FastSimCorrectionFactors
    """
    def __init__(self,name,applySystVariation=True,era="2016Moriond17",tagger = "CSV", btagDisc = 'CSVv2IVFM', opPoint = '1',forceSFToUnity=False,fileTag="",cutflow="SR",jetCollName="selJets25",sysType="central"):
        super(BTagSFWeighter,self).__init__(name)

        # working point: 0=Loose, 1=Medium, 2=Tight
        self._opPoint = opPoint
        if not tagger in supportedTaggers: raise ValueError("Tagger {0} is not supported.".format(tagger))
        self._tagger = tagger
        if not btagDisc in BTagWorkingPoints: raise ValueError("B-tag discrminator {0} not found".format(btagDisc))
        self._btagDisc = btagDisc

        # hadronFlavour to csvFlavour conversion
        self._jetFlavorsDict = jetFlavoursDict
        self._jetFlavorsHeavy = jetFlavourHeavy
        self._jetFlavorsLight = jetFlavourLight

        # use incl for light jets, comb for b,c jets
        self._measTypeDict = measTypeDict

        self._btagDiscWP = BTagWorkingPoints[self._btagDisc][1]

        self._applySystVariation = applySystVariation
        self._forceSFToUnity = forceSFToUnity

        self._bcfEtaPhiBin = bcfEtaPhiBin
        self._bcfPtBins = bcfPtBins 

        self.era = era
        self.fileTag = fileTag
        self.cutflow = cutflow
        self.jetCollName = jetCollName
        self.sysType = sysType
    
    def begin(self):

        if self.dataset.isData:          return True
        
        #if    self._PSet.systVar is None:   self.sysType = "central"
        #elif  self._PSet.systVar == "Up":   self.sysType = "up"
        #elif  self._PSet.systVar == "Down": self.sysType = "down"

        self.bsfFile = os.environ['BASE_PATH']+"/DataMC/BTagging/"+self.era+"/btagScaleFactors"+self.fileTag+".p"
        #self.bsfFile = os.environ['ALPHATOOLSDIR']+"/Data/BTagging/"+self.era+"/btagScaleFactors_CSVv2_Moriond17_B_F.p"
        #self.bsfFile = os.environ['ALPHATOOLSDIR']+"/Data/BTagging/"+self.era+"/btagScaleFactors_CSVv2_Moriond17_G_H.p"

        self.applyCF = False
        if "SMS" in self.dataset.name:
            pass
            
            #self.applyCF = True

            #if   "T1"   in self._sample.parent or "T5"   in self._sample.parent: mSUS = int(re.findall('(?<=mGluino-)\d+', self._sample.name)[0])
            #elif "T2qq" in self._sample.parent: mSUS = int(re.findall('(?<=mSquark-)\d+', self._sample.name)[0])
            #elif "T2tt" in self._sample.parent: mSUS = int(re.findall('(?<=mStop-)\d+',   self._sample.name)[0])
            #elif "T2cc" in self._sample.parent: mSUS = int(re.findall('(?<=mStop-)\d+',   self._sample.name)[0])
            #elif "T2-4bd" in self._sample.parent: mSUS = int(re.findall('(?<=mStop-)\d+',   self._sample.name)[0])
            #elif "T2mixed" in self._sample.parent: mSUS = int(re.findall('(?<=mStop-)\d+',   self._sample.name)[0])
            #elif "T2bb" in self._sample.parent: mSUS = int(re.findall('(?<=mSbottom-)\d+',self._sample.name)[0])
            #elif "T2tb" in self._sample.parent: mSUS = int(re.findall('(?<=mStop-)\d+',self._sample.name)[0])
            #elif "T2bW_X05" in self._sample.parent: mSUS = int(re.findall('(?<=mStop-)\d+',self._sample.name)[0])
            #mLSP = int(self._sample.name.split("mLSP-")[1].split("_")[0])

            #splitting = splittingType(mSUS,mLSP)
            #parent = self._sample.parent

            #self.bcfFile = os.environ['ALPHATOOLSDIR']+"/Data/BTagging/"+self.era+"/btagScaleFactors_"+parent+"_"+splitting+".p"
            #self.effFile = os.environ['ALPHATOOLSDIR']+"/Data/BTagging/"+self.era+"/btagEfficiencies_"+parent+"_"+splitting+".p"

            #if not os.path.exists(self.bcfFile):
            #    self.bcfFile = os.environ['ALPHATOOLSDIR']+"/Data/BTagging/"+self.era+"/btagScaleFactors_combined.p"

            #if not os.path.exists(self.effFile):
            #    print "WARNING: b-tag efficiencies not available for sample", self._sample.name
            #    print "Will only apply nominal scale factors"
            #    self.applyCF = False
            #    self.effFile = os.environ['ALPHATOOLSDIR']+"/Data/BTagging/"+self.era+"/btagEfficiencies_"+self._PSet.name+".p"
        
        else:
            self.effFile = os.environ['BASE_PATH']+"/DataMC/BTagging/"+self.era+"/btagEfficiencies_"+self.cutflow+".p"

        self.bsfDict = pickle.load( open(self.bsfFile,"rb") )
        self.effDict = pickle.load( open(self.effFile,"rb") )
        self.bcfDict = pickle.load( open(self.bcfFile,"rb") ) if self.applyCF else None

        self.evalDict = self.makeEvalDict(self.bsfDict)

    #@staticmethod
    def makeEvalDict(self,bsfDict):
        evalDict = {}
        for op,measDict in bsfDict.iteritems():
            if op not in evalDict: evalDict[op] = {}
            for meas,sysDict in measDict.iteritems():
                if meas not in evalDict[op]: evalDict[op][meas] = {}
                for sys,flavDict in sysDict.iteritems():
                    if sys not in evalDict[op][meas]: evalDict[op][meas][sys] = {}
                    for flav,etaptDict in flavDict.iteritems():
                        if flav not in evalDict[op][meas][sys]: evalDict[op][meas][sys][flav] = {}
                        for etapt,sf in etaptDict.iteritems():
                            #evalDict[op][meas][sys][flav][etapt] = eval("lambda x: "+bsfDict[op][meas][sys][flav][etapt])
                            evalDict[op][meas][sys][flav][etapt] = LambdaFunc("x: "+bsfDict[op][meas][sys][flav][etapt])
        return evalDict

    def end(self):
        if self.dataset.isMC:
            for op,measDict in self.evalDict.iteritems():
                for meas,sysDict in measDict.iteritems():
                    for sys,flavDict in sysDict.iteritems():
                        for flav,etaptDict in flavDict.iteritems():
                            for etapt,sf in etaptDict.iteritems():
                                self.evalDict[op][meas][sys][flav][etapt].end()

    @staticmethod
    def returnJetInfo(jet,jetFlavDict,measTypeDict,bsfDict,opPoint,sysType,bcfPtBins):
        jetPt   = jet.pt
        jetEta  = abs(jet.eta)
        jetFlav = jetFlavDict[jet.hadronFlavour]
        measType = measTypeDict[jetFlav]
        etaptBins    = bsfDict[opPoint][measType][sysType][jetFlav]
        etaptBins_Up = bsfDict[opPoint][measType]["up"][jetFlav]
        etaptBins_Do = bsfDict[opPoint][measType]["down"][jetFlav]
        
        minPt = min(etaptbin[1][0] for etaptbin in etaptBins)
        maxPt = max(etaptbin[1][1] for etaptbin in etaptBins)

        doubleUncertainty = False

        if jetPt < minPt: 
            jetPtSF = minPt + 1E-4
            doubleUncertainty = True
        elif jetPt > maxPt: 
            jetPtSF = maxPt - 1E-4
            doubleUncertainty = True
        else:
            jetPtSF = jetPt
        
        minPtCF = bcfPtBins[1]
        maxPtCF = bcfPtBins[-2]
        
        doubleUncertaintyCF = False
        
        if jetPt < minPtCF:
            jetPtCF = minPtCF + 1E-4
            doubleUncertaintyCF = True
        elif jetPt > maxPtCF:
            jetPtCF = maxPtCF - 1E-4
            doubleUncertaintyCF = True
        else:
            jetPtCF = jetPt

        skipEvent = False 
        
        for etaptBin in etaptBins:
            if etaptBin[0][0] <= jetEta < etaptBin[0][1] and etaptBin[1][0] <= jetPtSF < etaptBin[1][1] :
                break
        else:
            # ignore jets outside tracker acceptance
            skipEvent = True
 
        for etaptBin_Up in etaptBins_Up:
            if etaptBin_Up[0][0] <= jetEta < etaptBin_Up[0][1] and etaptBin_Up[1][0] <= jetPtSF < etaptBin_Up[1][1] :
                break
        
        for etaptBin_Do in etaptBins_Do:
            if etaptBin_Do[0][0] <= jetEta < etaptBin_Do[0][1] and etaptBin_Do[1][0] <= jetPtSF < etaptBin_Do[1][1] :
                break
        if skipEvent:
            return False
        else:
            return jetFlav,measType,etaptBin,etaptBin_Up,etaptBin_Do,doubleUncertainty,jetPtSF,doubleUncertaintyCF,jetPtCF

    @staticmethod
    def safe_div(num, den, fail_val=1.):
        try:
            ratio = num / den
        except ZeroDivisionError:
            ratio = fail_val
        return ratio

    def analyze(self,event):

        if self.dataset.isData:          return True

        mcTag     = 1.
        mcNoTag   = 1.
        dataTag   = 1.
        dataNoTag = 1.

        mcTag_Up     = 1.
        mcNoTag_Up   = 1.
        dataTag_Up   = 1.
        dataNoTag_Up = 1.

        mcTag_Do     = 1.
        mcNoTag_Do   = 1.  
        dataTag_Do   = 1.
        dataNoTag_Do = 1.

        mcTagLight_Up     = 1.
        mcNoTagLight_Up   = 1.
        dataTagLight_Up   = 1.
        dataNoTagLight_Up = 1.

        mcTagLight_Do     = 1.
        mcNoTagLight_Do   = 1.
        dataTagLight_Do   = 1.
        dataNoTagLight_Do = 1.

        mcTagCFb_Up     = 1.
        mcNoTagCFb_Up   = 1.
        dataTagCFb_Up   = 1.
        dataNoTagCFb_Up = 1.

        mcTagCFb_Do     = 1.
        mcNoTagCFb_Do   = 1.
        dataTagCFb_Do   = 1.
        dataNoTagCFb_Do = 1.

        mcTagCFc_Up     = 1.
        mcNoTagCFc_Up   = 1.
        dataTagCFc_Up   = 1.
        dataNoTagCFc_Up = 1.

        mcTagCFc_Do     = 1.
        mcNoTagCFc_Do   = 1.
        dataTagCFc_Do   = 1.
        dataNoTagCFc_Do = 1.

        mcTagCFl_Up     = 1.
        mcNoTagCFl_Up   = 1.
        dataTagCFl_Up   = 1.
        dataNoTagCFl_Up = 1.

        mcTagCFl_Do     = 1.
        mcNoTagCFl_Do   = 1.
        dataTagCFl_Do   = 1.
        dataNoTagCFl_Do = 1.

        jets = getattr(event,self.jetCollName)

        for jet in jets:

            results = self.returnJetInfo(jet,self._jetFlavorsDict,self._measTypeDict,self.bsfDict,self._opPoint,self.sysType,self._bcfPtBins)
            
            if results != False:
                jetFlav,measType,etaptBin,etaptBin_Up,etaptBin_Do,doubleUncertainty,jetPtSF,doubleUncertaintyCF,jetPtCF = results
            else:
                # Skip jet if this is out of tracker acceptance
                continue
            
            # scale factor
            x     = jetPtSF
            SF    = self.evalDict[self._opPoint][measType][self.sysType][jetFlav][etaptBin](x)
            SF_Up = self.evalDict[self._opPoint][measType]["up"][jetFlav][etaptBin_Up](x) if jetFlav in self._jetFlavorsHeavy else SF
            SF_Do = self.evalDict[self._opPoint][measType]["down"][jetFlav][etaptBin_Do](x) if jetFlav in self._jetFlavorsHeavy else SF
            SFLight_Up = self.evalDict[self._opPoint][measType]["up"][jetFlav][etaptBin_Up](x) if jetFlav in self._jetFlavorsLight else SF
            SFLight_Do = self.evalDict[self._opPoint][measType]["down"][jetFlav][etaptBin_Do](x) if jetFlav in self._jetFlavorsLight else SF

            CF = evalCF(self.bcfDict[self._opPoint]["fastsim"][self.sysType][jetFlav][self._bcfEtaPhiBin],jetPtCF,self._bcfPtBins) if self.applyCF else 1.
            CFb_Up = evalCF(self.bcfDict[self._opPoint]["fastsim"]["up"][jetFlav][self._bcfEtaPhiBin],jetPtCF,self._bcfPtBins) if self.applyCF and jetFlav == "0" else 1.
            CFb_Do = evalCF(self.bcfDict[self._opPoint]["fastsim"]["down"][jetFlav][self._bcfEtaPhiBin],jetPtCF,self._bcfPtBins) if self.applyCF and jetFlav == "0" else 1.
            CFc_Up = evalCF(self.bcfDict[self._opPoint]["fastsim"]["up"][jetFlav][self._bcfEtaPhiBin],jetPtCF,self._bcfPtBins) if self.applyCF and jetFlav == "1" else 1.
            CFc_Do = evalCF(self.bcfDict[self._opPoint]["fastsim"]["down"][jetFlav][self._bcfEtaPhiBin],jetPtCF,self._bcfPtBins) if self.applyCF and jetFlav == "1" else 1.
            CFl_Up = evalCF(self.bcfDict[self._opPoint]["fastsim"]["up"][jetFlav][self._bcfEtaPhiBin],jetPtCF,self._bcfPtBins) if self.applyCF and jetFlav == "2" else 1.
            CFl_Do = evalCF(self.bcfDict[self._opPoint]["fastsim"]["down"][jetFlav][self._bcfEtaPhiBin],jetPtCF,self._bcfPtBins) if self.applyCF and jetFlav == "2" else 1.

            if doubleUncertainty:
                SF_Up = 2*(SF_Up - SF) + SF
                SF_Do = 2*(SF_Do - SF) + SF

                SFLight_Up = 2*(SFLight_Up - SF) + SF
                SFLight_Do = 2*(SFLight_Do - SF) + SF

            if doubleUncertaintyCF:
                CFb_Up = 2*(CFb_Up - CF) + CF
                CFb_Do = 2*(CFb_Do - CF) + CF

                CFc_Up = 2*(CFc_Up - CF) + CF
                CFc_Do = 2*(CFc_Do - CF) + CF

                CFl_Up = 2*(CFl_Up - CF) + CF
                CFl_Do = 2*(CFl_Do - CF) + CF


            # efficiency
            sampleKey = self.effDict.keys()[0] if self.applyCF else "AllSample"
            eff    = self.effDict[sampleKey][self._opPoint][measType][self.sysType][jetFlav][etaptBin]
            eff_Up = self.effDict[sampleKey][self._opPoint][measType]["up"][jetFlav][etaptBin_Up] if jetFlav in self._jetFlavorsHeavy else eff
            eff_Do = self.effDict[sampleKey][self._opPoint][measType]["down"][jetFlav][etaptBin_Do] if jetFlav in self._jetFlavorsHeavy else eff
            effLight_Up = self.effDict[sampleKey][self._opPoint][measType]["up"][jetFlav][etaptBin_Up] if jetFlav in self._jetFlavorsLight else eff
            effLight_Do = self.effDict[sampleKey][self._opPoint][measType]["down"][jetFlav][etaptBin_Up] if jetFlav in self._jetFlavorsLight else eff

            effCFb_Up = self.effDict[sampleKey][self._opPoint][measType]["up"][jetFlav][etaptBin_Up] if self.applyCF and jetFlav == "0" else eff
            effCFb_Do = self.effDict[sampleKey][self._opPoint][measType]["down"][jetFlav][etaptBin_Up] if self.applyCF and jetFlav == "0" else eff
            effCFc_Up = self.effDict[sampleKey][self._opPoint][measType]["up"][jetFlav][etaptBin_Up] if self.applyCF and jetFlav == "1" else eff
            effCFc_Do = self.effDict[sampleKey][self._opPoint][measType]["down"][jetFlav][etaptBin_Up] if self.applyCF and jetFlav == "1" else eff
            effCFl_Up = self.effDict[sampleKey][self._opPoint][measType]["up"][jetFlav][etaptBin_Up] if self.applyCF and jetFlav == "2" else eff
            effCFl_Do = self.effDict[sampleKey][self._opPoint][measType]["down"][jetFlav][etaptBin_Up] if self.applyCF and jetFlav == "2" else eff

            # tagged
            if getattr(jet,"btag"+self._tagger) > self._btagDiscWP:

                mcTag   *= eff
                dataTag *= eff * SF * CF

                mcTag_Up   *= eff_Up
                dataTag_Up *= eff_Up * SF_Up * CF

                mcTag_Do   *= eff_Do
                dataTag_Do *= eff_Do * SF_Do * CF

                mcTagLight_Up   *= effLight_Up
                dataTagLight_Up *= effLight_Up * SFLight_Up * CF

                mcTagLight_Do   *= effLight_Do
                dataTagLight_Do *= effLight_Do * SFLight_Do * CF

                mcTagCFb_Up   *= effCFb_Up
                dataTagCFb_Up *= effCFb_Up * SF * CFb_Up

                mcTagCFb_Do   *= effCFb_Do
                dataTagCFb_Do *= effCFb_Do * SF * CFb_Do

                mcTagCFc_Up   *= effCFc_Up
                dataTagCFc_Up *= effCFc_Up * SF * CFc_Up

                mcTagCFc_Do   *= effCFc_Do
                dataTagCFc_Do *= effCFc_Do * SF * CFc_Do

                mcTagCFl_Up   *= effCFl_Up
                dataTagCFl_Up *= effCFl_Up * SF * CFl_Up

                mcTagCFl_Do   *= effCFl_Do
                dataTagCFl_Do *= effCFl_Do * SF * CFl_Do

            # not tagged
            else:

                mcNoTag   *= (1 - eff)
                dataNoTag *= (1 - eff * SF * CF)

                mcNoTag_Up   *= (1 - eff_Up)
                dataNoTag_Up *= (1 - eff_Up * SF_Up * CF)

                mcNoTag_Do   *= (1 - eff_Do)
                dataNoTag_Do *= (1 - eff_Do * SF_Do * CF)

                mcNoTagLight_Up   *= (1 - effLight_Up)
                dataNoTagLight_Up *= (1 - effLight_Up * SFLight_Up * CF)

                mcNoTagLight_Do   *= (1 - effLight_Do)
                dataNoTagLight_Do *= (1 - effLight_Do * SFLight_Do * CF)

                mcNoTagCFb_Up   *= (1 - effCFb_Up)
                dataNoTagCFb_Up *= (1 - effCFb_Up * SF * CFb_Up)

                mcNoTagCFb_Do   *= (1 - effCFb_Do)
                dataNoTagCFb_Do *= (1 - effCFb_Do * SF * CFb_Do)

                mcNoTagCFc_Up   *= (1 - effCFc_Up)
                dataNoTagCFc_Up *= (1 - effCFc_Up * SF * CFc_Up)

                mcNoTagCFc_Do   *= (1 - effCFc_Do)
                dataNoTagCFc_Do *= (1 - effCFc_Do * SF * CFc_Do)

                mcNoTagCFl_Up   *= (1 - effCFl_Up)
                dataNoTagCFl_Up *= (1 - effCFl_Up * SF * CFl_Up)

                mcNoTagCFl_Do   *= (1 - effCFl_Do)
                dataNoTagCFl_Do *= (1 - effCFl_Do * SF * CFl_Do)                

        
        event.bsfWeight      = self.safe_div(dataTag * dataNoTag, mcTag * mcNoTag)

        event.bsfWeight_Up   = self.safe_div(dataTag_Up * dataNoTag_Up, mcTag_Up * mcNoTag_Up, event.bsfWeight)
        event.bsfWeight_Down = self.safe_div(dataTag_Do * dataNoTag_Do, mcTag_Do * mcNoTag_Do, event.bsfWeight)

        event.bsfLightWeight_Up   = self.safe_div(dataTagLight_Up * dataNoTagLight_Up, mcTagLight_Up * mcNoTagLight_Up, event.bsfWeight)
        event.bsfLightWeight_Down = self.safe_div(dataTagLight_Do * dataNoTagLight_Do, mcTagLight_Do * mcNoTagLight_Do, event.bsfWeight)

        event.bsfCFbWeight_Up   = self.safe_div(dataTagCFb_Up * dataNoTagCFb_Up, mcTagCFb_Up * mcNoTagCFb_Up, event.bsfWeight)
        event.bsfCFbWeight_Down = self.safe_div(dataTagCFb_Do * dataNoTagCFb_Do, mcTagCFb_Do * mcNoTagCFb_Do, event.bsfWeight)

        event.bsfCFcWeight_Up   = self.safe_div(dataTagCFc_Up * dataNoTagCFc_Up, mcTagCFc_Up * mcNoTagCFc_Up, event.bsfWeight)
        event.bsfCFcWeight_Down = self.safe_div(dataTagCFc_Do * dataNoTagCFc_Do, mcTagCFc_Do * mcNoTagCFc_Do, event.bsfWeight)

        event.bsfCFlWeight_Up   = self.safe_div(dataTagCFl_Up * dataNoTagCFl_Up, mcTagCFl_Up * mcNoTagCFl_Up, event.bsfWeight)
        event.bsfCFlWeight_Down = self.safe_div(dataTagCFl_Do * dataNoTagCFl_Do, mcTagCFl_Do * mcNoTagCFl_Do, event.bsfWeight)

        event.bsfWeight_Up   /= event.bsfWeight
        event.bsfWeight_Down /= event.bsfWeight

        event.bsfLightWeight_Up   /= event.bsfWeight
        event.bsfLightWeight_Down /= event.bsfWeight

        event.bsfCFbWeight_Up   /= event.bsfWeight
        event.bsfCFbWeight_Down /= event.bsfWeight

        event.bsfCFcWeight_Up   /= event.bsfWeight
        event.bsfCFcWeight_Down /= event.bsfWeight

        event.bsfCFlWeight_Up   /= event.bsfWeight
        event.bsfCFlWeight_Down /= event.bsfWeight

        if self._forceSFToUnity: event.bsfWeight = 1.
        event.weight *= event.bsfWeight 

        return True



def splittingType(mSUS,mLSP):

    if mSUS - mLSP < 401:
        return "compressed"
    else: 
        return "uncompressed"


def evalCF(formula,x,ptBins):

    # FIXME: This is a horrible hack
    CFs = map( float, re.findall("\d+\.\d+", formula) )

    for i in range(len(ptBins)-1):
        if ptBins[i] <= x < ptBins[i+1]:
            return CFs[i-1]

    else: 
        sys.exit("Jet pT out of bounds")
